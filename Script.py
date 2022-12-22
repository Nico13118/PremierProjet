import re
import shutil
import time
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os

manquant = "https://books.toscrape.com/catalogue/"
liste_liens_livres3 = []
global url_category, page_accueil, url_accueil, page_directory, page_category, reponse, liste_categorie_accueil2, recuperation_liens_livre6, page_livre, page_livre2, page_lien_livre2, page_lien_livre4
data = os.getcwd()
##################################################################################################
# Condition qui permet de contrôler si le répertoire BookToScrape\Catégorie existe

recherche_fichier_bookstoscrape_categories = os.path.exists(f"{data}/BooksToScrape/Categories")
recherche_fichier_bookstoscrape = os.path.exists(f"{data}/BooksToScrape")
if recherche_fichier_bookstoscrape:
    if recherche_fichier_bookstoscrape_categories:
        # print("Si le fichier Catégories existe")
        shutil.rmtree(f"{data}/BooksToScrape/Categories")
        print(f"Création du répertoire Catgories dans {data}")
        os.mkdir(f"{data}/BooksToScrape/Categories")

    if not recherche_fichier_bookstoscrape_categories:
        os.mkdir(f"{data}/BooksToScrape/Categories")


else:
    print("Création du répertoire BooksToScrape et Categories")
    os.mkdir(f"{data}/BooksToScrape")
    os.mkdir(f"{data}/BooksToScrape/Categories")

##################################################################################################
# Récupération du nom de chaque catégorie ( Travel ...)
page_directory2 = 0
while not page_directory2 == 200:
    url_directory = "https://books.toscrape.com/"
    try:
        page_directory = requests.get(url_directory)
        page_directory2 = page_directory.status_code
        if page_directory2 == 200:
            print(f"Test de connexion sur le site {url_directory}: OK")

    except:
        print("Problème de connexion, nouvelle tentative dans 15 secondes")
        sleep(15)

soup_directory = BeautifulSoup(page_directory.content, "html.parser")

directory_categorie_1 = soup_directory.find_all("a")
liste_directory_1 = []
for directory_categorie_2 in directory_categorie_1:
    directory_categorie_3 = directory_categorie_2.get_text()
    directory_categorie_3 = directory_categorie_3.strip()
    #print(directory_categorie_3)
    liste_directory_1.append(directory_categorie_3)
liste_directory_2 = liste_directory_1[3:53]

#print(liste_directory_2)

###################################################################################################
#Boucle qui va créer un répertoire pour chaque catégorie
nombre_categorie_accueil1 = len(liste_directory_2)
nombre_categorie_accueil2 = nombre_categorie_accueil1 + 1
h, i = 0, 0
while h < nombre_categorie_accueil2:
    h = h + 1
    if h == nombre_categorie_accueil2:
        break
    elif h < nombre_categorie_accueil2:
        nom_categorie_accueil = liste_directory_2[i]
        os.mkdir(f"{data}/BooksToScrape/Categories/{nom_categorie_accueil}")
        i = i + 1



##################################################################################################
# Boucle qui va créer un répertoire Images dans "Categories/le_nom_de_la_catégorie"
nombre_categorie_accueil3 = nombre_categorie_accueil1 + 1
j, k = 0, 0
while j < nombre_categorie_accueil3:
    j = j + 1
    if j == nombre_categorie_accueil3:
        break
    elif j < nombre_categorie_accueil3:
        nom_categorie_accueil2 = liste_directory_2[k]
        os.mkdir(f"{data}/BooksToScrape/Categories/{nom_categorie_accueil2}/Images")
        k = k + 1


##################################################################################################
##################################################################################################
# Création d'une liste de lien pour chaque catégorie de la page d'accueil books.toscrape.com
page_accueil2 = 0
while not page_accueil2 == 200:
    url_accueil = "https://books.toscrape.com/"
    try:
        page_accueil = requests.get(url_accueil)
        page_accueil2 = page_accueil.status_code
        if page_accueil2 == 200:
            print("Création d'une liste de lien par catégorie")
    except:
        print("Problème de connexion, nouvelle tentative dans 15 secondes")
        sleep(15)
soup_accueil = BeautifulSoup(page_accueil.content, "html.parser")
index = "index.html"
books1 = "catalogue/category/books_1/index.html"

categorie_page_accueil1 = soup_accueil.find_all("a")
liste_categorie_accueil = []
for categorie_page_accueil2 in categorie_page_accueil1:
    categorie_page_accueil3 = categorie_page_accueil2.get("href")
    # Une condition, ne récupère pas les liens index et books1
    if categorie_page_accueil3 != index:
        if categorie_page_accueil3 != books1:
            # Création du lien
            categorie_page_accueil4 = url_accueil + categorie_page_accueil3
            liste_categorie_accueil.append(categorie_page_accueil4)
liste_categorie_accueil2 = liste_categorie_accueil[:50]
# print(liste_categorie_accueil2)
# print(len(liste_categorie_accueil2))
nombre_de_categorie1 = len(liste_categorie_accueil2)


