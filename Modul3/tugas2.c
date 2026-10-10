#include <stdio.h>

int main() {
    int n, baris, angka, i, space;

    while (1) {
        printf("Masukkan tinggi setengah menara (2 - 15): ");
        scanf("%d", &n);
        if (n < 2 || n > 15) {
            printf("Tinggi setengah menara tidak valid, harus diantara 2 sampai 15!\n");
            continue;
        } else {
            break;
        }
    }

    for (baris = 1; baris <= n; baris++) {
        space = (n - baris) * 2;

        for (i = 0; i < space; i++) {
            printf(" ");
        }
        for (angka = 1; angka <= baris; angka++) {
            printf("%d ", angka % 10);
        }
        for (angka = baris - 1; angka >= 1; angka--) {
            printf("%d ", angka % 10);
        }
        printf("\n");
    }

    baris = n - 1;
    while (baris >= 1) {
        space = (n - baris) * 2;

        for (i = 0; i < space; i++) {
            printf(" ");
        }
        for (angka = 1; angka <= baris; angka++) {
            printf("%d ", angka % 10);
        }
        for (angka = baris - 1; angka >= 1; angka--) {
            printf("%d ", angka % 10);
        }
        printf("\n");
        baris--;
    }

    return 0;
}