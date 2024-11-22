from PIL import Image

im = Image.open('image//animee.jpg')  #chargement image
pix = im.load() #création tableau de pixels

n=0
m=0

largeur = im.size[0] #récupération des dimensions
hauteur = im.size[1] # de l'image

print (largeur)
print (hauteur)
fichier = open("imageNB3.txt", "a")
L = ['$','@','B','%','8','&','W','M','#','*','o','a','h','k','b','d','p','q','w','m','Z','O','0','Q','L','C','J','U','Y','X','z','c','v','u','n','x','r','j','f','t','/','|','(',')','1','{','}','[',']','?','-','_','+','~','<','>','i','l','I',';',':',',','^','.']        

for _ in range(hauteur//3):
    for _ in range (largeur//2):
        pixel_test=pix[n,m]+pix[n+1,m]+pix[n,m-1]+pix[n+1,m-1]+pix[n, m-2]+pix[n+1,m-2]
        r=(pixel_test[0]+pixel_test[3]+pixel_test[6]+pixel_test[9]+pixel_test[12]+pixel_test[15])/6 #moyenne de rouge dans le pixel
        v=(pixel_test[1]+pixel_test[4]+pixel_test[7]+pixel_test[10]+pixel_test[13]+pixel_test[16])/6#moyenne de vert dans le pixel
        b=(pixel_test[2]+pixel_test[5]+pixel_test[8]+pixel_test[11]+pixel_test[14]+pixel_test[17])/6#moyenne de bleu dans le pixel
        rvb= (r+v+b)/3 #moyenne des 3 couleurs pour faire des images en couleurs
        l = int(((255/64)*rvb*4)//64)#pour trouvé quel signe dans la liste
        fichier.write(L[l])
        n+=2
    n=0
    m+=3
    fichier.write("\n")
fichier.close()
print("fini")
