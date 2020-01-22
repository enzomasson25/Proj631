# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:19:44 2020

@author: 33762
"""

"""
Etape 1 : Détermination de l’alphabet et des fréquences de caractères

L’alphabet sera composé des caractères présents dans le texte fourni et uniquement de ceux-ci. La
fréquence des différents caractères de l’alphabet dans le texte sera déterminée. Le terme fréquence
est ici, et dans toute la suite, utilisé pour une fréquence absolue, c’est-à-dire un nombre d’occurrences
des caractères dans le texte. L’ordre des caractères de l’alphabet sera maintenu par fréquence
croissante puis par ordre de codage des caractères ASCII
"""


phrase = open(r"C:\Users\33762\Desktop\cours\Sem6\ProjetAlgo\projet1\alice.txt").read()


def generation_alphabet_frequence(phrase):
    """
    
    """
    alphabet = []
    frequence = []
    for i in range(0,len(phrase)):
        if phrase[i] not in alphabet:
            alphabet.append(phrase[i])
            frequence.append(1)
        else:
            rang = alphabet.index(phrase[i])
            frequence[rang] = frequence[rang]+1
    return alphabet, frequence

def ordonnement_par_frequence(alphabet,frequence,alphabet_ordonne=[],frequence_ordonnee=[]):
    if alphabet==[]:
        return alphabet_ordonne, frequence_ordonnee
    freq_min = min(frequence)
    for i in range(0,len(frequence)):
        if frequence[i]==freq_min:
            alphabet_ordonne.append(alphabet[i])
            frequence_ordonnee.append(frequence[i])
    for element in alphabet_ordonne:
        if element in alphabet:
            alphabet.remove(element)
    for element in frequence_ordonnee:
        if element in frequence:
            frequence.remove(element)
    return ordonnement_par_frequence(alphabet,frequence,alphabet_ordonne,frequence_ordonnee)

def ordonnement_par_ascii(alphabet,frequence):
    res = []
    alphabet_decoupe=decoupage(alphabet,frequence)
    for alpha in alphabet_decoupe:
        alpha = sorted(alpha,key = ord)
        res = res + alpha
    return res,frequence

def decoupage(alphabet,frequence):
    res = []
    frequence_sans_doublon = sorted(set(frequence))
    for element in frequence_sans_doublon:
        tab = []
        for i in range(0,len(frequence)):
            if frequence[i] == element:
                tab.append(alphabet[i])
        res.append(tab)
    return res


alphabet=generation_alphabet_frequence(phrase)[0]
frequence=generation_alphabet_frequence(phrase)[1]
alphabet_frequence_ordonne_frq=ordonnement_par_frequence(alphabet,frequence)
ordonned=ordonnement_par_ascii(alphabet_frequence_ordonne_frq[0],alphabet_frequence_ordonne_frq[1])
print(ordonned[0])
print(ordonned[1])


"""
Etape 2 : Construction de l’arbre

L’algorithme est décrit dans l’article de son créateur publié en 1952. Il repose sur une structure
d’arbre binaire où tous les nœuds internes ont exactement deux successeurs. Les feuilles sont
étiquetées avec les caractères de l’alphabet, les branches par 0 (fils gauche) et 1 (fils droit). Les
chemins depuis la racine jusqu’aux feuilles constituent les codes des caractères.

La construction de l’arbre est réalisée de la manière suivante :
    
Créer un arbre (feuille) pour chaque caractère de l’alphabet avec la fréquence associée
Répéter
Déterminer les 2 arbres t1 et t2 de fréquence minimale avec t1.freq <= t2.freq
Créer un nouvel arbre t avec t1 et t2 comme sous-arbres respectivement gauche et droite
avec t.freq = t1.freq + t2.freq
Jusqu’à ce qu’il ne reste plus qu’un seul arbre
"""

class arbre:
    
    
    def arbre(self,frequence,etiquette="",fils_gauche=None,fils_droit=None):
        self.frequence=frequence
        self.etiquette=etiquette 
        self.fils_gauche=fils_gauche
        self.fils_droit=fils_droit
    
    def set_frequence(self,frequence):
        self.frequence=frequence
    
    #exemple :
#    arbreb=arbre(1,'b')
#    arbrej=arbre(1,'j')
#    arbren=arbre(1,'n')
#    arbrer=arbre(1,'r')
#    arbreu=arbre(1,'u')
#    arbrebexc=arbre(2,'!')
#    arbreo=arbre(2,'o')
#    arbre1=arbre(2,'',arbreb,arbrej)
#    arbre2=arbre(2,'',arbren,arbrer)
#    arbre3=arbre(3,'',arbreu,arbrebexc)
#    arbre4=arbre(4,'',arbreo,arbre2)
#    arbre5=arbre(5,'',arbre2,arbre3)
#    arbre6=arbre(9,'',arbre4,arbre5)
    



