import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
resposta = requests.get(url)

if resposta.status_code == 200:
    site = BeautifulSoup(resposta.text, 'html.parser')
    citacoes = site.find_all('div', class_='quote')
    
    # Criando e abrindo o arquivo CSV para escrita
    with open('citacoes.csv', mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        
        # Escreve o cabeçalho da planilha
        escritor.writerow(['Numero', 'Autor', 'Frase'])
        
        print(f"--- ENCONTRADAS {len(citacoes)} CITAÇÕES. SALVANDO EM CSV... ---\n")
        
        for i, item in enumerate(citacoes, 1):
            frase = item.find('span', class_='text').text.replace('“', '').replace('”', '')
            autor = item.find('small', class_='author').text
            
            # Salva a linha no arquivo CSV
            escritor.writerow([i, autor, frase])
            
            print(f"[{i}] Salvo: {autor}")

    print("\n✓ Dados salvos com sucesso no arquivo 'citacoes.csv'!")
else:
    print(f"Erro: {resposta.status_code}")

