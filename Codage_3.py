from wave import  *

'''Octets de poids faible modifiée, message répétés tant qu'il y a du son et chaque lettre du message est répétée nbrep fois.'''

def codage(nbrep, nmfichier, message):
    f_r = open(nmfichier, "rb")
    #a = Wave_read.getsampwidth(f_r)
    f_w = open("440-1.wav", "wb") #ouverture d'un fichier d'écriture wave


    Wave_write.setparams(f_w, Wave_read.getparams(f_r))

    #nombre d'échantillons
    n = Wave_read.getnframes(f_r)

    #Codage 2 à 2 de la nouvelle séquence d'octets
    k = 0
    for k in range(n//(4*nbrep)): #n//2 doubles échantillons
        for ite in range(nbrep):

            lettre = message[k % len(message)]
            b = ord(lettre)
            a1=b//64
            b=b-64*a1
            a2=b//16
            b=b-16*a2
            a3=b//4
            a4=b%4
            a=[a1,a2,a3,a4]

            seq = Wave_read.readframes(f_r, 4)  #lecture de 4 échantillons consécutifs
            A = seq[:2],seq[2:4],seq[4:6],seq[6:]

            for i in range(4):
                A1 = (A[i][1]//64)*64+a[i]*16+A[i][1]%16
                Wave_write.writeframes(f_w, bytes([A[i][0]]))    #écriture de la séquence modifiée
                Wave_write.writeframes(f_w, bytes([A1]))

    Wave_read.close(f_r)
    Wave_write.close(f_w)
