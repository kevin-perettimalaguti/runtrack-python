def lettre(message, decalage):
    msg_code = ""
    
    for k in message:        
        
        if k.isalpha():       

            if k.islower():
                k = chr((ord(k) - ord('a') + decalage) % 26 + ord('a'))
                msg_code += k

            else:
                k = chr((ord(k) - ord('A') + decalage) % 26 + ord('A'))
                msg_code += k
        else:
            msg_code += k
    return msg_code


msg = "Sous le ciel étoilé, les rues silencieuses murmurent des histoires oubliées."
resultat = lettre(msg, 3)
print(resultat)
        
            