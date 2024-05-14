
import random
miniscule = "azertyuiop^qsdfghjklmùwxcvnn"
majisucle ="AZERTYUIOP¨QSDFGHJKLMWXCVBN"
nombre = "123456789"
symbole=""
x = int(input("Combiren de mot pass tu veux "))
tout =  miniscule + majisucle + nombre + symbole
lenght = int(input("entre how much do you wanna"))
for i in  range(x):
    motpass ="".join(random.sample(tout,lenght))
    print(motpass)








