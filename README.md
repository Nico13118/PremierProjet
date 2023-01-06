# Fonctionnement du Script

Le script permet de se connecter sur le site <https://books.toscrape.com> afin de récupérer  
toutes les images dans un répertoire et toutes les informations de chaque livre dans un fichier csv.

Lors de son exécution, les répertoires nommés **"BooksToScrape"** et **"Categories"** seront créés à  
l'endroit où se trouve le fichier script.

Dans le répertoire **"Categories"** vous trouverez un répertoire pour chaque catégorie avec un  
fichier csv ainsi qu'un répertoire pour les images.

Le Script affichera dans le terminal Python plusieurs tests de connexion puis procèdera à l'enregistrement  
des informations de chaque livre.  
Lorsque le Scrip aura récupéré tous les livres, un message vous indiquera 
"**Téléchargerment terminé"**,  
le répertoire **"Catégories"** sera renommé sous la forme d'une date, ce qui vous permettra de relancer  
le script un autre jour à des fins de comparaison.  
Si pour une raison ou une autre le Script venais à s'arrêter pendant la récupération des données, vous  
pouvez relancer le script, le répertoire **"Categories"** sera écrasé puis reprendra son cycle normal.

## 1) Notice d'installation Python

Pour l'installation de Python sous Windows ou Mac, cliquez sur le lien suivant :  
<https://fr.wikihow.com/installer-Python>

- Sous Windows, suivre les indications **"Méthode 1"**.


- Sous Mac \ Linux, suivre les indications **"Méthode 2"**.



## 2) Création d'un répertoire sur votre bureau
Ouvrir le terminal puis saisir les lignes de commandes suivantes :  
```sh
cd desktop   
   ```

```sh
mkdir Books   
   ```
```sh
cd books   
   ```
  

Garder le terminal ouvert

## 3) Téléchargement et décompression du Script

Cliquez sur le lien suivant pour télécharger le script :  
<https://github.com/Nico13118/PremierProjet/archive/refs/heads/master.zip>  
Une fois téléchargé, placer le fichier zip dans le répertoire Books, vous allez devoir ensuite  
le décompresser.

- Pour décompresser un fichier zip sous Windows :  Faites un clic droit sur le fichier .zip  
puis sélectionner "Extraire tout...", puis Extraire.


- Pour décompresser un fichier zip sous Mac \ Linux : Cliquez deux fois sur le fichier .zip.  
L’élément décompressé apparaît dans le même dossier que le fichier .zip.

## 4) Création d'un environnement virtuel

Depuis le terminal, saisir la commande suivante :  

Sous Windows :
```sh
python -m venv env   
   ```
  

Sous Mac \ Linux :
```sh
python3 -m venv env   
   ```

## 5) Activation de l'environnement virtuel

Depuis le terminal, saisir la commande suivante :

Sous Windows :  

```sh
env\Scripts\activate.ps1 ou env\Scripts\activate.bat
   ```
Sous Mac \ Linux :
```sh
env/bin/activate
   ```

## 6) Installation des librairies 

Depuis le terminal, saisir la commande suivante :
```sh
pip install -r requirements.txt
   ```
 

## 7) Exécution du Script

Depuis le terminal, saisir la commande suivante :  

Sous Windows :
```sh
python Script.py   
   ```

Sous Mac \ Linux :
```sh
python Script.py
   ```


