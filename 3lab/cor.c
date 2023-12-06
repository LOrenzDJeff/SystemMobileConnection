#include <stdio.h>
#include <math.h>

int correlation(int a[], int b[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += a[i] * b[i];
    return sum;
}

double correlationnorm(int a[], int b[], int n)
{
    double itog;
    int sum = correlation(a, b, n), suma = 0, sumb = 0;
    for (int i = 0; i < n; i++)
    {
        suma += a[i] * a[i];
        sumb += b[i] * b[i];
    }
    itog = sum / sqrt(suma*sumb);
    return itog;
}

int main() 
{
    int n = 8;
    int a[] = {1, 2, 5, -2, -4, -2, 1, 4};
    int b[] = {3, 6, 7, 0, -5, -4, 2, 5};
    int c[] = {-1, 0, -3, -9, 2, -2, 5, 1};

    int corab = correlation(a, b, n);
    int corac = correlation(a, c, n);
    int corbc = correlation(b, c, n);
    double cornormab = correlationnorm(a, b, n);
    double cornormac = correlationnorm(a, c, n); 
    double cornormbc = correlationnorm(b, c, n);
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
    /*printf("Корреляция между a и b: %lf\n", corab);
    //printf("Корреляция между a и c: %lf\n", corac);
    //printf("Корреляция между b и c: %lf\n", corbc);
    //printf("Корреляция между a и b: %lf\n", cornormab);
    //printf("Корреляция между b и c: %lf\n", cornormbc);
    printf("Корреляция между a и c: %lf\n", cornormac);*/
    return 0;
}
