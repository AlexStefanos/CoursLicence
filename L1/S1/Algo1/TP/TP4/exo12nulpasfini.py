#exo10.py*2 pour avoir 2 listes à partir de 2 chaînes de caractère, n°1
chaine=input("Saisissez une liste de notes avec des espaces entre chaque note : ")
esp=" "
liste1=[]
txt=""
txtv=""
liste2=[]
i=0
a=0
for c in chaine :
    if chaine[i]==esp:
        liste1=liste1+[i]
        liste2.append(txt)
        txt=txtv
        i=i+1
    else :
        txt=txt+c
        i=i+1
liste2.append(txt)
txt=txtv
#n°2
chaine2=input("Saisissez la liste des noms dans l'ordre par rapport aux notes avec des espaces entre chaque noms : ")
liste3=[]
txt2=""
txtv=""
liste4=[]
i2=0
a2=0
for c2 in chaine2 :
    if chaine2[i2]==esp:
        liste3=liste3+[i2]
        liste4.append(txt2)
        txt2=txtv
        i2=i2+1
    else :
        txt2=txt2+c2
        i2=i2+1
liste4.append(txt2)
txt2=txtv
#début exo 12
liste5=[]
txt3=""
liste6=[]
i3=0
a3=0
d=1
liste7=[]
if len(liste2)==len(liste4):
    chaine3=input("Saisissez la liste des mentions dans l'ordre par rapport aux notes avec des espaces entre chaque noms : ")
    for c3 in chaine3 :
        if chaine3[i3]==esp:
            liste5=liste5+[i3]
            liste6.append(txt3)
            txt3=txtv
            i3=i3+1
        else :
            txt3=txt3+c3
            i3=i3+1
    liste6.append(txt3)
    txt3=txtv
    liste7=[liste2,liste4,liste6]
    print(liste7)

        
