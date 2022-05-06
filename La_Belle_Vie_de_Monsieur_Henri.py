from random import *
from math import  *
from tkinter import *
import time
import os

def B22(t): #Vestige du boutton numéro deux, fonction pour placer les premiérs éléments du jeu.
        global IMage, X, Y, mapa
        if t == 0:
                mapa=2
        CanvasAcceuil.place_forget()
        ZoneDess.place(x=00,y=00)
        QQ=testMapa(mapa)
        traceImage(ZoneDess,QQ,0,0,'deux')
        PlacePika(X,Y)

####### Fonction Déplacement ########

def testMapa(m):
        if m ==1:
                return (Carte1)
        if m ==2:
                return (Carte2)
        if m ==3:
                return (Carte3)
        if m ==4:
                return (Carte4)


def BDD(event):#Fonction qui gère le déplacement à droite
        global X, Y, inverse
        inverse=1
        for i in range (3):
                testeMove(X,Y)
                X=X+deplacementD
                PlacePika(X,Y)
        testeTel(X,Y)


def BGG(event):#Fonction qui gère le déplacement à gauche
        global X, Y, inverse
        inverse=0
        for i in range (3):
                testeMove(X,Y)
                X=X-deplacementG
                PlacePika(X,Y)
        testeTel(X,Y)

def BHH(event):#Fonction qui gère le déplacement en haut
        global X, Y, inverse
        inverse=2
        for i in range (3):
                testeMove(X,Y)
                Y=Y-deplacementH
                PlacePika(X,Y)
        testeTel(X,Y)

def BBB(event):#Fonction qui gère le déplacement en bas
        global X, Y, inverse
        inverse=3
        for i in range (3):
                testeMove(X,Y)
                Y=Y+deplacementB
                PlacePika(X,Y)
        testeTel(X,Y)


###################################### Téléportation + Mouvement + Parlé


def testeTel(x,y):#Fonction teste téléportation
        global mapa
        if (mapa == 1 ):
                if(-150<=x<=-50) and (140<=y<=250) :
                        Tel(1030,y+20,Carte3,3,IMageR1)
        if (mapa == 3):
                if(345<x<450) and (40<y<80) :
                        Tel(510,470,Carte2,2,IMage1)
                if (1070<x<1300) and (170<y<250) :
                        Tel(-20,y-20,Carte1,1,IMage1)
                if (-150<x<-50) and (200<y<400) :
                        Tel(1030,y,Carte4,4,IMageR1)

        if (mapa == 2):
                if (500<x<566) and (450<y<700) :
                        Tel(385,115,Carte3,3,IMageB1)
        if (mapa == 4):
                if (1040<x<1200) and (200<y<400) :
                        Tel(0,y-30,Carte3,3,IMageB1)




def Tel(x,y,M,m,image):#Fonction téléportation
        global X, Y, mape, mapa, victoires
        X=x
        Y=y
        mapa = m
        mape = M

        delete('un')
        ZoneDess.delete(ALL)
        traceImage(ZoneDess,mape,0,0,'deux')
        traceImage(ZoneDess,image,X,Y,'un')

        if mapa == 3 :
                if victoires <3:
                        traceImage(ZoneDess,IChCarte3,0,250,'cheche')
        if mapa == 1 :
                if victoires <4:
                        traceImage(ZoneDess,ISuperman,410,40,'Sman')



