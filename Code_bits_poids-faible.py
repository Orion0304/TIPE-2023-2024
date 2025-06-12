"""moitié forte des octets de poids faible
message répétés tant qu'il y a du son
lettres répétées nbrep fois"""

from wave import*
fr="440.wav"

def codefaible(nbrep, nmfichier, message):
    f_r = open(nmfichier, "rb")
    #a = Wave_read.getsampwidth(f_r)
    f_w = open("440-1.wav", "wb") #ouverture d'un fichier d'écriture wave


    Wave_write.setparams(f_w, Wave_read.getparams(f_r))

    #nombre d'échantillons
    n = Wave_read.getnframes(f_r)

    #Codage 2 à 2 de la nouvelle séquence d'octets
    k = 0
    for k in range(n//(2*nbrep)): #n//2 doubles échantillons
        for ite in range(nbrep):
            lettre = message[k % len(message)]
            seq = Wave_read.readframes(f_r, 2)
            b = ord(lettre)
            #a = bytes([b])
            debut = bytes([(b//(2**3))*(2**3)])
            fin = bytes([(b % (2**3))*(2**3)])
            seq2 = (debut, bytes([seq[1]]), fin, bytes([seq[3]]))
            for i in range(4):
                Wave_write.writeframes(f_w, seq2[i])

    Wave_read.close(f_r)
    Wave_write.close(f_w)
