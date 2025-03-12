import requests
import threading
import time

# Configurações
url = "https://cebacentroeducacional.com.br/"  # Substitua pelo URL do seu site
num_requests = 100  # Número total de requisições
interval = 0.1  # Intervalo entre requisições (em segundos)
timeout = 10  # Timeout para cada requisição (em segundos)

# Headers para simular um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Função para enviar uma requisição
def send_request():
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        print(f"Status Code: {response.status_code}")  # Mostra o código de status da resposta
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")

# Criando e iniciando as threads para enviar requisições simultaneamente
threads = []
for i in range(num_requests):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()
    time.sleep(interval)  # Intervalo entre as requisições

# Aguardando todas as threads terminarem
for thread in threads:
    thread.join()

print("Teste concluído!")
