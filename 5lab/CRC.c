#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Функция для вывода
int printus(int pack[], int N, int G)
{
    printf("Пакет: ");
    for(int i = 0; i < N + G - 1; i++)
        printf("%d ", pack[i]);
    printf("\n");
    return 0;
}

// Функция для выполнения операции деления с остатком (CRC)
int procces(int pack[], int del[], int ost[], int N, int G){

    // Вычисление остатка от деления
    for(int i = 0; i < G - 1; i++)
    {
        ost[i] = pack[i + 1] ^ del[i + 1];
    }
    ost[G - 1] = pack[G];

    for(int i = G + 1; i < N + G - 1; i++)
    {
        if(ost[0] != 0)
            for(int j = 0; j < G - 1; j++)
                ost[j] = ost[j + 1] ^ del[j + 1];
        else
            for(int j = 0; j < G - 1; j++)
                ost[j] = ost[j + 1];
        ost[G - 1] = pack[i];
    }

    // Поправка остатка
    if(ost[0] != 0)
        for(int j = 0; j < G; j++)
            ost[j] = ost[j] ^ del[j];
    else
        for(int j = 0; j < G; j++)
            ost[j] = ost[j];
    return 0;
}

int main() {
    srand(time(NULL));

    int N = 21, G = 8; // Размеры пакета и полинома
    int pack[N + G - 1], ost[G]; // Массивы для хранения пакета и остатка
    pack[0] = 1;

    // Генерация случайных битов для пакета
    for(int i = 1; i < N; i++)
        pack[i] = rand() % 2;

    // Заполнение нулями для дополнения до N + G - 1 элементов
    for(int i = N; i < N + G - 1; i++)
        pack[i] = 0;

    // Вывод начального состояния пакета
    printus(pack, N, G);

    int del[] = {1,0,1,1,1,1,1,1}; // Полином деления
    procces(pack, del, ost, N, G);

    // Вывод остатка от деления
    printf("Остаток от деления: ");
    for(int i = 1; i < G; i++)
        printf("%d ", ost[i]);
    printf("\n");

    // Коррекция ошибок в пакете
    for(int i = N; i < N + G - 1; i++)
        pack[i] = ost[i - N + 1];
    
    // Вывод исправленного пакета
    printus(pack, N, G);
    procces(pack, del, ost, N, G);

    // Повторный вывод остатка от деления
    printf("Остаток от деления: ");
    for(int i = 1; i < G; i++)
        printf("%d ", ost[i]);
    printf("\n");

    // Проверка наличия ошибок
    for(int i = 0; i < G; i++)
    {    if(ost[i] == 1)
        {
            printf("Ошибка присутствует");
            break;    
        }
        if(i == G - 1)
            printf("Ошибки не найдено");
    }
    printf("\n");

    //Те-же самые действия, только для пакета размером 250
    N = 250;
    int pack2[N + G - 1], ost2[G];
    pack2[0] = 1;

    for(int i = 1; i < N; i++)
        pack2[i] = rand() % 2;
    
    for(int i = N; i < N + G - 1; i++)
        pack2[i] = 0;
    
    printus(pack2, N, G);
    procces(pack2, del, ost2, N, G);

    printf("Остаток от деления: ");
    for(int i = 1; i < G; i++)
        printf("%d ", ost2[i]);
    printf("\n");
    
    for(int i = N; i < N + G - 1; i++)
        pack2[i] = ost2[i - N + 1];
    
    printus(pack2, N, G);
    procces(pack2, del, ost2, N, G);
    
    printf("Остаток от деления: ");
    for(int i = 1; i < G; i++)
        printf("%d ", ost2[i]);
    printf("\n");
    
    for(int i = 0; i < G; i++)
    {    if(ost2[i] == 1)
        {
            printf("Ошибка присутствует");
            break;    
        }
        if(i == G - 1)
            printf("Ошибки не найдено");
    }
    printf("\n");

    //Проверка ошибок при искажении битов
    int pack3[N + G - 1], ost3[G], pack4[N + G - 1], pack5[N + G - 1];
    int error = 0, unerror = 0;
    pack3[0] = 1;
    pack5[0] = 1;
    
    for(int i = 1; i < N; i++)
    {
        pack3[i] = rand() % 2;
        pack5[i] = rand() % 2;
    }
    
    for(int i = N; i < N + G - 1; i++)
    {    
        pack3[i] = 0;
        pack5[i] = 0;
    }
    
    //Проверка при искажении общего числа битов
    for(int k = N + G - 1; k > 0; k--)
    {
        for(int i = 0; i < N + G - 1; i++)
            pack4[i] = pack3[i];
        
        procces(pack4, del, ost3, N, G);
        
        for(int i = N; i < N + G - 1; i++)
            pack4[i] = ost3[i - N + 1];
        
        procces(pack4, del, ost3, N, G);
        
        for(int i = 0; i < G; i++)
        {   
            if(ost3[i] == 1)
            {
                error++;
                break;    
            }
            
            if(i == G - 1)
                unerror++;
        
        }
        
        if(pack3[k] == 0)
            pack3[k] = 1;
        
        else
            pack3[k] = 0;
    }
    printf("При искажении общего числа битов %d - ошибок %d - нет ошибок\n", error, unerror);

    error = 0;
    unerror = 0;

    //Проверка при искажении одного бита в пакете
    for(int k = N + G - 2; k > 0; k--)
    {
        for(int i = 0; i < N + G - 1; i++)
            pack4[i] = pack5[i];
        
        procces(pack4, del, ost3, N, G);
        
        for(int i = N; i < N + G - 1; i++)
            pack4[i] = ost3[i - N + 1];
        
        procces(pack4, del, ost3, N, G);
        
        for(int i = 0; i < G; i++)
        {   
            if(ost3[i] == 1)
            {
                error++;
                break;    
            }
            
            if(i == G - 1)
                unerror++;
        }
        
        if(pack5[k] == 0)
            pack5[k] = 1;
        
        else
            pack5[k] = 0;
        
        if(pack5[k + 1] == 0)
            pack5[k + 1] = 1;
        
        else
            pack5[k + 1] = 0;
    }
    printf("При искажении одного бита %d - ошибок %d - нет ошибок\n", error, unerror);
    return 0;
}