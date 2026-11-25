import random
while True
sifre=[]
karakterler = ['+', '-', '/', '*', '!', '&', '$', '#', '?', '=', '@', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '0']
soru=input('otomatik olarak bir sifre olusturmak istiyormusun')
if soru =='evet':
    for i in range(10):
        randomkarakter=random.choice(karakterler)
        sifre.append(randomkarakter)
    print(sifre)
else:
    print('tamam sonra gorusuruz')
