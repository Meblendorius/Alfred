import pyautogui
import time
cont=0
xpos= []
ypos= []
clicks=int(input("Quantidade de Clicks desejados: "))
tempo=int(input("Intervalo de segundos entre os cliques"))
while cont != clicks:
    input("Aperte Enter para marcar o click")
    x,y = pyautogui.position()
    xpos.append(x)
    ypos.append(y)
    print ("x = "+str(xpos[cont])+" y = "+str(ypos[cont]))
    cont = cont + 1
input("começar")
for i in range(len(xpos)):
    pyautogui.click(xpos[i],ypos[i])
    print("aguardando")
    time.sleep(tempo)













