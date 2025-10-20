from datetime import datetime

# 1. Obter a hora atual
agora = datetime.now()
hora_atual = agora.strftime("%H:%M:%S") # Formata a hora como HH:MM:SS

# 2. Definir a mensagem de saudação baseada na hora
hora = agora.hour

if 5 <= hora < 12:
    saudacao = "Bom dia"
elif 12 <= hora < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# 3. Exibir a saudação completa com a hora atual
print(f"{saudacao}! Agora são: {hora_atual}") 