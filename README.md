# Python script for aliexpress afilliate

## PT-BR
Script para envio de mensagens para telegram com python.

Este script deve ser capaz de ler as informações de um arquivo CSV cujo cabeçalho conterá os índices e as linhas em sequência com as informações dos respectivos produtos.

A partir desse arquivo, o script deverá rodar um loop que fará o download da imagem do produto, concatenará as informações e alterações e enviará a imagem junto com o texto padrão para um grupo/canal do telegram junto com o link de afiliado.

A cada remessa, o script baixa, renomeia e apaga a imagem, conta quantos produtos estão no arquivo e quantos já foram enviados.

## EN
Script for sending messages for telegram with python.

This script must be able to read information from a CSV file whose header will contain the indexes and lines in sequence with information about the respective products.

From this file, the script should run a loop that will download the product image, concatenate information and changes and send the image along with the standard text to a telegram group/channel along with the affiliate link.

At each shipment, the script downloads, renames and deletes the image, counts how many products are in the file and how many have already been sent.

## Requisitos para utilização do Script | Requirements for using the Script

### PT-BR
- Python 3 e as bibliotecas: python-telegram-bot, asyncio (essas são as que devem ser previamente instaladas pois não veem com o Python).
- Conta no telegram e um Token de Bot ao criar ele no BotFather.
- CHAT ID do seu canal/grupo que deseja enviar as mensagens. Pode conseguir com o o Bot IDBot.
- Para utilização do Bitly para encurtar os links precisará também de uma conta e um token de API da plataforma.
- Conta como afiliado na Aliexpress para poder baixar as bases de produtos conforme o nicho que vá divulgar.

### EN
- Python 3 and the libraries: python-telegram-bot, asyncio (these are the ones that must be previously installed as they don't come with Python).
- Telegram account and a Bot Token when creating it in BotFather.
- CHAT ID of your channel/group you want to send messages to. You can get it with the IDBot Bot.
- To use Bitly to shorten links, you will also need an account and a platform API token.
- Account as an affiliate on Aliexpress to be able to download product bases according to the niche you are going to advertise.