t = (0:100-1)/100;
pi = 3.14;

s1 = cos(2 * pi * t * 1);
s2 = cos(2 * pi * t * 5);
s3 = cos(2 * pi * t * 3);
a = 2 * s1 + 4 * s2 + s3;
b = s1 + s2;

% Вычисление корреляции
corsa = xcorr(s1, a);
corsb = xcorr(s1, b);
disp("Корреляция a s1")
disp(corsa);
disp("Корреляция b s1")
disp(corsb);

% Создание новых сигналов
a = [0.3 0.2 -0.1 4.2 -2 1.5 0];
b = [0.3 4 -2.2 1.6 0.1 0.1 0.2];

% Вычисление корреляции между новыми сигналами
corab = xcorr(a, b);
disp("Корреляция a b")
disp(corab);

% Поиск максимальной корреляции со сдвигом
[cormas, lags] = xcorr(a, b);
[maxznach, maxidx] = max(cormas);
maxsdvig = lags(maxidx) - 1;
disp("Максимальная корреляция");
disp(maxznach);
disp("При сдвиге");
disp(maxsdvig);

% Визуализация результатов
figure;
subplot(3, 1, 1);
plot(corsa);
title("Корреляция a s1");

subplot(3, 1, 2);
plot(corsb);
title("Корреляция b s1");

subplot(3, 1, 3);
plot(lags, cormas);
title("Корреляция со сдвигом b");
