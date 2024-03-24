def LOGIN_GEN():
    name = ""
    first_name = ""
    login = ""
    name = input("Veuillez entrer votre nom de famille : ")
    first_name = input("Veuillez entrer votre prénom : ")
    print(first_name, name, "voici votre login : ")

    login = (first_name[0])+"."+ name[0]+name[1]+name[2]+name[3]

    print(login.lower())
    
LOGIN_GEN()