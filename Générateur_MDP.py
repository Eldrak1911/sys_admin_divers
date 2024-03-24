def MDPGEN():
    import random

    LETTRES = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chiffres = ["0","1","2","3","4","5","6","7","8","9"]
    Special = ["@","#","-","","%","*","‰","€","$","£","µ","?","^"]
    MDP = [""]
    mdp_final = ""
    longeur = int(input("Veuillez entrer le nombre de caractères souhaités : "))
    print("Ce générateur de mot de passe créera des chaînes de {longeur} caractères.")

    while (len(MDP) < longeur):
        a = random.choice(LETTRES)
        MDP += a
        c = random.choice(chiffres)
        MDP += c
        d = random.choice(Special)
        MDP += d
        b = random.choice(lettres)
        MDP += b
    else:
        random.shuffle(MDP)
        for i in MDP:
            mdp_final += i
        print(mdp_final)

MDPGEN()