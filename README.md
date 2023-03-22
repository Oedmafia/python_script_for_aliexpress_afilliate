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