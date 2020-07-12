# Raspberry com Telegram
Este projeto foi feito para a matéria Prática na Fábrica Experimental De Software IV. Utilizou-se um Raspberry Pi 3 modelo B, juntamente com uma câmera. O SO utilizado foi o Noobs.

[Tutorial de como criar o bot no Telegram](https://www.filipeflop.com/blog/telegram-bot-com-raspberry-pi-3/), pegar o chat_id e o tokenAccess


## Comandos que podem ser ultilizados
- On                 - Aciona o detector de movimento
- On:2               - Aciona o detector de faces
- Off                - Desliga o detector de faces
- Config             - Retorna os valores configurados
- Foto               - Recebe uma foto da camera
- Delay: n           - Altera o valor de tempoDeEspera
- Altura_max: n      - Altera o valor de altura_max
- Altura_min: n      - Altera o valor de altura_min
- Largura_max: n     - Altera o valor de largura_max
- Largura_min: n     - Altera o valor de largura_min
- Help               - Retorna os comandos que podem ser utilizados 

Bibliotecas utilizadas: `OpenCV` e `Telepot`

**Script necessário para baixar as dependências no Raspberry**
```
sudo apt-get update
sudo apt-get -y install python-pip
sudo apt-get -y install python-git 
sudo apt-get -y install python-numpy 
sudo apt-get -y install python-scipy 
sudo apt-get -y install python-opencv 
sudo pip install telepot
```