def testeMove(x,y):#Fonction teste déplacement 
        global deplacementH, deplacementB, deplacementG, deplacementD, savedeplace, mapa
        if mapa == 1 :
                if(-100<=x<=360) and (0<=y<=172) or (390<=x<=700) and (0<=y<=80):
                        deplacementH=0

                if(-100<=x<=360) and (215<=y<=500) or (310<=x<=650) and (280<=y<=500):
                        deplacementB=0

                if(300<=x<=390) and (0<=y<=160)or (300<=x<=390) and (220<=y<=500):
                        deplacementG=0

                if(470<=x<=700) and (0<=y<=600):
                        deplacementD=0

                if(-100<=x<=350) and (155<=y<=205) or (305<=x<=470) and (90<=y<=285):
                        deplacementD=vitesse
                        deplacementG=vitesse
                        deplacementH=vitesse
                        deplacementB=vitesse

        if mapa == 3 :
                if (480<x<1600)and (0<y<180) or (-100<x<480) and (0<y<80) or (-100<x<320) and (240<y<260):
                        deplacementH=0

                if (480<x<1600) and (250<y<700) or (-100<x<600) and (305<y<700):
                        deplacementB=0

                if (305<x<320) and (0<y<240) or (0<x<125) :
                        deplacementG=0

                if(490<=x<=500) and (0<=y<=170) or (480<x<500) and (245<y<600) :
                        deplacementD=0

                if (victoires >= 3) and (450<x<1600) and (180<y<250) or (319<x<481) and(49<y<306) or (-100<x<400)and (260<y<315):
                        deplacementD=vitesse
                        deplacementG=vitesse
                        deplacementH=vitesse
                        deplacementB=vitesse

                if (victoires < 3) and (450<x<1600) and (180<y<250) or (319<x<481) and(49<y<306) or (125<x<400)and (260<y<315):
                        deplacementD=vitesse
                        deplacementG=vitesse
                        deplacementH=vitesse
                        deplacementB=vitesse

        if mapa == 2 :

                if (0<y<190) or (0<x<347) and (240<y<310) or (347<x<400) and (210<y<250) or (580<x<900) and (245<y<265) or (727<x<1100):
                        deplacementH=0

                if (0<x<525) and (415<y<513) or(565<x<1100) and (395<y<513):
                        deplacementB=0

                if (0<x<245) or (300<x<355) and (150<y<300)or (200<x<404) and (0<y<250) :
                        deplacementG=0

                if (845<x<1100) or (720<x<900) and (250<y<280)or (570<x<585) and (0<y<250):
                        deplacementD=0

                if (240<x<840) and (310<y<=415) or (350<x<728) and (260<y<360) or (403<x<570) and (190<y<410) or (525<=x<=565) and (390<y<480):
                        deplacementD=vitesse
                        deplacementG=vitesse
                        deplacementH=vitesse
                        deplacementB=vitesse
        if mapa == 4 :

                if (150<y<300) and (515<x<1200) or (0<y<120) :
                        deplacementH=0

                if (355<y<600):
                        deplacementB=0

                if (0<x<500):
                        deplacementG=0

                if (520<x<560) and (0<y<320):
                        deplacementD=0

                if (495<x<1100) and (325<y<=355) or (500<x<520) and (120<y<355):
                        deplacementD=vitesse
                        deplacementG=vitesse
                        deplacementH=vitesse
                        deplacementB=vitesse


def parler (event):#Fonction pour parler aux personnages
        global Ntexte, victoires
        a=Ntexte
        T=0.0
        Dialogue=""
        traceImage(ZoneDess,IBoxText,175,410,'textB')
        if mapa == 3 :
                if (0<X<175):
                        if victoires <3:
                                T=1.5
                                if a == 1 :
                                        Dialogue="ON NE PASSE PAS!!"
                                        Ntexte = 2
                                if a == 2 :
                                        Dialogue="ON NE PASSE PAS J'AI DIT!!"
                                        Ntexte = 3
                                if a == 3 :
                                        Dialogue="TU VEUX TE BATTRE ?"


        if mapa == 4:
                if (0<Y<160):
                        Dialogue = "Je te donne mon pouvoir"
                        T=3
                        ChuckPower()
                
        traceTexte(ZoneDess,Dialogue,525,517,"white","texte")
        ZoneDess.update()
        time.sleep(T)
        delete('texte')
        delete("textB")


def TestCombat (event):#Fonction pour tester les combats
        global Ntexte, Vieadv, NVieadv, Attaqueadv, victoires, CHvie, CHniveauV
        if mapa == 3 :
                if Ntexte==3:
                        if (0<X<175):
                                if victoires < 3:
                                        COMBAT(IChevalier,CHvie,CHniveauV,CHattaque)
                                        Vieadv = CHvie
                                        NVieadv = CHniveauV
                                        Attaqueadv = CHattaque
        if mapa == 1 :
                if (0<Y<125):
                        if victoires < 4:
                                COMBAT(I2Superman,100,100,40)
                                Vieadv = 100
                                NVieadv = 100
                                Attaqueadv = 40

