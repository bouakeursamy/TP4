from noeud import Noeud 
#qst4
n1 = Noeud (2)
n2 = Noeud ("y")
n_plus=Noeud("+",[n1,n2])
n_expo=Noeud("exp",[n_plus])

print(n_expo.affichage_polonais())