##################################################################################################
# Une boucle qui va lister les liens de chaque catégorie une par une
f, g = 0, 0
nombre_de_categorie2 = nombre_de_categorie1
nombre_de_categorie2 = nombre_de_categorie2 + 1
while g < nombre_de_categorie2:
    g = g + 1
    #print(liste_categorie_accueil2[f])
    if g < nombre_de_categorie2:
        url_category = liste_categorie_accueil2[f]
        f = f + 1
    if g == nombre_de_categorie2:
        print("Création des liens de chaque catégorie : Terminé")
        break
        # print("Téléchargement terminé")

        # break
    #print(url_category)


    ################################################################################################
    # Une boucle qui va initialiser un lien par rapport au nombre de pages
    page_category2 = 0
    while not page_category2 == 200:
        try:
            page_category = requests.get(url_category)
            page_category2 = page_category.status_code
            if page_category2 == 200:
                print("Ligne 153")
        except:
            print("Problème de connexion, nouvelle tentative dans 15 secondes")
            sleep(15)

    soup_category = BeautifulSoup(page_category.content, "html.parser")



    liste_liens_pages = []
    recherche_page1 = soup_category.find("li", class_="current")
    if recherche_page1:
        # Si recherche_page1 est vrai alors supprime les 10 derniers caractère de url_category
        modif_url_category = url_category[:-10]
        recherche_page2 = recherche_page1.get_text()
        #Suppression \n
        recherche_page3 = recherche_page2.strip()
        # Suppressions des caractères pour garder le nombre de pages
        recherche_page4 = recherche_page3[10:]
        recherche_page4 = int(recherche_page4)
        a = 0
        while a != recherche_page4:
            a = a + 1
            nouvelle_adresse = f"{modif_url_category}page-{a}.html"
            liste_liens_pages.append(nouvelle_adresse)

    if not recherche_page1:
        # Si recherche_page1 = None alors ajoute l'adresse directement dans la liste
        liste_liens_pages.append(url_category)
    #print(liste_liens_pages)

    # Une boucle qui va lister une par une les url de chaque page
    nombre_page = len(liste_liens_pages)
    #print(nombre_page)
    b, c = 0, 0
    nombre_page = nombre_page + 1
    while c < nombre_page:
        if c < nombre_page:
            c = c + 1
            if c == nombre_page:
                break
            if c < nombre_page:
                resultat = liste_liens_pages[b]
                b = b + 1
                resultat = str(resultat)



                url_livre = resultat
                #print("Ligne 63", url_livre)
                url_livre_fusion = url_livre[0:37]
                page_livre2 = 0
                while not page_livre2 == 200:
                    try:
                        page_livre = requests.get(url_livre)
                        page_livre2 = page_livre.status_code
                        if page_livre2 == 200:
                            print("Ligne 210")

                    except:
                        print("Problème de connexion, nouvelle tentative dans 15 secondes")
                        sleep(15)

                soup_livre = BeautifulSoup(page_livre.content, "html.parser")
                # Récupération des liens de chaque livre par catégorie
                recuperation_liens_livre1 = soup_livre.find_all("a")
                liste_liens_livres = []
                for recuperation_liens_livre2 in recuperation_liens_livre1:
                    recuperation_liens_livre3 = recuperation_liens_livre2.get("href")
                    #Suppression des caractères ../
                    recuperation_liens_livre4 = re.sub("\../", "", recuperation_liens_livre3)
                    liste_liens_livres.append(recuperation_liens_livre4)

                if recherche_page1:
                    liste_liens_livres2 = liste_liens_livres[54:-1]
                    liste_liens_livres3.append(liste_liens_livres2)


                if not recherche_page1:
                    # Si recherche_page1 = None
                    liste_liens_livres2 = liste_liens_livres[54:]
                    liste_liens_livres3.append(liste_liens_livres2)



#print(liste_liens_livres2)
liste_livre_sans_doublon = []
# Suppressions des doublons
liste_doublons1 = liste_liens_livres3
for liste in liste_doublons1:
    liste_doublons3 = liste
    for liste_doublons2 in liste_doublons3:
        if liste_doublons2 not in liste_livre_sans_doublon:
            liste_livre_sans_doublon.append(liste_doublons2)
            #print(liste_livre_sans_doublon)
nombre_de_livre = len(liste_livre_sans_doublon)
print("Liste de livres sans doublons", liste_livre_sans_doublon)

# Boucle qui m'affiche les liens de chaque livre pour reconstitution du lien et suppression des liens indésirable

liste_clean1 = []
yy = 0
while not yy == nombre_de_livre:
    if yy < nombre_de_livre:
        for liste2 in liste_livre_sans_doublon:
            liste3 = manquant + liste2
            yy = yy + 1
            nombre_de_caractere = len(liste3)
            if nombre_de_caractere == 48:
                print("Suppression d'un mauvais lien ")
            elif nombre_de_caractere > 48:
                liste_clean1.append(liste3)
                print(f"Création d'un lien :{liste3}")
                print(f"Livre N° = {yy}")
                sleep(0.3)






