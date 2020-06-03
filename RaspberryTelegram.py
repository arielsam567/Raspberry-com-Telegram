#@reboot python /home/pi/Desktop/FaceDetectionVideo/faceDetection.py &
import cv2
import telepot
import time
import datetime

video = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('HaarCascade/haarcascade-frontalface-default.xml')
chat_id = 999999999 #coloque o seu chat_id
tokenAccess = '1010101010:353535353535353533535353535' #coloque o seu tokenAccess

# Tutorial de como criar o bot no Telegram 
# E pegar o chat_id
# E o tokenAccess
# https://www.filipeflop.com/blog/telegram-bot-com-raspberry-pi-3/


# Comandos que podem ser ultilizados
# On                 - Aciona o detector de faces
# Off                - Desliga o detector de faces
# Foto               - Recebe uma foto da camera
# Delay:(numero)     - Altera o valor de tempoDeEspera
# Help               - Retorna os comandos que podem ser utilizados 



tempoDeEspera = 10 #Segunos    
tempoUltimo= 0   
validador = 0


def handle(msg):
    global validador 
    global tempoDeEspera
    hat_id = msg['chat']['id']
    command = msg['text']
    print ('Recebeu o comando: %s' % command)
    

    
    if command.upper() == 'ON':
        validador = 1
        message = "Alarme Ligado"
        bot.sendMessage (chat_id, message)
    if (command.upper() =='OFF'):
        validador = 0
        message = "Alarme Desligado"
        bot.sendMessage (chat_id, message)
    if command.upper() =='FOTO':
        tiraFoto()
    if command[0:6].upper() == "DELAY:":
        tempoDeEspera = int(command[6:])
        message = "O delay atual e de " + command[6:] + " segundos"
        bot.sendMessage (chat_id, message)
    if command[0:7].upper() == "DELAY: " :
        tempoDeEspera = int(command[7:])
        message = "O delay atual e de " + command[7:] + " segundos"
        bot.sendMessage (chat_id, message)
    if command.upper() == "HELP":
         message = "On           -  Ligar o detector" + "\nOff          -  Desligar o detector"+ "\nFoto        -  Receber uma foto atual "+ "\nDelay: n  - Alterar o tempo entre as fotos"
         bot.sendMessage (chat_id, message)

    
def tiraFoto():
        _,frame = video.read()
        frame = cv2.flip(frame, 0)
        cv2.imwrite("Capture.jpg", frame)
        print("enviando....")
        bot.sendPhoto(chat_id=chat_id, photo=open('./Capture.jpg', 'rb'))
        print("enviado")


def verificaFace():
    global tempoUltimo
    _,frame = video.read()
    frame = cv2.flip(frame, 0)
    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    deteccoes = classificador.detectMultiScale(imagemCinza, scaleFactor=1.3, minNeighbors=9)
    for (x, y, l, a) in deteccoes:
        tempoUltimo = time.time()
        cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)
        cv2.putText(frame, 'INTRUSO',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        cv2.imwrite("Capture.jpg", frame)
        print("enviando....")
        bot.sendPhoto(chat_id=chat_id, photo=open('./Capture.jpg', 'rb'))
        print("enviado")
        nowa = datetime.datetime.now()
        message = "Face Detectada as "+ str(nowa.hour) + ":" + str(nowa.minute) + ":" + str(nowa.second)
        bot.sendMessage (chat_id, message)

def loop():
    while True:
        if validador == 1 and (time.time() - tempoUltimo) > tempoDeEspera:#
            verificaFace()

bot = telepot.Bot(tokenAccess)	
print('Esperando Comando...')
bot.message_loop(handle)	

message = "RASPBERRY ATIVO"
bot.sendMessage (chat_id, message)
loop()


