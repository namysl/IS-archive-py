int main() {
    char znak;

    do {
        /*
        instrukcje w menu
        */
        printf("Zakonczyc program? (T/N): ");
        scanf(" %c", &znak);
    } while ((znak != 't') && (znak != 'T'));

    printf("Koniec programu.\n");

    return 0;
}