##############################################################################################
# Boucle qui va lister un par un les liens de chaque livre (sans les adresses indésirables)
zz = 0
nombre_de_livre2 = len(liste_clean1)
#liste_clean2 = []
for liste_clean3 in liste_clean1:
    zz = zz + 1

    if zz > nombre_de_livre2:
        print("Téléchargement terminé")
        nom, ext = os.path.splitext(f"{data}/BooksToScrape/Categories")
        dateiso = time.strftime('%Y_%m_%d_%H_%M')
        os.rename(f"{data}/BooksToScrape/Categories", nom + '_' + dateiso + ext)

    page_lien_livre3 = 0
    while not page_lien_livre3 == 200:
        try:
            page_lien_livre4 = requests.get(liste_clean3)
            page_lien_livre3 = page_lien_livre4.status_code

            if page_lien_livre3 == 200:
                print("Ligne 293")

        except:
            print("Problème de connexion, nouvelle tentative dans 15 secondes")
            sleep(15)
        soup_lien_livre4 = BeautifulSoup(page_lien_livre4.content, "html.parser")
        premiere_recuperation_1 = soup_lien_livre4.find_all("td")
        liste_recuperation_1 = []
        product_page_url = [liste_clean3]
        titre_image = product_page_url[37:-11]
        for premiere_recuperation_2 in premiere_recuperation_1:
            liste_recuperation_1.append(premiere_recuperation_2.string)
        universal_product_code = [liste_recuperation_1[0]]
        price_including = [liste_recuperation_1[2]]
        price_excluding = [liste_recuperation_1[3]]
        review_rating = [liste_recuperation_1[-1]]

        # quantite_stock_1 = number_available
        quantite_stock_1 = soup_lien_livre4.find_all("td")
        liste_quantite_stock_1 = []
        for quantite_stock_2 in quantite_stock_1:
            quantite_stock_3 = quantite_stock_2.string
            #quantite_stock_4 = str(quantite_stock_3)
            resultat = ([str(s) for s in re.findall(r"-?\d+\.?\d*", quantite_stock_3)])
            liste_quantite_stock_1.append(resultat)
        number_available = liste_quantite_stock_1[5]

        # description_produit_1 = product_description
        description_produit_1 = soup_lien_livre4.find_all("p")
        liste_description_produit_1 = []
        for description_produit_2 in description_produit_1:
            liste_description_produit_1.append(description_produit_2.get_text())
        product_description = [liste_description_produit_1[3]]
        #print("Ligne 148", product_description)

        sleep(1)
        # title
        title = titre_image

        sleep(1)
        # recuperation_categorie_1 = category
        recuperation_categorie_1 = soup_lien_livre4.find_all("a")
        liste_categorie_1 = []
        for recuperation_categorie_2 in recuperation_categorie_1:
            liste_categorie_1.append(recuperation_categorie_2.string)
        category = [liste_categorie_1[3]]


        sleep(1)
        # lien_image_1 = image_url
        lien_image_1 = soup_lien_livre4.find_all("img")
        liste_lien_image_1 = []
        for lien_image_2 in lien_image_1:
            lien_image_3 = (lien_image_2.get("src"))
            lien_image_4 = re.sub('\../', "", lien_image_3)
            lien_image_5 = url_accueil + lien_image_4
            liste_lien_image_1.append(lien_image_5)
        image_url = [liste_lien_image_1[0]]


        # Création de mon fichier jpeg
        image_url2 = liste_lien_image_1[0]
        category2 = liste_categorie_1[3]
        title3 = titre_image

        z = open(f"{data}/BooksToScrape/Categories/{category2}/Images/{title3}.jpg", "wb")
        reponse2 = 0
        while not reponse2 == 200:
            try:
                reponse = requests.get(image_url2)
                reponse2 = reponse.status_code
                if reponse2 == 200:
                    print("Ligne 371")
            except:
                print("Problème de connexion, nouvelle tentative dans 15 secondes")
                sleep(15)
        z.write(reponse.content)
        z.close()
        #print("Sorite de boucle")

        print(f"Enregistrement des informations du livre '{title3}' dans un fichier au format csv dans le répertoire : {category2} \nEmplacement du fichier csv : {data}/BooksToScrape/Categories/{category2}")


        print("\n \n \n")
        # Création de l'en-tête
        en_tete = ["product_page_url", "universal_product_code(upc)", "title", "price_including_tax",
                   "price_excluding_tax", "number_available", "product_description", "category",
                   "review_rating", "image_url"]
        # Création d'un répertoire image par catégorie

        if os.path.exists(f"{data}/BooksToScrape/Categories/{category2}/output.csv"):
            print()
        else:
            with open(f"{data}/BooksToScrape/Categories/{category2}/output.csv", "w", encoding="utf-8") as fichier_csv:
                writer = csv.writer(fichier_csv, delimiter=";")
                writer.writerow(en_tete)

        # Ajout des données dans le fichier csv
        with open(f"{data}/BooksToScrape/Categories/{category2}/output.csv", "a", encoding="utf8") as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=";")

            for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url in zip(
                    product_page_url, universal_product_code, title, price_including, price_excluding,
                    number_available, product_description, category, review_rating, image_url):
                writer.writerow(
                    [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                     number_available, product_description, category, review_rating, image_url])




