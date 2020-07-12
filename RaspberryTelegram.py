#@reboot python /home/pi/Desktop/FaceDetectionVideo/faceDetection.py &
import cv2
import numpy as np
import telepot
import time
import datetime

largura_min=30 
altura_min=30 
largura_max=90 
altura_max=90 
video = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('HaarCascade/haarcascade-frontalface-default.xml')
chat_id = 999999999 #coloque o seu chat_id
tokenAccess = '1010101010:353535353535353533535353535' #coloque o seu tokenAccess
tempoDeEspera = 10 #Segunos    
tempoUltimo= 0   
validador = 0
detec = []
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

# Tutorial de como criar o bot no Telegram 
# E pegar o chat_id
# E o tokenAccess
# https://www.filipeflop.com/blog/telegram-bot-com-raspberry-pi-3/

# Comandos que podem ser ultilizados
# On                 - Aciona o detector de Movimento
# On:2               - Aciona o detector de faces
# Off                - Desliga o detector de faces
# Config             - Retorna os valores configurados
# Foto               - Recebe uma foto da camera
# Delay: n           - Altera o valor de tempoDeEspera
# Altura_max: n      - Altera o valor de altura_max
# Altura_min: n      - Altera o valor de altura_min
# Largura_max: n     - Altera o valor de largura_max
# Largura_min: n     - Altera o valor de largura_min
# Help               - Retorna os comandos que podem ser utilizados 




def handle(msg):
    global validador 
    global tempoDeEspera
    global altura_max
    global altura_min
    global largura_max
    global largura_min
    hat_id = msg['chat']['id']
    command = msg['text']
    print ('Recebeu o comando: %s' % command)
    

    
    if command.upper() == 'ON:1':
        validador = 1
        message = "Alarme Ligado - Deteccao Facial"
        bot.sendMessage (chat_id, message)
    if command.upper() == 'ON':
        validador = 2
        message = "Alarme Ligado - Deteccao de Movimento"
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
    if command[0:12].upper() == "LARGURA_MIN:" :
        largura_min = int(command[12:])
        message = "A largura minima atual sao " + command[12:] + " pixels"
        bot.sendMessage (chat_id, message)
    if command[0:12].upper() == "LARGURA_MAX:" :
        largura_max = int(command[12:])
        message = "A largura maxima atual sao " + command[12:] + " pixels"
        bot.sendMessage (chat_id, message)
    if command[0:11].upper() == "ALTURA_MIN:" :
        altura_min = int(command[11:])
        message = "A altura minima atual sao " + command[11:] + " pixels"
        bot.sendMessage (chat_id, message)
    if command[0:11].upper() == "ALTURA_MAX:" :
        altura_max = int(command[11:])
        message = "A altura maxima atual sao " + command[11:] + " pixels"
        bot.sendMessage (chat_id, message)
    if command.upper() == "HELP":
         message = "On           -  Ligar o detector de Movimento" +"\nOn:1         -  Ligar o detector de Face" + "\nOff          -  Desligar o detector"+ "\nConfig    - Retorna os valores configurados"+ "\nFoto        -  Receber uma foto atual "+ "\nDelay: n  - Alterar o tempo entre as fotos" +"\n\nAltura_max: n      - Altera a altura maxima de pixels para a deteccao"+"\n\nAltura_min: n      - Altera a altura minima de pixels para a deteccao"+"\n\nLargura_max: n     - Altera a largura maxima de pixels para a deteccao"+"\n\nLargura_min: n     - Altera a largura minima de pixels para a deteccao"
         bot.sendMessage (chat_id, message)
    if command.upper() == "CONFIG":
         message = "Largura maxima:" + str(largura_max) + "\nAltura maxima:" + str(altura_max)+ "\nLargura minima:" + str(largura_min)+  "\nAltura minima:" + str(altura_min)
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
    global contador
    _,frame = video.read()
    frame = cv2.flip(frame, 0)
    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    deteccoes = classificador.detectMultiScale(imagemCinza, scaleFactor=1.3, minNeighbors=3,minSize=(60,60))
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
  

	
def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

def verificaMovimentacao():
    global tempoUltimo
    global altura_max
    global altura_min
    global largura_max
    global largura_min
    _,frame= video.read()
    frame = cv2.flip(frame, 0)
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(1,1),0)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((15,15)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    
    _,contorno,h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for(i,c) in enumerate(contorno):
        (x,y,w,h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min) and (w<=largura_max) and (h<=altura_max)
        if not validar_contorno:
            continue

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)        
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame, centro, 4, (0, 0,255), -1)

        for (x,y) in detec:
            tempoUltimo = time.time()
            #cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)
            cv2.putText(frame, 'INTRUSO',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
            cv2.imwrite("Capture.jpg", frame)
            print("enviando....")
            bot.sendPhoto(chat_id=chat_id, photo=open('./Capture.jpg', 'rb'))
            print("enviado")
            nowa = datetime.datetime.now()
            message = "Movimento Detectado as "+ str(nowa.hour) + ":" + str(nowa.minute) + ":" + str(nowa.second)
            bot.sendMessage (chat_id, message)       
    
  
  
def loop():
    
    while True:
        _,frame = video.read()
        if validador == 1 and (time.time() - tempoUltimo) > tempoDeEspera:#
            verificaFace()
        if validador == 2 and (time.time() - tempoUltimo) > tempoDeEspera:#
            verificaMovimentacao()

bot = telepot.Bot(tokenAccess)	
print('Esperando Comando...')
bot.message_loop(handle)	
message = "RASPBERRY BRANCO ATIVO"
bot.sendMessage (chat_id, message)

loop()


