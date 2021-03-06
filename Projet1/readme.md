# Descriptif général

Le codage de Huffman, du nom de son concepteur, est une méthode statistique de compression de
données. Son principe est de remplacer un caractère (ou symbole) par une suite de bits de longueur
variable. L'idée sous-jacente est de coder ce qui est fréquent sur peu de bits et au contraire ce qui est
rare sur des séquences de bits plus longues. Il permet une compression sans perte, c’est-à-dire qu’une
suite de bits strictement identique à l’originale est restituée par décompression. Il nécessite cependant
que soit connues (ou estimées) les fréquences d’apparition des différents symboles à coder. Il existe
ainsi plusieurs variantes de l’algorithme de Huffman (statique, semi-adaptatif ou adaptatif)
aujourd’hui utilisées dans des algorithmes de compression de fichiers tels que gzip.
Ce sujet concerne la version semi-adaptative de l’algorithme dans laquelle le texte à coder est tout
d’abord lu intégralement de façon à construire l’alphabet et déterminer les fréquences d’apparition
des éléments de l’alphabet.

# Fonctionnement du programme

![alt text](https://github.com/enzomasson25/Proj631/blob/master/Projet1/src/Untitled%20Diagram.png)

# Utilisation du programme 

Exécuter le code du fichier main.py, renseigner le fichier que vous voulez compresser. Le fichier compressé data.bin de votre fichier de départ se trouve dans le dossier du main.py.
