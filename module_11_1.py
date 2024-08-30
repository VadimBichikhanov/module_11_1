import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from requests.exceptions import ReadTimeout

# Укажите тикер акции и период
ticker = 'AAPL'  # Например, Apple
period = '5d'    # 5 дней (одна неделя)

# Увеличиваем время ожидания для запроса
yf.utils.timeout = 60  # Увеличиваем время ожидания до 60 секунд

# Скачивание данных с повторным запросом
max_retries = 3
for attempt in range(max_retries):
    try:
        data = yf.download(ticker, period=period)
        break
    except ReadTimeout as e:
        if attempt == max_retries - 1:
            raise e
        print(f"Попытка {attempt + 1} не удалась: {e}. Повторная попытка...")

# Проверка, если данные пусты
if data.empty:
    print(f"Данные для акции {ticker} за последние {period} не найдены.")
else:
    # Сохранение данных в файл CSV
    data.to_csv(f'{ticker}_data_{period}.csv')
    print(f"Данные сохранены в файл {ticker}_data_{period}.csv")

    # Вывод данных
    print(data)

    # Построение графика
    data['Close'].plot(title=f'Цена закрытия акции {ticker} за последние {period}')
    plt.xlabel('Дата')
    plt.ylabel('Цена закрытия')
    plt.grid(True)

    # Сохранение графика в файл
    plt.savefig(f'{ticker}_plot_{period}.png')
    plt.close()

    # Загрузка изображения с помощью Pillow и сохранение в другом формате, если нужно
    img = Image.open(f'{ticker}_plot_{period}.png')
    img_rgb = img.convert('RGB')  # Преобразование в режим RGB
    img_rgb.save(f'{ticker}_plot_{period}.jpg')

    print(f"График сохранен в файлы {ticker}_plot_{period}.png и {ticker}_plot_{period}.jpg")

import numpy as np

# Создание массива чисел
arr = np.array([1, 2, 3, 4, 5])

# Вывод исходного массива
print("Исходный массив:", arr)

# Математические операции с массивом
arr_squared = np.square(arr)
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
arr_max = np.max(arr)
arr_min = np.min(arr)

# Вывод результатов операций
print("Массив в квадрате:", arr_squared)
print("Сумма элементов массива:", arr_sum)
print("Среднее значение элементов массива:", arr_mean)
print("Максимальное значение в массиве:", arr_max)
print("Минимальное значение в массиве:", arr_min)