def COMBAT (adversaire,Vadv,NVadv,Aadv):#Fonction pour combatre
        global vie, niveauV
        CanvasCombat.place(x=100,y=2)
        traceImage(CanvasCombat,ICombat,0,0,'un')
        traceImage(CanvasCombat,IGGCombat,150,255,'un')
        traceImage(CanvasCombat,adversaire,470,-40,'un')
        CanvasCombat.create_window(19+113,510, window=BAttaque ,tags= "texteC")
        CanvasCombat.create_window(260+113,510, window=BFuite ,tags= "texteC")
        CanvasCombat.create_window(500+113,510, window=BSac ,tags= "texteC")

        CanvasCombat.create_text(100,70,font="Arial 14 italic",text = "Vie de l'adversaire :")
        CanvasCombat.create_text(513,303,font="Arial 14 italic",text = "Vie de Henri :")

        traceVie(70,85,Vadv,NVadv,CanvasCombat)
        traceVie(487,321,vie,niveauV,CanvasCombat)
        CanvasCombat.update()


def traceVie(x0,y0,V,N,CANVAS):#Fonction pour tracer la vie dans le mode combat
        PdeVie=V/N
        PdeVie=PdeVie*200
        if PdeVie<0:
                PdeVie=0
        traceRect(x0-3,y0,x0+203,y0+25,CANVAS,"white","")
        traceRect(x0,y0+3,x0+PdeVie,y0+22,CANVAS,"red","")

def traceRect(x0,y0,x1,y1,CANVAS,color,T):#Fonction pour tracer des rectangles
        CANVAS.create_rectangle(x0,y0,x1,y1,fill=color,tags=T)



def ATTAQUE ():#Fonction pour l'attaque de notre personnage 
        global attaque, Vieadv, NVieadv, victoires, Attaqueadv
        traceGIF(CanvasCombat,"boom.gif",480,5,"Explo",15,0.03)
        Vieadv=Vieadv-attaque
        traceVie(70,85,Vieadv,NVieadv,CanvasCombat)
        if Vieadv<=0 :
                CanvasCombat.update()
                time.sleep(1)
                victoires=victoires+1
                TestDelet()
                FinCombat()

        if Vieadv>0 :
                CanvasCombat.update()
                time.sleep(1)
                TourAdv(Attaqueadv)

def TourAdv(A):#Fonction pour le tour adverse 
        global vie, niveauV, X, Y, mapa, morts
        traceGIF(CanvasCombat,"Sword.gif",40,100,"Explo",13,0.01)
        vie=vie-A
        traceVie(487,321,vie,niveauV,CanvasCombat)
        if vie <= 0:
                X=650
                Y=220
                mapa=2
                CanvasCombat.update()
                time.sleep(1)
                FinCombat()
                ZoneDess.delete(ALL)
                vie = niveauV
                morts = morts +1
                traceImage(ZoneDess,Carte2,0,0,'deux')
                traceImage(ZoneDess,IMage1,X,Y,'un')



def FinCombat():
        CanvasCombat.place_forget()

def TestDelet():
        global victoires
        if victoires >=3:
                delete('cheche')
        if victoires >=4:
                YouWin()



def SAC ():
        traceGIF(CanvasCombat,"Sacmm.gif",75,0,"sacmmm",1,1)

def FUITE ():
        CanvasCombat.place_forget()

def traceGIF(CANVAS,IMAGE,a,b,c,Nframe,T):#Fonction pour utiliser des GIF facilement
        I=0
        for i in range (Nframe):
                Frame= "gif -index " + str(I)
                GIF= PhotoImage(file=IMAGE, format=Frame)
                traceImage(CANVAS,GIF,a,b,c)
                time.sleep(T)
                CANVAS.update()
                I=I+1



########################

def PlacePika(a,b):#Vestige des premier test avec un pikachu, elle permet de placer le personnage
        global imageN, Vitesse2
        V=Vitesse2
        delete('un')
        if(inverse==1):
                if (imageN==1):
                        delete('un')
                        traceImage(ZoneDess,IMage1,a,b,'un')
                        time.sleep(V)

                if (imageN==2):
                        delete('un')
                        traceImage(ZoneDess,IMage2,a,b,'un')
                        time.sleep(V)
                if (imageN==3):
                        delete('un')
                        traceImage(ZoneDess,IMage3,a,b,'un')
                        time.sleep(V)
                        imageN=0
        if(inverse==0):
                if (imageN==1):
                        delete('un')
                        traceImage(ZoneDess,IMageR1,a,b,'un')
                        time.sleep(V)

                if (imageN==2):
                        delete('un')
                        traceImage(ZoneDess,IMageR2,a,b,'un')
                        time.sleep(V)
                if (imageN==3):
                        delete('un')
                        traceImage(ZoneDess,IMageR3,a,b,'un')
                        time.sleep(V)
                        imageN=0
        if(inverse==2):
                if (imageN==1):
                        delete('un')
                        traceImage(ZoneDess,IMageM1,a,b,'un')
                        time.sleep(V)

                if (imageN==2):
                        delete('un')
                        traceImage(ZoneDess,IMageM2,a,b,'un')
                        time.sleep(V)
                        imageN=0
        if(inverse==3):
                if (imageN==1):
                        delete('un')
                        traceImage(ZoneDess,IMageB1,a,b,'un')
                        time.sleep(V)

                if (imageN==2):
                        delete('un')
                        traceImage(ZoneDess,IMageB2,a,b,'un')
                        time.sleep(V)
                        imageN=0
        imageN=imageN+1

