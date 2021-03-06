i = open("texte.txt", 'r')
i = i.read()

def parcour(i):
    (l, h) = i.size
    for y in range (h):
        for x in range (l):
            p = i.getpixel((x,y))
            return p
            
def paire():
    a = []
    for i in range (0,3):
        if p[i]/2 == type(float):
            a.append(1)
        else:
            a.append(0)
        return a
            
def decode():
    for a in range:
        fait en sorte de 8 -8 puis converti en bin,
        puis arret ala fonction avec le message secret
        
        
                    