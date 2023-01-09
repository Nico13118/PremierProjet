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
global url_category, page_accueil, url_accueil, page_directory, page_category, reponse, liste_categorie_accueil2, recuperation_liens_livre6, page_livre, page_livre2, page_lien_livre2, page_lien_livre4, url_directory

##################################################################################################
# Condition qui permet de contrôler l'existance du répertoire BookToScrape et Categories
data = os.getcwd()
recherche_fichier_bookstoscrape = os.path.exists(f"{data}/BooksToScrape")
recherche_fichier_bookstoscrape_categories = os.path.exists(f"{data}/BooksToScrape/Database")
print("Vérification de la présence du répertoire BooksToScrape et Database")
sleep(2)
if recherche_fichier_bookstoscrape:
    if recherche_fichier_bookstoscrape_categories:
        # print("Si le fichier Catégories existe")
        print("Suppression du répertoire Database\n")
        sleep(2)
        shutil.rmtree(f"{data}/BooksToScrape/Database")
        print(f"Création du répertoire Database dans {data}/BooksToScrape\n")
        sleep(2)
        os.mkdir(f"{data}/BooksToScrape/Database")

    if not recherche_fichier_bookstoscrape_categories:
        print(f"Création du répertoire Database dans {data}/BooksToScrape\n")
        sleep(2)
        os.mkdir(f"{data}/BooksToScrape/Database")


else:
    print("Création du répertoire BooksToScrape et Database\n")
    sleep(2)
    os.mkdir(f"{data}/BooksToScrape")
    os.mkdir(f"{data}/BooksToScrape/Database")

##################################################################################################

# Récupération du nom de chaque catégorie (Exemple : Travel ...)
page_directory2 = 0
url_directory = "https://books.toscrape.com/"
while not page_directory2 == 200:
    try:
        page_directory = requests.get(url_directory)
        page_directory2 = page_directory.status_code
        if page_directory2 == 200:
            print(f"Test de connexion sur le lien {url_directory}: OK\n")

    except:
        print("Problème de connexion, nouvelle tentative dans 15 secondes\n")
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



###################################################################################################
#Boucle qui va créer un répertoire pour chaque catégorie et un répertoire Images
print("Création d'un répertoire portant le nom d'une catégorie et ajout du répertoire Images\n")
nombre_categorie_accueil1 = len(liste_directory_2)
nombre_categorie_accueil2 = nombre_categorie_accueil1 + 1
h, i = 0, 0
while h < nombre_categorie_accueil2:
    h = h + 1
    if h == nombre_categorie_accueil2:
        break
    elif h < nombre_categorie_accueil2:
        nom_categorie_accueil = liste_directory_2[i]
        os.mkdir(f"{data}/BooksToScrape/Database/{nom_categorie_accueil}")
        os.mkdir(f"{data}/BooksToScrape/Database/{nom_categorie_accueil}/Images")
        i = i + 1
############################################################################################
# Création d'un lien pour chaque catégorie de la page d'accueil bookstoscrape.com
print("Création d'un lien par catégorie en cours...\n")
index = "index.html"
books1 = "catalogue/category/books_1/index.html"


categorie_page_accueil1 = directory_categorie_1

liste_categorie_accueil = []
for categorie_page_accueil2 in categorie_page_accueil1:
    categorie_page_accueil3 = categorie_page_accueil2.get("href")
    # Une condition, qui ne récupère pas les liens index et books1
    if categorie_page_accueil3 != index:
        if categorie_page_accueil3 != books1:
            # Concaténation de la variable url_directory et categorie_page_accueil3
            categorie_page_accueil4 = url_directory + categorie_page_accueil3
            liste_categorie_accueil.append(categorie_page_accueil4)
liste_categorie_accueil2 = liste_categorie_accueil[:50]
print("Fin de la création d'un lien pour chaque catégorie\n")

##################################################################################################
# Une boucle qui va lister les liens de chaque catégorie une par une
nombre_de_categorie1 = len(liste_categorie_accueil2)
print(f"Nombre de catégorie : {nombre_de_categorie1}")

