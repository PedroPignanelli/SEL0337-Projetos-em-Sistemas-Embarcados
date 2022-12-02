# -------------------------------------------
# Codigo Pratica 5 - Interrupcoes e Threading
# -------------------------------------------
# Pedro Pignanelli e Mateus Darini
# -------------------------------------------

# Importacao das bibliotecas necessarias
import threading as thread
import RPi.GPIO as GPIO
import time

# Definicao como variavel dos pinos I/O utilizados
botao = 21
led = 20

# Variaveis utilizadas para logica e funcoes do codigo
global pisca
global freq
pisca = True
freq = 4

# Definicao da funcao a ser executada quando o botao e pressionado (sinal de input)
def funcao_botao(channel):
		global freq
		if GPIO.input(botao):   # Se houver input o parametro de frequencia e 1
			print("Interrupcao realizada!")
			freq = 1
		else:                   # Se NAO houver input o parametro de frequencia e 2
			freq = 2

def timer_callback():
	global pisca
	pisca = False
    print("Fim da contagem!")

# Configuracao da rotina de atendimento a interrupcao (sinal de input no botao)
GPIO.setmode(GPIO.BCM)
GPIO.setup(botao, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(botao, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.add_event_detect(botao, GPIO.BOTH, callback=funcao_botao, bouncetime=100)

# Funcionamento do timer de contagem
S = thread.Timer(20.0, timer_callback)
S.start()
print("Inicio da contagem!")

# Faz o LED ficar piscando com uma frequencia que depende da existencia de uma interupcao
while pisca:
	GPIO.output(led, GPIO.HIGH)
	time.sleep(freq)
	GPIO.output(led, GPIO.LOW)
	time.sleep(freq)
	print(freq)

GPIO.cleanup()