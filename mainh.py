import requests

# URL do webhook do Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/1345154913939755028/4zqGCotnTDuZa5eBMAnimEuJYZTqTGjcIyrCkvvmC862M4D3bfv0wE048bbFMn4PQ2y3"

def enviar_mensagem(mensagem):
    data = {"content": mensagem}
    headers = {"Content-Type": "application/json"}
    print(f"Enviando mensagem: {mensagem}")  # Verificar a mensagem antes de enviar
    response = requests.post(WEBHOOK_URL, json=data, headers=headers)
    
    if response.status_code in [200, 204]:
        print(f"Mensagem enviada: {mensagem}")
    else:
        print(f"Erro ao enviar mensagem: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("Digite suas mensagens para o webhook do Discord. Digite 'sair' para encerrar.")
    
    while True:
        mensagem = input("Você: ")  # Solicitação para digitar a mensagem
        if not mensagem:
            print("Por favor, digite uma mensagem!")  # Caso o usuário não digite nada
        if mensagem.lower() == "sair":
            print("Encerrando...")
            break
        enviar_mensagem(mensagem)