f, g = 0, 0
nombre_de_categorie2 = nombre_de_categorie1 + 1
while g < nombre_de_categorie2:
    g = g + 1
    if g < nombre_de_categorie2:
        url_category = liste_categorie_accueil2[f]
        f = f + 1
    if g == nombre_de_categorie2:
        print("Fin du test de connexion\n")
        break



    ################################################################################################


    # Test de connexion d'une url
    page_category2 = 0
    while not page_category2 == 200:
        try:
            print(f"\nTest de connexion pour l'url :\n{url_category} ")
            page_category = requests.get(url_category)
            page_category2 = page_category.status_code
            if page_category2 == 200:
                """"""
        except:
            print("Problème de connexion, nouvelle tentative dans 15 secondes")
            sleep(15)


    soup_category = BeautifulSoup(page_category.content, "html.parser")
    liste_liens_pages = []
    # Si la recherche dans la balise "li" class_="current" ne trouve pas un nombre de
    # pages, recherche_page1 me retourne la valeur None.
    recherche_page1 = soup_category.find("li", class_="current")
    # Si recherche_page1 est vrai alors supprime les 10 derniers caractère de url_category
    # Resultat = https://books.toscrape.com/catalogue/category/books/mystery_3/
    if recherche_page1:
        print(f"Test OK, cette url contient plusieurs pages")
        modif_url_category = url_category[:-10]
        recherche_page2 = recherche_page1.get_text()
        #Suppression des espaces (\n)
        recherche_page3 = recherche_page2.strip()
        # Suppressions des caractères pour garder le nombre de pages
        recherche_page4 = recherche_page3[10:]
        recherche_page4 = int(recherche_page4)
        a = 0
        # La boucle suivante
        while a != recherche_page4:
            a = a + 1
            nouvelle_adresse = f"{modif_url_category}page-{a}.html"
            print(nouvelle_adresse)
            liste_liens_pages.append(nouvelle_adresse)

    if not recherche_page1:
        # Si recherche_page1 = None alors ajoute l'adresse directement dans la liste
        print("Test OK, cette url ne contient pas de page suplémentaire \n")
        liste_liens_pages.append(url_category)


    # Une boucle qui va lister une par une les url par rapport au nombre de pages
    # Exemple : https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html
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
                page_livre2 = 0
                while not page_livre2 == 200:
                    try:
                        page_livre = requests.get(url_livre)
                        page_livre2 = page_livre.status_code
                        if page_livre2 == 200:
                            """print("Ligne 227")"""

                    except:
                        print("Problème de connexion, nouvelle tentative dans 15 secondes\n")
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

                liste_liens_livres2 = liste_liens_livres[54:]
                liste_liens_livres3.append(liste_liens_livres2)



# Création d'une liste sans doublons
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


# Création d'un lien pour chaque livre et suppression des liens indésirables
print("Création d'un lien pour chaque livre et suppression des liens indésirables\n")
liste_clean1 = []
yy = 0
while not yy == nombre_de_livre:
    if yy < nombre_de_livre:
        for liste2 in liste_livre_sans_doublon:
            liste3 = manquant + liste2
            yy = yy + 1
            nombre_de_caractere = len(liste3)
            if nombre_de_caractere == 48:
                print(f"Suppression d'un mauvais lien : {liste3}")

            elif nombre_de_caractere > 48:
                liste_clean1.append(liste3)

                print(f"Création d'un lien :{liste3}\n")
                sleep(0.1)


##############################################################################################
# Boucle qui va lister un par un les liens de chaque livre (sans les adresses indésirables)
# Mise en place d'une condition dans la boucle while qui renomme le répertoire Database
# lorsqu'il a fini tous les livres et met fin au programme
nombre_de_livre2 = len(liste_clean1)
xx = nombre_de_livre2 + 1
zz = 0

print("Début d'intégration des données")


