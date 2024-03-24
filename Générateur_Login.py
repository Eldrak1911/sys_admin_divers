def LOGIN_GEN():
    name = ""
    first_name = ""
    login = ""
    longeur = int(input("Veuillez entrer la longeur du login souhaitée : "))
    name = input("Veuillez entrer votre nom de famille : ")
    first_name = input("Veuillez entrer votre prénom : ")
    print(first_name, name, "voici votre login : ")
    
    login = (first_name[0])+"."+name
    
    print(login[:longeur].lower())
    
LOGIN_GEN()