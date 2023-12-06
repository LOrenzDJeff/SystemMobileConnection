//группа 132
//х = 1 у = 8 x2 = 2 y2 = 3
//x = 00001 y = 01000 x2 = 00010 y2 = 00011
#include <stdio.h>

// Функция циклического сдвига элементов массива вправо
void shiftRight(int arr[], int size) {
    int temp = arr[size - 1];

    for (int i = size - 1; i > 0; i--) {
        arr[i] = arr[i - 1];
    }

    arr[0] = temp;
}

// Функция генерации золотой последовательности на основе x и y
int generateGoldSequence(int x[], int y[]) {
    int summator;
    int newBit = x[4] ^ y[4];

    summator = x[2] ^ x[3];
    shiftRight(x, 5);
    x[0] = summator;


    summator = y[1] ^ y[2];
    shiftRight(y, 5);
    y[0] = summator;

    return newBit;
}

// Вывод таблицы автокорреляции
void printgold(int n, int golden[], int shift[])
{
    printf("\n");
    printf("Сдвиг");
    for (int i = 1; i < n + 1; ++i)
        printf(" | бит %2d", i);
    printf(" | Автокорреляция");
    printf(" |\n");
    printf("______|");
    for (int i = 0; i < n; i++)
        printf("________|");
    printf("________________|");
    printf("\n");
    int n2 = 31;
    int sh = 0, nsh = 0;
    int itog[n2];

    // Расчет автокорреляции для каждого сдвига
    for (int i = 0; i < n2; ++i){
        for (int j = 0; j < n; ++j)
        {
            if (golden[j] == shift[j])
                sh = sh + 1;
            else
                nsh = nsh + 1;
        }
        itog[i] = (sh - nsh);
        sh = 0;
        nsh = 0;
        printf("%5d", i);
        for (int j = 0; j < n; j++)
            printf(" |     %2d", shift[j]);
        printf(" |     %7d/31 |", itog[i]);
        printf("\n");
        printf("______|");
        for (int k = 0; k < n; k++)
            printf("________|");
        printf("________________|");
        printf("\n");
        shiftRight(shift, n);

    }
    printf("\n");
}

// Генерация золотой последовательности и вывод битов на экран
void rashet(int x[], int y[], int golden[], int shift[], int n)
{
    for (int i = 0; i < n; ++i) {
        int goldBit = generateGoldSequence(x, y);
        printf("%d ", goldBit);
        golden[i] = goldBit;
        shift[i] = goldBit;
    }
}

// Вычисление корреляции между двумя последовательностями
int correlation(int a[], int b[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += a[i] * b[i];
    return sum;
}

// Основная функция программы
int main() {
    int x[] = {1, 0, 0, 0, 0};
    int y[] = {0, 0, 0, 1, 0};
    int n = 31;
    int golden[n], shift[n];

    // Генерация и вывод золотой последовательности для x и y
    rashet(x, y, golden, shift, n);
    printgold(n, golden, shift);

    int x2[] = {0, 1, 0, 0, 0};
    int y2[] = {1, 1, 0, 0, 0};
    int golden2[n];
    
    // Генерация и вывод золотой последовательности для x2 и y2
    rashet(x2, y2, golden2, shift, n);
    printgold(n, golden2, shift);

    // Вычисление и вывод взаимной корреляции между двумя последовательностями
    int correltion12 = correlation(golden, golden2, n);
    printf("Взаимная корреляция равна %d\n", correltion12);

    
    return 0;
}