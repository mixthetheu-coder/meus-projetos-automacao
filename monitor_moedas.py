import requests
import csv
from datetime import datetime
import time

# API pública e gratuita para cotação de moedas em tempo real
URL_API = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

def buscar_cotacoes():
    try:
        resposta = requests.get(URL_API)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            # Extraindo informações do Dólar e do Euro
            dolar = dados['USDBRL']['bid']
            euro = dados['EURBRL']['bid']
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print("========================================")
            print(f" COTAÇÃO EM TEMPO REAL ({data_hora})")
            print("========================================")
            print(f"💵 Dólar (USD): R$ {float(dolar):.2f}")
            print(f"💶 Euro (EUR) : R$ {float(euro):.2f}")
            print("========================================")
            
            # Salva o histórico no arquivo CSV
            salvar_historico(data_hora, dolar, euro)
        else:
            print(f"Erro na conexão com a API: {resposta.status_code}")
            
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def salvar_historico(data_hora, dolar, euro):
    arquivo_existe = True
    
    # Verifica se o arquivo já existe para não repetir o cabeçalho
    try:
        with open('historico_moedas.csv', 'r') as f:
            pass
    except FileNotFoundError:
        arquivo_existe = False

    with open('historico_moedas.csv', mode='a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        
        if not arquivo_existe:
            escritor.writerow(['DataHora', 'Dolar_BRL', 'Euro_BRL'])
            
        escritor.writerow([data_hora, dolar, euro])
        print("✓ Cotações salvas em 'historico_moedas.csv'!\n")

if __name__ == "__main__":
    print("🚀 Monitor de moedas iniciado! (Pressione Ctrl + C para parar)\n")
    while True:
        buscar_cotacoes()
        # Espera 30 segundos antes de buscar novamente
        time.sleep(30)