def traceImage(CANVAS,IMAGE,a,b,c):#Fonction pour les images
        CANVAS.create_image(a,b,image=IMAGE,anchor=NW, tags=c)
        CANVAS.update()


def delete(MonTag):
        ZoneDess.delete(ZoneDess.find_withtag(MonTag))


##################################### Stat + Option
def traceTexte(CANVAS,Texte,a,b,C,T):
        CANVAS.create_text(a,b,text=Texte, fill=C,font="arial 15",tags=T)
        CANVAS.update()


def MontreMenu (event):#Fonction charger d'afficher le menu grace à la touche échap
        global Menuefface, ataque, vie, niveauV, morts, victoire, vitesse, exp
        VIE = str(vie)+" / "+str(niveauV)
        Test=Menuefface
        if Test==0:
                Menuefface=1
                CanvasMenu.place(x=300,y=205)
                traceImage(CanvasMenu,IStat,190,0,"stat")
                traceTexte(CanvasMenu,VIE,288,24,"white","")
                traceTexte(CanvasMenu,attaque,438,24,"white","")

                traceTexte(CanvasMenu,vitesse,317,79,"white","")
                traceTexte(CanvasMenu,morts,317,108,"white","")
                traceTexte(CanvasMenu,victoires,317,136,"white","")
                CanvasMenu.create_window(100,35, window=Bsave ,tags= "")
                CanvasMenu.create_window(100,96, window=Bcharge ,tags= "")
                CanvasMenu.create_window(100,160, window=Bquite ,tags= "")
        if Test==1:
                Menuefface=0
                CanvasMenu.place_forget()




def  tuch (evt)  :
        a=evt.x
        b=evt.y
        testClick (a,b)


def testClick (a,b):#Fonction de l'aceuil 
        global mapa
        if mapa == 0 :
                if (401<a<707) and (345<b<395):
                        B22(0)
                if (450<a<657) and (404<b<453):
                        Continue()
                if (468<a<634) and (463<b<511):
                        Ferme()



def Sauvegarde ():
        global attaque, vie, niveauV, morts, victoires, vitesse, exp, X, Y, mapa
        FichierSauvgarde=""
        a=str(attaque)
        b=str(vie)
        c=str(niveauV)
        d=str(morts)
        e=str(victoires)
        f=str(vitesse)
        g=str(exp)
        h=str(X)
        i=str(Y)
        j=str(mapa)
        FichierSauvgarde= a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j
        f= open("fichier.txt","w")
        f.write(FichierSauvgarde)
        f.close()
        


def Continue():
        global attaque, vie, niveauV, morts, victoires, vitesse, exp, X, Y, mapa, imageN
        fichier = open( "fichier.txt", "r")
        S=fichier.readlines()
        for z in range (len(S)):
                S[z-1]=int(S[z-1].replace("\n",""))

        attaque=S[0]
        vie=S[1]
        niveauV=S[2]
        morts=S[3]
        victoires=S[4]
        vitesse=S[5]
        exp=S[6]
        X=S[7]
        Y=S[8]
        mapa=S[9]

        fichier.close()
        CanvasAcceuil.place_forget()
        B22(1)
        CanvasMenu.place_forget()
        imageN=1
        if mapa == 3 :
                if victoires <3:
                        traceImage(ZoneDess,IChCarte3,0,250,'cheche')
        if mapa == 1 :
                if victoires <4:
                        traceImage(ZoneDess,ISuperman,410,40,'cheche')





def Ferme ():
        fenPrincip.destroy()

def ChuckPower():
        global Vitesse2, vie, attaque, niveauV
        Vitesse2=0.01
        vie = 100
        attaque = 50
        niveauV = 100

def YouWin():
        CanvasVictoire.place(x=0,y=0)
        traceImage(CanvasVictoire,IYouWin,0,0,"")

