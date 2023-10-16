import requests
from datetime import datetime
import xml.etree.ElementTree as ET

pair = input("Qual o par? ")

# Define the URL for the currency pair in XML format
xml_url = f"http://economia.awesomeapi.com.br/xml/{pair}/1"

# Helper function to parse XML data
def parse_xml(data):
    root = ET.fromstring(data)
    return root.find(".//bid").text

# Function to fetch and print exchange rate data in XML format
def fetch_and_print_xml(url):
    requisicao = requests.get(url)
    if requisicao.status_code == 200:
        cotacao = parse_xml(requisicao.text)
        print(f"Cotação atualizada. {datetime.now()}\n{pair}: R${cotacao}")
    else:
        print(f"Error: Failed to retrieve data from the API. Status code: {requisicao.status_code}")

# Fetch and print data in XML format
fetch_and_print_xml(xml_url)
