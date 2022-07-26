palabra = ()
contador = 0
pali_ok = 0
pali_no_ok = 0
while palabra != "aloha" and palabra != "bye" :
    palabra = (input ("Ingrese palabra a evaluar : "))
    if palabra != "aloha" and palabra != "bye" :
        contador += 1
        if palabra == palabra [::-1] :
            pali_ok += 1            
        else :                           
            pali_no_ok += 1

print ("Se ingresaron",contador,"palabras.",pali_ok,"eran palindromos y",pali_no_ok,"no lo eran") 