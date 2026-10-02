class Noeud:
    def __init__(self, valeur, enfant=[]):
        self.valeur = valeur
        self.enfant = enfant

    def ajouter_enfant(self, noeud):
        self.enfant.append(noeud)

    def affichage_polonais(self):
        # Cas de base : une feuille (pas d'enfants) → on affiche juste sa valeur
        if len(self.enfant) == 0:
            return str(self.valeur)

        # Cas récursif : un nœud avec des enfants
        # on affiche la valeur, puis "(" + enfants séparés par des virgules + ")"
        enfants_str = [enfant.affichage_polonais() for enfant in self.enfant]
        return f"{self.valeur}({', '.join(enfants_str)})"

#qst5
    import math

def evaluer(self, dic):

    if isinstance(self.valeur, int):
        return float(self.valeur)

    if isinstance(self.valeur, float):
        return self.valeur

    if isinstance(self.valeur, str):

        if self.valeur == "+":
            valeur1 = self.enfant[0].evaluer(dic)
            valeur2 = self.enfant[1].evaluer(dic)
            return valeur1 + valeur2

        if self.valeur == "-":
            valeur1 = self.enfant[0].evaluer(dic)
            valeur2 = self.enfant[1].evaluer(dic)
            return valeur1 - valeur2

        if self.valeur == "*":
            valeur1 = self.enfant[0].evaluer(dic)
            valeur2 = self.enfant[1].evaluer(dic)
            return valeur1 * valeur2

        if self.valeur in dic:
            return float(dic[self.valeur])

        raise ValueError("La variable " + self.valeur + " n'a pas de valeur")


# --- test --- polonais 
feuille_3 = Noeud(3)
feuille_x = Noeud("x")
noeud_sin = Noeud("sin", [feuille_x])
racine_mul = Noeud("mul", [feuille_3, noeud_sin])

print(racine_mul.affichage_polonais())
# mul(3, sin(x))