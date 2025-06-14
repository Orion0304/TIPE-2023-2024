from wave import*
import os



##Ce programme effectue une modification des octet de poids faible de chaque échantillon:

def modif_naif (fichier,message):
    fileread = open (fichier,'rb')
    nouveaufichier = open ('440-1.wav','wb')
    #récupération des infos nécessaires :
    infos= Wave_read.getparams(fileread)
    n= infos[3]
    #écriture de l'entete :
    Wave_write.setparams(nouveaufichier,infos)

    for i in range (n):
        longueur = len(message)
        a= Wave_read.readframes(fileread,1)

        if i<longueur :
            b= bytes([ord(message[i]), a[1]])
            Wave_write.writeframes(nouveaufichier,b)

        Wave_write.writeframes(nouveaufichier,a)

    Wave_read.close(fileread)
    Wave_write.close(nouveaufichier)


##Ce programme effectue une modification des octet de poids faible, en répétant le message autant de fois que possible dans le fichier:

def modif_repMessage (fichier,message) :

    fileread = open (fichier,'rb')
    nouveaufichier = open ('440-1.wav','wb')
    #récupération des infos nécessaires
    infos= Wave_read.getparams(fileread)
    n= infos[3]
    #écriture de l'entete
    Wave_write.setparams(nouveaufichier,infos)
    for i in range (n):
        longueur = len(message)
        a= Wave_read.readframes(fileread,1)
        b= bytes([ord(message[(i%longueur)]), a[1]])
        Wave_write.writeframes(nouveaufichier,b)
    Wave_read.close(fileread)
    Wave_write.close(nouveaufichier)


##Ce programme effectue une modification des octet de poids faible, en répétant le message autant de fois que possible dans le fichier et en répétant chaque caractère pour pouvoir l'indentifier à l'écoute du fichier modifié:

def modif_repMessage_et_repLettre (fichier,message,rep):
    fileread = open (fichier,'rb')
    nouveaufichier = open ('440-1.wav','wb')
    #récupération des infos nécessaires :
    infos= Wave_read.getparams(fileread)
    n= infos[3]
    longueur = len(message)
    #écriture de l'entête :
    Wave_write.setparams(nouveaufichier,infos)
    for i in range (n//rep):
        for j in range (rep):
            a= Wave_read.readframes(fileread,1)
            b= bytes([ord(message[i%longueur]), a[1]])
            Wave_write.writeframes(nouveaufichier,b)
    for k in range(n%rep):
        a= Wave_read.readframes(fileread,1)
        Wave_write.writeframes(nouveaufichier,a)
    Wave_read.close(fileread)
    Wave_write.close(nouveaufichier)

