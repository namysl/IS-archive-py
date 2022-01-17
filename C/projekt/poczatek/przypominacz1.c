#include <stdio.h>
#include <time.h>

time_t czas;
struct tm *data;

void data_ctime(){
    time_t czas = 0;
    time( & czas );
    printf( "%s", ctime( & czas ) );
}

void data_timet(){
    czas = time(0);
    data = localtime(&czas);
    printf("%d %d %d %d:%d:%d ", data->tm_year+1900, data->tm_mon+1, data->tm_mday, data->tm_hour, data->tm_min, data->tm_sec);

}

int main(){

    data_ctime();
    data_timet();

    return 0;
}
