import requests
import os
import shutil

# Função para centralizar o texto
def centralizar_texto(texto):
    # Pega a largura do terminal
    largura_terminal = shutil.get_terminal_size().columns
    # Centraliza o texto calculando a posição correta
    return texto.center(largura_terminal)

# Função para colorir o texto de azul
def colorir_texto_azul(texto):
    return f"\033[34m{texto}\033[0m"  # Código ANSI para azul

# Título estilizado
titulo = """
 __    __    ___    ___  ____   __ __   ___    ___   __  _ 
|  |__|  |  /  _]  /  _]|    \ |  |  | /   \  /   \ |  |/ ] 
|  |  |  | /  [_  /  [_ |  o  )|  |  ||     ||     ||  ' /  
|  |  |  ||    _]|    _]|     ||  _  ||  O  ||  O  ||    \  
|  `  '  ||   [_ |   [_ |  O  ||  |  ||     ||     ||     | 
 \      / |     ||     ||     ||  |  ||     ||     ||  .  | 
  \_/\_/  |_____||_____||_____||__|__| \___/  \___/ |__|\_| 
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

# Exibe o título centralizado e em azul
print(colorir_texto_azul(centralizar_texto(titulo)))

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
