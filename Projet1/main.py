# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:19:44 2020

@author: Masson Enzo
"""
import os #utiliser pour connaitre la taille d'un fichier (étape 4)

"""
Etape 1 : Détermination de l’alphabet et des fréquences de caractères
"""

#fichier de départ
fichier_initial=r"alice.txt"
phrase = open(fichier_initial).read()


def generation_alphabet_frequence(phrase):
    """
    generation_alphabet_frequence(String phrase) -> return List[String] alphabet, List[int] frequence
    Fonction qui va compter tous les caractères d'une String 
    Retourne deux List donc les rangs correspondent 
        frequence[i]=nb occurence de alphabet[i]
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
"""

 
class arbre:
    
    #constructeur de la classe arbre :
    def __init__(self,frequence,etiquette="",fils_gauche=None,fils_droit=None):
        self.frequence=frequence
        self.etiquette=etiquette 
        self.fils_gauche=fils_gauche
        self.fils_droit=fils_droit
    
    #surchargement de la classe arbre :
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
    
    
    #set de la classe arbre :
    def set_frequence(self,frequence):
        self.frequence=frequence
    
    
    #get de la classe arbre :
    def get_frequence(self):
        return self.frequence
    
    def get_fils_droit(self):
        return self.fils_droit
    
    def get_fils_gauche(self):
        return self.fils_gauche
    
    
    #fonctions :
    def parcourir(self,chemin=None,res={}):
        """
        parcourir(arbre,String,Dictionary{String etiquette:String chemin}) -> return Dictionary{String etiquette:String chemin}
        fonction qui parcours un arbre en profondeur
        retourne le dictionnaire composé des étiquettes des feuilles et de leur code binaire ici appelé chemin
        """
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
        
#Construction de l'arbre :

#On crée un arbre pour chaque caractère 
liste_arbre=[]
for i in range(0,len(liste_frequence)):
    liste_arbre.append(arbre(liste_frequence[i],liste_caractere[i]))
    
#Tant qu'on a plus q'un arbre on prend les 2 arbres avec les plus petites fréquences puis on crée un arbre avec ces arbres
while(len(liste_arbre)>1):
    min1=min(liste_arbre)
    liste_arbre.remove(min1)
    min2=min(liste_arbre)
    liste_arbre.remove(min2)
    liste_arbre.append(arbre(min1.frequence+min2.frequence,"",min1,min2))

#Quand notre arbre est fini la racine est le premier (et unique) élément de notre liste d'arbre
racine = liste_arbre[0]


"""
Etape 3 : Codage du texte
"""


dic_carac_bin=racine.parcourir()


def remplacement_lettre_binaire(phrase):
    """
    remplacement_lettre_binaire(String phrase) -> Return String
    Fonction qui remplace chaque caractère d'une String par son code binaire correspondant dans le dictionnaire dic_carac_bin
    """
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
        fichier.write((int(octet, base=2)).to_bytes((len(octet)//8), byteorder='big')) #on convertit notre octet en int puis on le convertit en bytes et enfin on l'écrit dans notre fichier
fichier.close()


"""
Etape 4 : Détermination du taux de compression
"""

#definition variables : 
size_final=(os.path.getsize("data.bin"))
size_initial=(os.path.getsize(fichier_initial))

#calcul du taux de compression :
taux_de_compression=1-(size_final/size_initial)

#affichage : 
print("Le taux de compression pour "+str(fichier_initial)+" est de :"+str(taux_de_compression))


"""
Etape 5 : Détermination du nombre moyen de bits de stockage d’un caractère du texte compressé
"""

#definition variable :
total = 0 

#calcul de la moyene de bits d'un caractère :
for lettre in liste_caractere:
    total = total + len(dic_carac_bin[lettre])
nb_moy_bits=total/len(liste_caractere)

#affichage : 
print("Le nombre moyen de bits pour un caractère pour "+str(fichier_initial)+" est de : "+str(nb_moy_bits))





