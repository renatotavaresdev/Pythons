from captcha.image import ImageCaptcha
import random
import string
import os

from pyglet import image


#Função para gerar um texto aleatório
def gerar_texto_captcha(tamanho=5):
    caracteres = string.ascii_uppercase + string.digits #Letras Maiúsculas e Números
    return ''.join(random.choices(caracteres, k=tamanho))

#Função para Criar e Salvar a Imagem do CAPTCHA
def gerar_captcha(texto):
    image = ImageCaptcha(width=280, height=90)
    caminho_arquivo = "captcha.png"
    image.write(texto, caminho_arquivo)
    return caminho_arquivo

#Gerar texto do Captcha
texto_captcha = gerar_texto_captcha()

#Criar imagem do Captcha
caminho_captcha = gerar_captcha(texto_captcha)

#Exibir imagem do Captcha
os.system(f"start {caminho_captcha}")

#Solicitar entrada do usuário
resposta = input("Digite o texto do Captcha: ")

#Verificar se está correto
if resposta.upper() == texto_captcha:
    print("CAPTCHA correto!")
else:
    print("CAPTCHA incorreto!, Tente novamente")
