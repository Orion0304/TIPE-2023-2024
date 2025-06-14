import wave

def decodage_4(nbrep, nmfichier):
    f_r = open(nmfichier, "rb")
    #a = Wave_read.getsampwidth(f_r)
    #nombre d'échantillons
    n = Wave_read.getnframes(f_r)
    #indice du premier échantillon
    i = 0
    message = ""

    while i < n-4*nbrep: #tant qu'il est possible de coder nbrep lettres dans le reste du fichier
        ite = 0 #iteration de la lettre à décoder
        lettre = "" #possibles lettres décodées à la suite

        while ite<nbrep:
            sequence = Wave_read.readframes(f_r,4)
            a1 = (sequence[1]-128*(sequence[1]//128))//32
            a2 = (sequence[3]-128*(sequence[3]//128))//32
            a3 = (sequence[5]-128*(sequence[5]//128))//32
            a4 = (sequence[7]-128*(sequence[7]//128))//32
            lettre = lettre + chr(a1*64+a2*16+a3*4+a4)
            i = i+4
            ite = ite+1

        #determination de la lettre codée la plus probable (en cas de décodage après diffusion de la musique)
        d = {} #dictionnaire associant chaque lettre visible à son nombre d'occurrences
        for l in lettre:
            if not l in d:
                d[l] = 1
            else:
                d[l] = d[l] +1
        max = 0 #nombre d'occurrences de la lettre apparaissant le plus de fois
        vraielettre = "" #lettre apparaissant le plus de fois
        for l in d:
            if d[l] > max:
                vraielettre = l
                max = d[l]

        message = message + vraielettre
    return message