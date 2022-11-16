from bs4 import BeautifulSoup
import requests
import time
import asyncio

async def get_weather():
    url = 'https://yandex.com.am/weather/?lat=53.90228653&lon=27.56183243'  # weather in Minsk
    response = requests.get(url)
    # print(response)  # <Response [200]>

    soup = BeautifulSoup(response.text, 'lxml')
    # print(bs)

    temp = soup.find('span', 'temp__value temp__value_with-unit')
    print(temp.text)


async def main():
    task1 = asyncio.create_task(get_weather())

start_time = time.time()

asyncio.run(main())

print(f'Результат получен за {time.time() - start_time} секунд')
