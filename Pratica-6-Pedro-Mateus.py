# -------------------------------------------
# Codigo Pratica 6 - Visao computacional, API, Git
# -------------------------------------------
# Pedro Pignanelli e Mateus Darini
# -------------------------------------------

# Importacao das bibliotecas necessarias
from requests import get
import json
from pprint import pprint
from picamera import PiCamera, Color
import time

# Obtencao do link para o 'banco de dados'
url = 'https://apex.oracle.com/pls/apex/raspberrypi/urlstation/getlatestmeasurements/'  # URL do banco de dados das medidas climaticas
estacao = 966583       # ID estacao mais proxima

url = url + str(estacao)
dados = get(url).json()['items']    # Funcao que de fato importa os dados

# Imprime os dados climaticos obtidos formatados como itens no terminal
pprint(dados)

# Funcao para tirar uma foto com a camera da Rasp
camera = PiCamera()
camera.rotation = 180
camera.framerate = 15

# Inicia um preview da imagem - mostra no monitor
camera.start_preview(alpha=250)

# Muda algumas configuracoes da camera
camera.brightness = 50  # Muda brilho
camera.image_effect  = 'colorswap' # Inverte cores - nao foi aplicado no video apresentado 

# Sobrescreve o nUSP dos alunos na imagem e altera o tamanho da fonte
camera.annotate_text = "11800733-10311090"
camera.annotate_text_size = 100

# Espera por 3seg e encerra o preview da imagem
time.sleep(3)
camera.stop_preview()

# Tira a foto e salva na pasta indicada como argumento em formato .jpg
camera.capture("/home/sel/sel0337/Pedro-Mateus/Pratica 6/foto.jpg")

# Grava um video e salva na pasta indicada como argumento em formato .h264
camera.start_recording("/home/sel/sel0337/Pedro-Mateus/Pratica 6/video.h264")
time.sleep(3)   # Continua gravando por 3seg
camera.stop_recording()     # Para a gravacao

# Espera por 5seg para dar tempo de salvar o video
time.sleep(5)
