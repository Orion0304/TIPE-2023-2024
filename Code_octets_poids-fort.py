from wave import *

fichier_entree = open("440.wav","rb")
fichier_ecriture = open("440-1.wav","wb")

print(Wave_read.getparams(fichier_entree))
print(Wave_read.getnframes(fichier_entree))


#écriture des informations récupérées au-dessus:
Wave_write.setparams(fichier_ecriture,Wave_read.getparams(fichier_entree))

message='Coucou ceci est un test'

## Programme qui remplace les octets de poids fort par le même caractère 1000 fois de suite jusqu'à la fin du message, ensuite il recopie tel quel le fichier:

def code_repe_char(fichier_original,message):
    fichier_entree = open(fichier_original,'rb')
    fichier_ecriture = open("440-1.wav",'wb')
    Wave_write.setparams(fichier_ecriture,Wave_read.getparams(fichier_entree))
    for j in range(Wave_read.getnframes(fichier_entree)):
        if j< len(message):
            for i in range(1):
                a= Wave_read.readframes(fichier_entree,1)
                b=bytes([a[0],ord(message[j])])
                Wave_write.writeframes(fichier_ecriture,b)

        else:
            a= Wave_read.readframes(fichier_entree,1)
            Wave_write.writeframes(fichier_ecriture,a)

    Wave_write.close(fichier_ecriture)#enregistre et ferme le fichier une fois que les      informations sont écrites
    Wave_read.close(fichier_entree)#enregistre et ferme le fichier une fois que les informations sont écrites


## Ici le programme recopie plusieurs fois de suite le même carcère, puis 'attend' plusieurs échantillons pui passe au caractère suivant:

def code_repe_tout(fichier_entree,message,repe_char,tps_att):
    fichier_original = open(fichier_entree,'rb')
    fichier_sortie = open("440-1.wav",'wb')
    Wave_write.setparams(fichier_sortie,Wave_read.getparams(fichier_original))
    for j in range(Wave_read.getnframes(fichier_original)):

        if j< len(message):
            for i in range(repe_char):
                a= Wave_read.readframes(fichier_original,1)
                b=bytes([a[0],ord(message[j])])
                Wave_write.writeframes(fichier_sortie,b)

            for i in range(tps_att):
                a= Wave_read.readframes(fichier_original,1)
                Wave_write.writeframes(fichier_sortie,a)

        else:
            a= Wave_read.readframes(fichier_original,1)
            Wave_write.writeframes(fichier_sortie,a)

    Wave_write.close(fichier_sortie)#enregistre et ferme le fichier une fois que les informations sont écrites
    Wave_read.close(fichier_original)#enregistre et ferme le fichier une fois que les informations sont écrites

