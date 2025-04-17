import random

def game():
    print('start game ')
    secor = random.randint(1, 100)
    with open("text.txt") as file:
       hisceor = file.read()
       if(hisceor !=''):
          hisceor = int(hisceor)
       else:
          hisceor= 0

    print(f'sceor {secor}')
    if(secor>hisceor):
       with open("text.txt" , "w") as file:
          file.write(str(secor))
    return secor
          
game()