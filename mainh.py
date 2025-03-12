import requests
import threading

# URL do site que você deseja testar
url = "https://cebacentroeducacional.com.br/ensino-medio/uso-de-celular-por-alunos-pode-ser-proibido-em-escolas-municipais-do-rio/#"

# Número de requisições que você deseja enviar
num_requests = 100

# Função para enviar uma requisição
def send_request():
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")  # Mostra o código de status da resposta
    except Exception as e:
        print(f"Erro: {e}")

# Criando e iniciando as threads para enviar requisições simultaneamente
threads = []
for i in range(num_requests):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

# Aguardando todas as threads terminarem
for thread in threads:
    thread.join()

print("Teste concluído!")