while not zz == xx:
    if zz == nombre_de_livre2:
        sleep(5)
        nom, ext = os.path.splitext(f"{data}/BooksToScrape/Database")
        sleep(5)
        dateiso = time.strftime('%Y_%m_%d_%H_%M')
        sleep(5)
        os.rename(f"{data}/BooksToScrape/Database", nom + '_' + dateiso + ext)
        print("Fin du téléchargement")
        break
    elif zz < nombre_de_livre2:
        for liste_clean3 in liste_clean1:
            if zz < nombre_de_livre2:
                zz = zz + 1
                page_lien_livre3 = 0
                while not page_lien_livre3 == 200:
                    try:
                        page_lien_livre4 = requests.get(liste_clean3)
                        page_lien_livre3 = page_lien_livre4.status_code

                        if page_lien_livre3 == 200:
                            """print()"""
                    except:
                        print("Problème de connexion, nouvelle tentative dans 15 secondes")
                        sleep(15)


                    soup_lien_livre4 = BeautifulSoup(page_lien_livre4.content, "html.parser")
                    premiere_recuperation_1 = soup_lien_livre4.find_all("td")
                    # Récupération de product_page_url et title
                    product_page_url = [liste_clean3]
                    titre_image = liste_clean3[37:-11]
                    title = [titre_image]

                    # Récupération universal_product_code, price_including
                    # price_excluding, review_rating
                    liste_recuperation_1 = []
                    for premiere_recuperation_2 in premiere_recuperation_1:
                        liste_recuperation_1.append(premiere_recuperation_2.string)
                    universal_product_code = [liste_recuperation_1[0]]
                    price_including = [liste_recuperation_1[2]]
                    price_excluding = [liste_recuperation_1[3]]
                    review_rating = [liste_recuperation_1[-1]]

                    # Récupération number_available
                    quantite_stock_1 = soup_lien_livre4.find_all("td")
                    liste_quantite_stock_1 = []
                    for quantite_stock_2 in quantite_stock_1:
                        quantite_stock_3 = quantite_stock_2.string
                        #quantite_stock_4 = str(quantite_stock_3)
                        resultat = ([str(s) for s in re.findall(r"-?\d+\.?\d*", quantite_stock_3)])
                        liste_quantite_stock_1.append(resultat)
                    number_available = liste_quantite_stock_1[5]

                    # Récupération product_description
                    description_produit_1 = soup_lien_livre4.find_all("p")
                    liste_description_produit_1 = []
                    for description_produit_2 in description_produit_1:
                        liste_description_produit_1.append(description_produit_2.get_text())
                    product_description = [liste_description_produit_1[3]]




                    # Récupération category
                    recuperation_categorie_1 = soup_lien_livre4.find_all("a")
                    liste_categorie_1 = []
                    for recuperation_categorie_2 in recuperation_categorie_1:
                        liste_categorie_1.append(recuperation_categorie_2.string)
                    category = [liste_categorie_1[3]]

                    # Récupération image_url
                    lien_image_1 = soup_lien_livre4.find_all("img")
                    liste_lien_image_1 = []
                    for lien_image_2 in lien_image_1:
                        lien_image_3 = (lien_image_2.get("src"))
                        lien_image_4 = re.sub('\../', "", lien_image_3)
                        lien_image_5 = url_directory + lien_image_4
                        liste_lien_image_1.append(lien_image_5)
                    image_url = [liste_lien_image_1[0]]

                    # Création de mon fichier jpeg
                    image_url2 = liste_lien_image_1[0]
                    category2 = liste_categorie_1[3]
                    title3 = titre_image

                    z = open(f"{data}/BooksToScrape/Database/{category2}/Images/{title3}.jpg", "wb")
                    reponse2 = 0
                    while not reponse2 == 200:
                        try:
                            reponse = requests.get(image_url2)
                            reponse2 = reponse.status_code
                            if reponse2 == 200:
                                """print("Ligne 371")"""
                        except:
                            print("Problème de connexion, nouvelle tentative dans 15 secondes")
                            sleep(15)
                    z.write(reponse.content)
                    z.close()
                    #print("Sorite de boucle")

                    print(f"Enregistrement des informations du livre '{title3}' dans un fichier au format csv dans le répertoire : {category2} \nEmplacement du fichier csv : {data}/BooksToScrape/Database/{category2}")


                    print("\n \n \n")
                    # Création de l'en-tête
                    en_tete = ["product_page_url", "universal_product_code(upc)", "title", "price_including_tax",
                               "price_excluding_tax", "number_available", "product_description", "category",
                               "review_rating", "image_url"]

                    # Une condition qui controle si le fichier csv existe
                    if os.path.exists(f"{data}/BooksToScrape/Database/{category2}/output.csv"):
                        print()
                    else:
                        with open(f"{data}/BooksToScrape/Database/{category2}/output.csv", "w", encoding="utf-8") as fichier_csv:
                            writer = csv.writer(fichier_csv, delimiter=";")
                            writer.writerow(en_tete)

                    # Ajout des données dans le fichier csv
                    with open(f"{data}/BooksToScrape/Database/{category2}/output.csv", "a", encoding="utf-8") as fichier_csv:
                        writer = csv.writer(fichier_csv, delimiter=";")

                        for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, \
                                product_description, category, review_rating, image_url in zip(
                                product_page_url, universal_product_code, title, price_including, price_excluding,
                                number_available, product_description, category, review_rating, image_url):
                            writer.writerow(
                                [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                                 number_available, product_description, category, review_rating, image_url])
            elif zz == nombre_de_livre2:
                break





