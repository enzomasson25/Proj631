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

phrase="bonjour!!"

def generation_alphabet_frequence():
    alphabet=[]
    frequence=[]
    for i in range(0,len(phrase)):
        if phrase[i] not in alphabet:
            alphabet.append(phrase[i])
            frequence.append(1)
        else:
            rang=alphabet.index(phrase[i])
            frequence[rang]=frequence[rang]+1
    return alphabet, frequence

def ordonnement_par_frequence():
    pass

def ordonnement_par_ascii():
    pass