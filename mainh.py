import requests

# Título estilizado
titulo = """
$$$$$$$\  $$$$$$$\   $$$$$$\  $$\      $$\       $$$$$$$\  $$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |      $$  __$$\ \_$$  _|$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  \__|$$ |  $$ |$$ /  $$ |$$$$\  $$$$ |      $$ |  $$ |  $$ |  $$ /  \__|$$ /  \__|$$ /  $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$\  $$$$$$$  |$$$$$$$$ |$$\$$\$$ $$ |      $$ |  $$ |  $$ |  \$$$$$$\  $$ |      $$ |  $$ |$$$$$$$  |$$ |  $$ |
 \____$$\ $$  ____/ $$  __$$ |$$ \$$$  $$ |      $$ |  $$ |  $$ |   \____$$\ $$ |      $$ |  $$ |$$  __$$< $$ |  $$ |
$$\   $$ |$$ |      $$ |  $$ |$$ |\$  /$$ |      $$ |  $$ |  $$ |  $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$  |$$ |      $$ |  $$ |$$ | \_/ $$ |      $$$$$$$  |$$$$$$\ \$$$$$$  |\$$$$$$  | $$$$$$  |$$ |  $$ |$$$$$$$  |
 \______/ \__|      \__|  \__|\__|     \__|      \_______/ \______| \______/  \______/  \______/ \__|  \__|\_______/ 
"""

# Função para enviar a mensagem
def enviar_mensagem(webhook_url, mensagem):
    data = {"content": mensagem}
    headers = {"Content-Type": "application/json"}
    print(f"Enviando mensagem: {mensagem}")  # Verificar a mensagem antes de enviar
    response = requests.post(webhook_url, json=data, headers=headers)
    
    if response.status_code in [200, 204]:
        print(f"Mensagem enviada: {mensagem}")
    else:
        print(f"Erro ao enviar mensagem: {response.status_code} - {response.text}")

# Exibe o título
print(titulo)

# Solicita o webhook do usuário
webhook_url = input("Digite o webhook do Discord: ")

# Loop para enviar mensagens
if __name__ == "__main__":
    print("Digite suas mensagens para o webhook do Discord. Digite 'sair' para encerrar.")
    
    while True:
        mensagem = input("Você: ")  # Solicitação para digitar a mensagem
        if not mensagem:
            print("Por favor, digite uma mensagem!")  # Caso o usuário não digite nada
        if mensagem.lower() == "sair":
            print("Encerrando...")
            break
        enviar_mensagem(webhook_url, mensagem)
