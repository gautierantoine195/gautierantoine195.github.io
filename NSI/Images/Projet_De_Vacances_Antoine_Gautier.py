import turtle
turtle.tracer(0,0)
turtle.screensize(2000,2000)
turtle.pu()
turtle.goto(-500,0)
turtle.pd()

def dessiner(courbe, longueur, angle):
    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)

def regleSierpinski(chaine):
    nouvelleChaine = ''
    for lettre in chaine:
        if lettre == 'F':
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'
        elif lettre == 'G':
            nouvelleChaine = nouvelleChaine + 'GG'
        else :
            nouvelleChaine = nouvelleChaine + lettre
    return nouvelleChaine

def courbeSierpinski(motifInitial, niter):
    courbe = motifInitial
    for i in range(niter):
        nouveauMotif = regleSierpinski(courbe)
        courbe = nouveauMotif
    return courbe

longueur = 10
angle = 120
niter = 6
dessiner(courbeSierpinski('F-G-G', niter), longueur, angle)


turtle.update()
turtle.exitonclick()