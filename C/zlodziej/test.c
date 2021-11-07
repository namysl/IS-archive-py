void wstaw(unsigned x, wezel **korzen){
    wezel *q = *korzen,  *p = (wezel*)malloc(sizeof(wezel));
    if (p == 0){
        printf("brak pamieci");
        return;
    }
    *p = (wezel) (x, 0,0);
    if (korzen==0){
        *korzen=p;
        return;
    }
    while (q){
        if (q->number < x){
            if (q->prawy == 0){
                q->prawy = p;
                break;
            }
            q=q->prawy;
        }
        else{
            if (q->lewy == 0){
                q->lewy=p;
                break;
            }
            q=q->lewy;

        }
    }


}
