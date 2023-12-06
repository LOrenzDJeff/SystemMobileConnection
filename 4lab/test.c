//группа 132
//х = 1 у = 8
//x = 00001 y = 01000
#include <stdio.h>

void shiftRight(int arr[], int size) {
    int temp = arr[size - 1];

    for (int i = size - 1; i > 0; i--) {
        arr[i] = arr[i - 1];
    }

    arr[0] = temp;
}

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

int main() {
    int x[] = {1, 0, 0, 0, 0};
    int y[] = {0, 0, 0, 1, 0};
    int n = 11;
    int golden[n], shift[n];
    for (int i = 0; i < n; ++i) {
        int goldBit = generateGoldSequence(x, y);
        printf("%d ", goldBit);
        golden[i] = goldBit;
        shift[i] = goldBit;
        //for (int j = 0; j < 5; j++) 
        //    printf("%d ", x[j]);
        //printf("\n");
        //for (int j = 0; j < 5; j++) 
        //    printf("%d ", y[j]);
        //printf("\n");
    }
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
    int num = 1, n2 = 15;
    float itog[n2];
    for (int i = 0; i < n2; ++i){
        for (int j = 0; j < n; ++j)
        {
            if (golden[j] != shift[j])
            {
                num = 0;
                itog[i] = -1.0/13.0;
                break;
            }
        }
        if (num == 1)
            itog[i] = 1;
        printf("%5d", i);
        for (int j = 0; j < n; j++)
            printf(" |     %2d", shift[j]);
        printf(" |     %10f |", itog[i]);
        printf("\n");
        printf("______|");
        for (int k = 0; k < n; k++)
            printf("________|");
        printf("________________|");
        printf("\n");
        num = 1;
        shiftRight(shift, n);

    }
  /*  for (int i = 0; i < n; i++)
    {
        printf("%5d", i);
        for (int j = 0; j < n; j++)
            printf(" |     %2d", shift[j]);
        printf(" |     %10f |", itog[i]);
        printf("\n");
        printf("______|");
        for (int k = 0; k < n; k++)
            printf("________|");
        printf("________________|");
        printf("\n");
    }*/
    //printf("__|_____________________|_______________________|_______________________\n");
    //printf("a |         -           |           %d         |           %d          \n", corab, corac);
   // printf("__|_____________________|_______________________|_______________________\n");
    printf("\n");
    return 0;   
}

