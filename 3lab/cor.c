#include <stdio.h>
#include <math.h>

// Функция для вычисления корреляции между двумя массивами a и b
int correlation(int a[], int b[], int n) {
    int sum = 0;
    // Проход по элементам массивов и вычисление суммы произведений соответствующих элементов
    for (int i = 0; i < n; i++)
        sum += a[i] * b[i];
    return sum;
}

// Функция для вычисления нормализованной корреляции между двумя массивами a и b
double correlationnorm(int a[], int b[], int n) {
    double itog;
    int sum = correlation(a, b, n), suma = 0, sumb = 0;
    // Вычисление суммы квадратов элементов каждого массива
    for (int i = 0; i < n; i++) {
        suma += a[i] * a[i];
        sumb += b[i] * b[i];
    }
    // Вычисление нормализованной корреляции путем деления корреляции на произведение квадратных корней сумм квадратов
    itog = sum / sqrt(suma * sumb);
    return itog;
}

int main() {
    // Инициализация размера массивов и самих массивов данных
    int n = 8;
    int a[] = {1, 2, 5, -2, -4, -2, 1, 4};
    int b[] = {3, 6, 7, 0, -5, -4, 2, 5};
    int c[] = {-1, 0, -3, -9, 2, -2, 5, 1};

    // Вычисление корреляций между парами массивов и нормализованных корреляций
    int corab = correlation(a, b, n);
    int corac = correlation(a, c, n);
    int corbc = correlation(b, c, n);
    double cornormab = correlationnorm(a, b, n);
    double cornormac = correlationnorm(a, c, n);
    double cornormbc = correlationnorm(b, c, n);

    // Вывод результатов в виде таблицы
    printf("Корреляция\n\n");
    printf("/ |         a           |           b           |           c           \n");
    printf("__|_____________________|_______________________|_______________________\n");
    printf("a |         -           |           %d         |           %d          \n", corab, corac);
    printf("__|_____________________|_______________________|_______________________\n");
    printf("b |         %d         |           -           |           %d          \n", corab, corbc);
    printf("__|_____________________|_______________________|_______________________\n");
    printf("c |         %d           |           %d         |           -           \n\n", corac, corbc);

    printf("Нормализованная корреляция\n\n");
    printf("/ |         a           |           b           |           c           \n");
    printf("__|_____________________|_______________________|_______________________\n");
    printf("a |         -           |         %lf      |         %lf           \n", cornormab, cornormac);
    printf("__|_____________________|_______________________|_______________________\n");
    printf("b |      %lf       |           -           |        %lf           \n", cornormab, cornormbc);
    printf("__|_____________________|_______________________|_______________________\n");
    printf("c |      %lf       |        %lf      |           -           \n", cornormac, cornormbc);

    return 0;
}
