# python_script_for_aliexpress_afilliate
Script for sending messages for telegram with python.

This script must be able to read information from a CSV file whose header will contain the indexes and lines in sequence with information about the respective products.

From this file, the script should run a loop that will download the product image, concatenate information and changes and send the image along with the standard text to a telegram group/channel along with the affiliate link.

At each shipment, the script downloads, renames and deletes the image, counts how many products are in the file and how many have already been sent.