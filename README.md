# SEL0337-Projetos-em-Sistemas-Embarcados
Repositório com trabalhos da disciplina SEL0337 - Projetos em Sistemas Embarcados, EESC/USP.

# Prática 6 - Introdução a interfaces de visão computacional, sistemas de versionamento de arquivos e APIs públicas.
Nesta prática foi desenvolvido um programa básico em Python a ser executado em uma Raspberry Pi 3B+.

O desenvolvimento programa teve por objetivo introduzir os alunos a interface com a câmera da Raspberry utilizada, a utilização de APIs públicas (no caso um banco de dados climáticos) e sistemas de versionamento de arquivos - como o GitHub.
Foram utilizadas várias funções e bibliotecas para trabalhar com as APIs.

Dentre as bibliotecas, pode-se citar a biblioteca 'requests', que permite o envio de solicitações HTTP em Python. Já a biblioteca 'picamera' foi utilizada para permitir o uso do módulo de câmera da Raspberry. Por fim, também foram utilizadas as bibliotecas 'json' e 'pprint', que respectivamente tem a função de permitir a organização das estruturas de dados de forma mais fácil e imprimir os dados de forma ordenada no terminal.

No que tange a aplicação das funções, para obter os dados climáticos foi utilizada a função 'get', da biblioteca 'requests', junto com o link da página de dados. Já para o cntrole da câmera foram utilizadas funções da biblioteca 'picamera' como 'start_preview', 'stop_preview', 'capture', 'start_recording' e 'stop_recording', que permitem mostrar na tela conectada ao HDMI da Raspberry a imagem atuamente sendo capturada pela câmera, tirar uma fotografia e fazer um vídeo.

A foto e vídeo capturados estão disponíveis neste repositório.
