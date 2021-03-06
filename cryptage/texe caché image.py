from math import *
from PIL.Image import *


img=open("perenoel.bmp")

def traiteimg(img,textebin):
    chrono=0
    (l,h)=img.size
    for y in range (h):
        for x in range (l):
            p=list(img.getpixel((x,y)))

            p,chrono=traitepixel(p,chrono,textebin)
            
            nouvcoul=tuple(p)
            img.putpixel((x,y),nouvcoul)
            if chrono==len(textebin):
                return img
         
            
            
def traitepixel(p,chrono,textebin):
    for i in range(3):
        if textebin[chrono]=='0':
            while not(p[i]/2==int(p[i]/2)):
                p[i]-=1
        else:
            while p[i]/2==int(p[i]/2):
                p[i]+=1
        chrono+=1
        if chrono==len(textebin):
            return p,chrono
    return p,chrono



def traitexte(texte):
    textebin=[] 
    for lettre in texte:
        d=format(ord(lettre),'08b')
        for bina in d:
            textebin.append(bina)
    return textebin

def invtraiteimg(p,invtextebin,chrono):
    for i in range(3):
        if p[i]/2==int(p[i]/2):
            invtextebin.append(0)
        else:
            invtextebin.append(1)
        chrono+=1
        if chrono==32:
            return invtextebin,chrono
    return invtextebin,chrono


def recuptexte(img):
    chrono=0
    invtextebin=[]
    (l,h)=img.size
    for y in range (h):
        for x in range (l):
            p=list(img.getpixel((x,y)))
            invtextebin,chrono=invtraiteimg(p,invtextebin,chrono)
            if chrono==32:
                return invtextebin
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
