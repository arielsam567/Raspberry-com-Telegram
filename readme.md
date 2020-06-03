# Raspberry com Telegram
Este projeto foi feito para a matéria PRÁTICA NA FÁBRICA EXPERIMENTAL DE SOFTWARE IV. Utilizou-se um Raspberry Pi 3 modelo B, juntamente com uma câmera. O SO utilizado foi o Noobs.

Tutorial de como criar o bot no Telegram, pegar o chat_id e o tokenAccess
https://www.filipeflop.com/blog/telegram-bot-com-raspberry-pi-3/

Comandos que podem ser ultilizados
On                 - Aciona o detector de faces
Off                - Desliga o detector de faces
Foto               - Recebe uma foto da camera
Delay:(numero)     - Altera o valor de tempoDeEspera
Help               - Retorna os comandos que podem ser utilizados 

Bibliotecas utilizadas: `OpenCV` e `Telepot'

Script necessário para baixar as dependências no Raspberry

`sudo apt-get update`

`sudo apt-get -y install python-pip`

`sudo apt-get -y install python-git `

`sudo apt-get -y install python-numpy `

`sudo apt-get -y install python-scipy `

`sudo apt-get -y install python-opencv `

`sudo pip install --upgrade cython`

`sudo pip install -U scikit-learn` 

`sudo pip install imutil`

`sudo apt-get -y install python-sklearn`

`sudo apt-get -y install python-skimage`  

`sudo pip3 install telepot`

`git clone https://github.com/nickoala/telepot.git`
