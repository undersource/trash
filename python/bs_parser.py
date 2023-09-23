from bs4 import BeautifulSoup
import requests


def parse(url: str) -> tuple:
    request = requests.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')

    index = soup.find('div', class_='product_index').text
    title = soup.find('h1', class_='product_title').text
    image = soup.find('img', class_='product_image')['src']
    price = soup.find('div', class_='product_price').text

    return (index, title, image, price)
