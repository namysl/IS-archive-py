#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

void PokerTest(uint32_t* tab,uint32_t n,uint32_t bits,uint32_t shift);

// tablice rozk³adu (chi^2)^(-1) dla alfa=0.00005 i iloœci bitów od 1 do 16 (potrzebne do testu pokerowego)
double chi2d[16]={0.0000, 0.0033, 0.2446, 2.1649, 9.2011, 28.3720, 74.1655, 176.3910, 395.9294,
		856.3608, 1807.4305, 3752.2915, 7702.4312, 15688.1539, 31780.4343, 64135.8807};
double chi2u[16]={16.4481, 22.5547, 31.5124, 46.1678, 71.3986, 116.3546, 198.6229, 352.4279, 644.9045,
		1208.4807, 2305.4147, 4456.5556, 8698.4169, 17096.6945, 33772.4144, 66952.9681};

// funkcja odczytuje i zwraca licznik wykonanych cykli procesora
uint64_t rdtsc(){
   uint32_t hi, lo;
   __asm__ __volatile__ ("rdtsc" : "=a"(lo), "=d"(hi));
   return ( (uint64_t)lo)|( ((uint64_t)hi)<<32 );
}
// funckcja sprawdza czy procesor posiada wbudowany generator liczb losowych
uint32_t isrndrand(){
	uint32_t wynik;
	__asm__ __volatile__ ("movl $1,%%eax;" "cpuid;" "shr $30,%%ecx;" "andl $1,%%ecx;"
						"movl %%ecx,%0;": "=g"(wynik): :"%eax", "%ebx", "%ecx", "%edx");
	return wynik;
}

// funkcja zwraca liczbê losow¹ u¿ywaj¹c generatora wbudowanego w procesor
void rdrand32(uint32_t *rand){
	__asm__ __volatile__ ("rdrand %0": "=r" (*rand));
}

// Inicjuje MT[] dla generatora Mersenne Twister
uint32_t MT[624];
uint32_t mti = 0;
void InicjujMT(uint32_t x0){
	uint64_t x;
	uint32_t i=0;
	MT[0] = x0;
	do{
		x = MT[i];
		x = (23023 * x) & 0xffffffffull;
		i++;
		x = (    3 * x) & 0xffffffffull;
		MT[i] = x;
	}while(i < 623);
}
// Generator liczb losowych Mersenne Twister
uint32_t MTrand(){
  const uint32_t MA[] = {0,0x9908b0df};
  uint32_t y,i1,i397;
  i1      = mti +   1; if(  i1 > 623) i1 = 0;
  i397    = mti + 397; if(i397 > 623) i397 -= 624;
  y       = (MT[mti] & 0x80000000) | (MT[i1] & 0x7fffffff);
  MT[mti] = MT[i397] ^ (y >> 1) ^ MA[y & 1];
  y       = MT[mti];
  y       ^=  y >> 11;
  y       ^= (y <<  7) & 0x9d2c5680;
  y       ^= (y << 15) & 0xefc60000;
  y       ^=  y >> 18;
  mti     = i1;
  return y;
}

int main(){
    // liczby do przechowywania cykli procesora
    uint64_t sr1,sr2;
    // liczby do przechowywania wartoœci minimalnej i maksymalnej z tablicy
	uint32_t cmin=0xFFFFFFFF,cmax=0;
	// inicjowanie generatorów losowych
	srand(time(0));
	InicjujMT(time(0));
	// rozmiar tablicy i tworzenie tablicy
	uint32_t n=64*1024*1024;
	uint32_t *tabl;
	tabl=(uint32_t*)malloc(n*sizeof(uint32_t));

	if(tabl==0)
		printf("Brak pamieci\n");
	else{
		printf("TABLICA ZAJMUJE %u MB pamieci\n",(n*sizeof(uint32_t))/(1024*1024));
		// sprawdzamy dostêpnoœæ w procesorze generatora liczb losowych
		if(isrndrand()){
			printf("RDRAND dostepne\n");
			// losowanie tablicy za pomoc¹ rdrand
			sr1=rdtsc();
		    for(int i=0;i<n;i++)
			    rdrand32(&(tabl[i]));
		    sr2=rdtsc();
            // znajdujemy maksimum i minimum tablicy
		    for(int i=0;i<n;i++){
			    if(tabl[i]<cmin)
				    cmin=tabl[i];
			    else if(tabl[i]>cmax)
				    cmax=tabl[i];
		    }
		    printf("TESTOWANIE RDRAND: min=%u, max=%u\n",cmin,cmax);
		    printf("Czas wykonania 1 rand %llu cykli\n",(sr2-sr1)/n);
		    // wykonujemy test pokerowy
		    for(int i=0;i<32;i+=4)
			    PokerTest(tabl,n,4,i);
		}
		else
			printf("RDRAND niedostepne\n");
        // sprawdzamy zwyk³y generator liczb losowych
        uint32_t bity=0; for(uint32_t temp=RAND_MAX;temp!=0;temp>>=1) bity++;
        printf("\nRand_max: %u, bity %u",RAND_MAX,bity);
        cmin=0xFFFFFFFF;cmax=0;
        // losujemy tablicê
		sr1=rdtsc();
        for(int i=0;i<n;i++)
		    tabl[i]=rand();
		sr2=rdtsc();
        // znajdujemy maksimum i minimum tablicy
        for(int i=0;i<n;i++){
            if(tabl[i]<cmin)
                cmin=tabl[i];
            else if(tabl[i]>cmax)
                cmax=tabl[i];
        }
        printf("\nTESTOWANIE RAND: min=%u, max=%u\n",cmin,cmax);
        printf("Czas wykonania 1 rand %llu cykli\n",(sr2-sr1)/n);
        // wykonanujemy testu pokerowy
		for(int i=0;i<bity-2;i+=3)
			PokerTest(tabl,n,3,i);

		// sprawdzamy generator Mersenne Twister
		cmin=0xFFFFFFFF;cmax=0;
        // losujemy tablicê
		sr1=rdtsc();
		for(int i=0;i<n;i++)
			tabl[i]=MTrand();
		sr2=rdtsc();
		// znajdujemy maksimum i minimum tablicy
		for(int i=0;i<n;i++){
			if(tabl[i]<cmin)
				cmin=tabl[i];
			else if(tabl[i]>cmax)
				cmax=tabl[i];
		}
		printf("\nTESTOWANIE MTRAND: min=%u, max=%u\n",cmin,cmax);
		printf("Czas wykonania 1 mtrand %llu cykli\n",(sr2-sr1)/n);
		for(int i=0;i<32;i+=4)
			PokerTest(tabl,n,4,i);

        // usuwamy tablicê
        free(tabl);
	}
	printf("\nKoniec");
    char znak;
    scanf("%c",&znak);
    return 0;
}

// funkcja wykonuje test pokerowy i wyœwietla jego wynik
// tab - tablica liczb losowych, n - rozmiar tablicy, bits - iloœæ bitów sprawdzanych, shift - przesuniêcie bitów
// sprawdzane bêd¹ bity od shift do shift+bits-1 z ka¿dego elementu tablicy tab
void PokerTest(uint32_t* tab,uint32_t n,uint32_t bits,uint32_t shift){
	
}