#----------------------------------------------------------------------------------------
#                                        Principal
#---------------------------------------------------------------------------------------


##### Stat de gugus
attaque=5
vie=20
niveauV=20
morts=0
victoires=0
vitesse = 8
Vitesse2 = 0.05
exp=0
####### Stat Chevalier
CHattaque=5
CHvie=12
CHniveauV=12
#######
Vieadv=0
NVieadv=0
Attaqueadv=0

Menuefface=0
Ntexte=1
Ntexte2=1
mape=1
mapa=0
X=530
Y=350
deplacementH = vitesse
deplacementB = vitesse
deplacementD = vitesse
deplacementG = vitesse
imageN=1
inverse=1

fenPrincip=Tk()
fenPrincip.geometry("1098x615")
fenPrincip.title("Menus")

Acceuil = PhotoImage(file=r"images\Menu.png")

IMage1 = PhotoImage(file=r"images\GG10.png")
IMage2 = PhotoImage(file=r"images\GG8.png")
IMage3 = PhotoImage(file=r"images\GG7.png")

IMageR1 = PhotoImage(file=r"images\GG9.png")
IMageR2 = PhotoImage(file=r"images\GG6.png")
IMageR3 = PhotoImage(file=r"images\GG5.png")

IMageM1 = PhotoImage(file=r"images\GG4.png")
IMageM2 = PhotoImage(file=r"images\GG3.png")

IMageB1 = PhotoImage(file=r"images\GG2.png")
IMageB2 = PhotoImage(file=r"images\GG1.png")

IStat = PhotoImage(file=r"images\StatPerso.png")

Carte1 =PhotoImage(file=r"images\carte1.png")
Carte2 =PhotoImage(file=r"images\carte2.png")
Carte3 =PhotoImage(file=r"images\carte3.png")
Carte4 =PhotoImage(file=r"images\carte4.png")

ICombat=PhotoImage(file=r"images\Combat.png")
IChevalier = PhotoImage(file=r"images\chevalier.png")
ISuperman= PhotoImage(file=r"images\superman.png")
I2Superman= PhotoImage(file=r"images\superman2.png")
IChCarte3 = PhotoImage(file=r"images\Ch1.png")
IGGCombat = PhotoImage(file=r"images\GGCombat.png")

Attaque = PhotoImage(file=r"images\Attaque.png")
Fuite = PhotoImage(file=r"images\Fuite.png")
Sac = PhotoImage(file=r"images\Sac.png")
Isacm = PhotoImage(file=r"images\Sacm.png")
ISave=PhotoImage(file=r"images\Save.png")
IBoxText=PhotoImage(file=r"images\Text box.png")
IYouWin=PhotoImage(file=r"images\youwin.png")

fenPrincip.bind("<Up>", BHH)
fenPrincip.bind("<Down>", BBB)
fenPrincip.bind("<Left>", BGG)
fenPrincip.bind("<Right>", BDD)
fenPrincip.bind("<p>", parler)
fenPrincip.bind("<Escape>", MontreMenu)
fenPrincip.bind("<c>", TestCombat)
fenPrincip.bind("<Button-1>", tuch)

ZoneDess=Canvas(width=1098,height=615,bd=0, bg="white")
CanvasMenu=Canvas(width=500,height=190,bd=0, bg="black")
CanvasCombat=Canvas(width=750,height=600,bd=-2, bg="black")
CanvasAcceuil=Canvas(width=1098,height=615,bd=0, bg="white")
CanvasVictoire=Canvas(width=1098,height=615,bd=0, bg="white")

BAttaque = Button(fenPrincip, text="", command=ATTAQUE, bd=-2)
BAttaque.config(image=Attaque)
BFuite = Button(fenPrincip, text="", command=FUITE, bd=-2)
BFuite.config(image=Fuite)
BSac = Button(fenPrincip, text="", command=SAC, bd=-2)
BSac.config(image=Sac)
Bsave = Button(fenPrincip, text="Save",fg="white",font="Arial 18", bg = "black", command=Sauvegarde, bd=-2)
Bcharge = Button(fenPrincip, text="Charger",fg="white",font="Arial 18", bg = "black", command=Continue, bd=-2)
Bquite = Button(fenPrincip, text="Quitter",fg="white",font="Arial 18", bg = "black", command=Ferme, bd=-2)

CanvasAcceuil.place(x=0,y=0)
traceImage(CanvasAcceuil,Acceuil,0,0,"")

fenPrincip.mainloop()