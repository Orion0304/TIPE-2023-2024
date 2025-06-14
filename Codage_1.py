from wave import *

'''Moitié faible des octets de poids forts modifiée, message répété tant qu'il y a du son et chaque lettre du message est répétée nbrep fois.'''

def codefort(nbrep, nmfichier, message):
    f_r = open(nmfichier, "rb")
    #a = Wave_read.getsampwidth(f_r)
    f_w = open("440-1.wav", "wb") #ouverture d'un fichier d'écriture wave


    Wave_write.setparams(f_w, Wave_read.getparams(f_r))

    #nombre d'échantillons
    n = Wave_read.getnframes(f_r)

    #Codage 2 à 2 de la nouvelle séquence d'octets
    k = 0
    for k in range(n//(2*nbrep)): #n//2 doubles échantillons
        lettre = message[k % len(message)]

        for ite in range(nbrep):
            seq = Wave_read.readframes(f_r, 2)  #lecture de 2 échantillons consécutifs
            b = ord(lettre)
            debut = b//16
            fin = b % 16
            seq2 = (bytes([(seq[1]//16)*16+debut]), bytes([seq[1]]),bytes([(seq[3]//16)*16+fin]), bytes([seq[3]]))

            for i in range(4):                  #écriture de la séquence modifiée
                Wave_write.writeframes(f_w, seq2[i])

    Wave_read.close(f_r)
    Wave_write.close(f_w)
