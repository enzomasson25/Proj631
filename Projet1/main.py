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

import os

fichier_initial=r"alice.txt"

phrase = open(fichier_initial).read()
#phrase = "ceci est un test"

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
liste_caractere = ordonned[0]
liste_frequence = ordonned[1]

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
    
    def __init__(self,frequence,etiquette="",fils_gauche=None,fils_droit=None):
        self.frequence=frequence
        self.etiquette=etiquette 
        self.fils_gauche=fils_gauche
        self.fils_droit=fils_droit
    
    def __str__(self):
        return "frequence : " + str(self.frequence) + " gauche : " + str(self.fils_gauche.frequence) + " droit : " + str(self.fils_droit.frequence)
    
    def __gt__(self, other):
        if isinstance(other, arbre):
            if self.frequence > other.frequence:
                return True
            elif self.frequence <= other.frequence:
                return False
            elif self.frequence > other.frequence:
                return True
            elif self.frequence <= other.frequence:
                return False
    
    def __lt__(self, other):
        if isinstance(other, arbre):
            if self.frequence < other.frequence:
                return True
            elif self.frequence >= other.frequence:
                return False
            elif self.frequence < other.frequence:
                return True
            elif self.frequence >= other.frequence:
                return False
    
    def set_frequence(self,frequence):
        self.frequence=frequence
    
    def get_frequence(self):
        return self.frequence
    
    def get_fils_droit(self):
        return self.fils_droit
    
    def get_fils_gauche(self):
        return self.fils_gauche
    

    def parcourir(self,chemin=None,res={}):
        if self.get_fils_droit() is None and self.get_fils_gauche() is None:
            res[self.etiquette]=chemin
        if not self.get_fils_gauche() is None:
            if chemin is None:
                self.get_fils_gauche().parcourir('0')
            else:
                self.get_fils_gauche().parcourir(chemin + '0')            
        if not self.get_fils_droit() is None:        
            if chemin is None:
                self.get_fils_droit().parcourir('1')
            else:
                self.get_fils_droit().parcourir(chemin + '1')            
        
        return res
        

liste_arbre=[]
for i in range(0,len(liste_frequence)):
    liste_arbre.append(arbre(liste_frequence[i],liste_caractere[i]))
    
#for i in range(0,len(liste_arbre)):
#    print(liste_arbre[i].frequence)
while(len(liste_arbre)>1):
    min1=min(liste_arbre)
    liste_arbre.remove(min1)
    min2=min(liste_arbre)
    liste_arbre.remove(min2)
    liste_arbre.append(arbre(min1.frequence+min2.frequence,"",min1,min2))

racine = liste_arbre[0]


"""
Etape 3 : Codage du texte
Le code de chaque caractère est obtenu par un parcours en profondeur de l’arbre.
Chaque caractère du texte est alors codé par une succession de bits et le codage du texte est obtenu
par concaténation des codes de chacun de ses caractères. Il sera stocké octet par octet dans le texte
compressé.
"""

dic_carac_bin=racine.parcourir()

def remplacement_lettre_binaire(phrase):
    res=""
    for lettre in phrase:
        res = res+dic_carac_bin[lettre]
    return res

phrase_binaire=remplacement_lettre_binaire(phrase)

#ajout des bits manquants pour atteindre un nombre diviseur par 8 
while len(phrase_binaire)%8 != 0 :
    phrase_binaire=phrase_binaire+'0'

#ecriture du fichier simple composé de 0 et de 1
with open("data.txt", "w") as fichier:
	fichier.write(phrase_binaire)
fichier.close()

#ici on sépart cette liste de 0 et de 1 en groupe de 8 bits 
liste_octets=[]
for i in range(8,len(phrase_binaire),8):
    liste_octets.append(phrase_binaire[i-8:i])

#ecriture du fichier encodé en binaire celui-ci sera composé de symboles ascii 
with open("data.bin", "wb") as fichier:
    for octet in liste_octets:
        fichier.write((int(octet, base=2)).to_bytes(-(-len(octet)//8), byteorder='big'))
fichier.close()


"""
Etape 4 : Détermination du taux de compression
Le taux de compression constitue une mesure de performance de votre algorithme relativement au
texte à compresser. Il est défini comme le gain en volume rapporté au volume initial des données,
c’est-à-dire :
Taux de compression = Gain en volume / Volume initial = 1 – Volume final / Volume initial
Les volumes sont évalués en nombre d’octets
"""
size_final=(os.path.getsize("data.bin"))
size_initial=(os.path.getsize(fichier_initial))
taux_de_compression=1-(size_final/size_initial)
print("Le taux de compression pour "+str(fichier_initial)+" est de :"+str(taux_de_compression))


"""
Etape 5 : Détermination du nombre moyen de bits de stockage d’un caractère du texte compressé
"""
total = 0 
for lettre in liste_caractere:
    total = total + len(dic_carac_bin[lettre])

nb_moy_bits=total/len(liste_caractere)
print("Le nombre moyen de bits pour un caractère pour "+str(fichier_initial)+" est de : "+str(nb_moy_bits))





