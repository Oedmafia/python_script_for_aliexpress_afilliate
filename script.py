# The fields where I am using R$ means that I am mentioning the Brazilian Real currency. You can change to the currency used in your affiliation type on Aliexpress.
# Bibliotecas | Libraries
import csv
import requests
import os
import time
import random
import asyncio
import json
from telegram import Bot

# Conectar a API do Bit.ly para encurtamento de links | Connect Bit.ly API for link shortening
BITLY_TOKEN = "" # Insira sua chave de API do bitly | Enter your bitly API key

headers = {
    "Authorization": f"Bearer {BITLY_TOKEN}",
    "Content-Type": "application/json"
}

# Inserindo o nome do arquivo CSV em uma variável | Inserting the CSV file name into a variable
file_csv = "sample_file.csv"

# Função para baixar a imagem | Function to download the image
def download_image(image_url, image_id):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(f"images/{image_id}.jpg", "wb") as f:
            f.write(response.content)

# Função para envio da mensagem/imagem ao Telegram | Function for sending the message/image to Telegram

async def send_image(bot, chat_id, image_id, product, original_price, sale_price, discount, discount_code, value_discount, rating, sales, link):
    # Chamada a API do Bitly para encurtar o link | Bitly API call to shorten the link
    short_link_response = requests.post(
        "https://api-ssl.bitly.com/v4/shorten",
        headers=headers,
        json={"long_url": link}
    )
    short_link = json.loads(short_link_response.text)["link"]

    # Definindo a imagem/mensagem para enviar | Setting the image/message to send
    with open(f"images/{image_id}.jpg", "rb") as f:
        # Fazendo uma verificação se o produto tem código de desconto disponibilizado ao importar a base do portal do aliexpress | Checking if the product has a discount code available when importing the base from the aliexpress portal
        if discount_code == "":
            caption = f"Product name: {product}\nOriginal Price: R$ {original_price}\nSale Price: R$ {sale_price}\nDiscount percentage: {discount}\nSales: {sales}\nRating percentage: {rating}\nLink to purchase: {short_link}"
        else:
            caption = f"Product name: {product}\nOriginal Price: R$ {original_price}\nSale Price: R$ {sale_price}\nDiscount percentage: {discount}\nCode for more discount: {discount_code}\nCode value: {value_discount}\nSales: {sales}\nRating percentage: {rating}\nLink to purchase: {short_link}"
        await bot.send_photo(chat_id=chat_id, photo=f,caption=caption)

async def main():
    # Inicialização do bot do telegram | Telegram bot startup
    bot = Bot(token='YOUR_TOKEN_BOT')
    chat_id = 'YOUR_CHAT_ID'

    # Cria a pasta images caso ela não exista | Create the images folder if it doesn't exist
    if not os.path.exists("image"):
        os.mkdir("images")
    
    # Leitura dos dados do arquivo CSV | Reading data from CSV file
    with open(file_csv, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) # Pula o cabeçalho | Skip header
        i = 1
        n = sum(1 for _ in reader)
        f.seek(0)
        next(reader)
        next(reader)
        products = list(reader)
        random.shuffle(products)
        for row in products:
            product = row[3]
            image_id = row[0].replace("/", "-") # Utilizei o ID do produto para o ID da imagem | I used the Product ID for the Image ID
            image_url = row[1]
            original_price = row[4].replace('BRL','')
            sale_price = row[5].replace('BRL','') # BRL refere-se a moeda Real do Brasil, caso esteja operando com outra moeda lembre-se de alterar 'BRL' para a moeda de sua preferência para ter perfeito funcionamento. | BRL refers to the Brazilian Real currency, if you are operating with another currency, remember to change 'BRL' to the currency of your choice for perfect operation.
            discount = row[6]
            discount_code = row[13]
            value_discount = row[16].replace('BRL','R$')
            sales = row[10]
            rating_info = row[11]
            # Valido se o campo da porcentagem de avaliação retorna um valor válido, dando opção para sim e para não | Valid if the evaluation percentage field returns a valid value, giving option for yes and no
            if rating_info == 'null%':
                rating = 0 + '%'
            else:
                rating = row[11]
            link = row[12]
            
            # Fazendo chamada as funções para baixar a imagem e enviar a mensagem, excluindo a imagem baixada e aguardando para prosseguir o loop | Calling the functions to download the image and send the message, deleting the downloaded image and waiting to continue the loop
            download_image(image_url, image_id)
            await send_image(bot, chat_id, image_id, product, original_price, sale_price, discount, discount_code, value_discount, rating, sales, link)
            os.remove(f"images/{image_id}.jpg")
            print(f"{i} products shipped out of a total of {n}")
            i += 1
            time.sleep(600)

if __name__ == "__main__":
    asyncio.run(main())