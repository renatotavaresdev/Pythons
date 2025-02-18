import tkinter as tk
import requests


# Função para obter a previsão do tempo
def obter_previsao():
    cidade = entrada_cidade.get()
    chave_api = 'd4c8958676aa20fddab588dd581af522'  # Substitua pela sua chave de API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        resultado = f'Temperatura: {temperatura}°C\nDescrição: {descricao}'
    else:
        resultado = 'Cidade não encontrada!'

    label_resultado.config(text=resultado)


# Configuração da interface gráfica
janela = tk.Tk()
janela.title('Previsão do Tempo')

# Entrada para a cidade
label_cidade = tk.Label(janela, text='Digite o nome da cidade:')
label_cidade.pack()

entrada_cidade = tk.Entry(janela)
entrada_cidade.pack()

# Botão para obter a previsão
botao = tk.Button(janela, text='Obter Previsão', command=obter_previsao)
botao.pack()

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text='')
label_resultado.pack()

# Iniciar o loop da interface
janela.mainloop()