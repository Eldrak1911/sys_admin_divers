import random

LETTRES = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chiffres = ["0","1","2","3","4","5","6","7","8","9"]
Special = ["@","#","-","_","%","*","‰","€","$","£","µ","?","^"]
MDP = ""
print("Ce générateur de mot de passe créer des chaînes de 12 caractères.")

while (len(MDP) < 12):
    a = random.choice(LETTRES)
    MDP += a
    c = random.choice(chiffres)
    MDP += c
    d = random.choice(Special)
    MDP += d
    b = random.choice(lettres)
    MDP += b
else:
    print(MDP)