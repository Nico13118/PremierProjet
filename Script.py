import re
import shutil
import time
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os

url_directory = "https://books.toscrape.com/"
page_directory = requests.get(url_directory)
soup_directory = BeautifulSoup(page_directory.content, "html.parser")
##################################################################################################
# Condition qui permet de contrôler si le répertoire BookToScrape\Catégorie existe ou pas si le fichier existe il sera renommé sous le format d'une date

recherche_fichier_bookstoscrape_categorie = os.path.exists("C:\BooksToScrape\Catégories")
recherche_fichier_bookstoscrape = os.path.exists("C:\BooksToScrape")
if recherche_fichier_bookstoscrape:
    if recherche_fichier_bookstoscrape_categorie:
        # print("Si le fichier Catégories existe")
        shutil.rmtree("C:\BooksToScrape\Catégories")
        print("Création du répertoire Catégories dans C:\BooksToScrape")
        os.mkdir("C:\BooksToScrape\Catégories")

    if not recherche_fichier_bookstoscrape_categorie:
        os.mkdir("C:\BooksToScrape\Catégories")

    #
    # if recherche_fichier_bookstoscrape:
    #     shutil.rmtree("C:\BooksToScrape")
    #     os.mkdir("C:\BooksToScrape")
    #     os.mkdir("C:\BooksToScrape\Catégories")

else:
    print("Création du répertoire BooksToScrape et Catégories")
    os.mkdir("C:\BooksToScrape")
    os.mkdir("C:\BooksToScrape\Catégories")


# Récupération des noms de catégories
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
#Boucle qui va afficher le nom d'une catégorie puis va créer les répertoires un à un dans "Catégories"
nombre_categorie_accueil1 = len(liste_directory_2)
nombre_categorie_accueil2 = nombre_categorie_accueil1 + 1
h, i = 0, 0
while h < nombre_categorie_accueil2:
    h = h + 1
    if h == nombre_categorie_accueil2:
        break
    elif h < nombre_categorie_accueil2:
        nom_categorie_accueil = liste_directory_2[i]
        os.mkdir(f"C:\BooksToScrape\Catégories\{nom_categorie_accueil}")
        i = i + 1



##################################################################################################
# Boucle qui va créer un répertoire Images dans chaque catégorie du répertoire Catégories
nombre_categorie_accueil3 = nombre_categorie_accueil1 + 1
j, k = 0, 0
while j < nombre_categorie_accueil3:
    # if os.path.exists(f"C:\BooksToScrape\Catégories\{nom_categorie_accueil2}\Images"):
    #     break
    j = j + 1
    if j == nombre_categorie_accueil3:
        break

    elif j < nombre_categorie_accueil3:
        nom_categorie_accueil2 = liste_directory_2[k]
        os.mkdir(f"C:\BooksToScrape\Catégories\{nom_categorie_accueil2}\Images")
        k = k + 1


##################################################################################################
##################################################################################################
# Création d'une liste de lien  pour chaque catégorie de la page d'accueil books.toscrape.com
url_accueil = "https://books.toscrape.com/"
page_accueil = requests.get(url_accueil)
soup_accueil = BeautifulSoup(page_accueil.content, "html.parser")
index = "index.html"
books1 = "catalogue/category/books_1/index.html"
global liste_categorie_accueil2
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

global url_category
##################################################################################################
# Création d'une boucle qui va lister une par une les liens de chaque catégorie

#print("Liste des catégories accueil:\n", liste_categorie_accueil2)
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
        print("Ligne 120: Fin du programme")
        nom, ext = os.path.splitext("C:\BooksToScrape\Catégories")
        dateiso = time.strftime('%Y_%m_%d_%H_%M')
        os.rename("C:\BooksToScrape\Catégories", nom + '_' + dateiso + ext)
        break
    #print(url_category)


    ################################################################################################
    page_category = requests.get(url_category)
    soup_category = BeautifulSoup(page_category.content, "html.parser")
    manquant = "https://books.toscrape.com/catalogue/"

    liste_liens_pages = []
    ###########################################################################################
    # Une boucle qui va initialiser un lien par rapport au nombre de pages
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

    # Une boucle qui va lister les url une par une
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
                #print(resultat)


                global recuperation_liens_livre6
                url_livre = resultat
                #print("Ligne 63", url_livre)
                url_livre_fusion = url_livre[0:37]
                page_livre = requests.get(url_livre)
                soup_livre = BeautifulSoup(page_livre.content, "html.parser")
                # Récupération des liens de chaque livre dans une catégorie
                recuperation_liens_livre1 = soup_livre.find_all("a")
                liste_liens_livres = []
                for recuperation_liens_livre2 in recuperation_liens_livre1:
                    recuperation_liens_livre3 = recuperation_liens_livre2.get("href")
                    #Suppression des caractères ../
                    recuperation_liens_livre4 = re.sub("\../", "", recuperation_liens_livre3)
                    # Suppression des liens inutiles ( index.html, books_1/index.html
                    if recuperation_liens_livre4 != "index.html":
                        if recuperation_liens_livre4 != "books_1/index.html":
                            if recuperation_liens_livre4 != "page-1.html":
                                if recuperation_liens_livre4 != "page-2.html":
                                    if recuperation_liens_livre4 != "page-3.html":
                                        if recuperation_liens_livre4 != "page-4.html":
                                            if recuperation_liens_livre4 != "page-5.html":
                                                if recuperation_liens_livre4 != "page-6.html":
                                                    if recuperation_liens_livre4 != "page-7.html":
                                                        if recuperation_liens_livre4 != "page-8.html":

                                                            # Fusion des url
                                                            recuperation_liens_livre5 = url_livre_fusion + recuperation_liens_livre4
                                                            liste_liens_livres.append(recuperation_liens_livre5)

                liste_liens_livres2 = liste_liens_livres[49:]
                #print("Ligne 91", liste_liens_livres2)
                recuperation_liens_livre6 = liste_liens_livres2
                liste_livre_sans_doublon = []

                # Suppressions des doublons
                liste_doublons1 = recuperation_liens_livre6

                for liste_doublons2 in liste_doublons1:
                    if liste_doublons2 not in liste_livre_sans_doublon:
                        liste_livre_sans_doublon.append(liste_doublons2)

                ###################################################################################################
                #print("Une boucle qui va lister les url des livres une par une")
                resultat_livre = len(liste_livre_sans_doublon)

                d, e = 0, 0
                resultat_livre = resultat_livre + 1
                while d < resultat_livre:
                    e = e + 1
                    if e == resultat_livre:
                        break

                    if e < resultat_livre:
                        resultat_livre1 = liste_livre_sans_doublon[d]
                        d = d + 1
                        ############################################################################
                        page_livre2 = requests.get(resultat_livre1)
                        soup_livre2 = BeautifulSoup(page_livre2.content, "html.parser")
                        # Récupération du lien pour un livre
                        product_page_url = [resultat_livre1]
                        #print("Ligne 121", product_page_url)
                        # premiere_recuperation_1 = universal_product_code, price_including, price_excluding, review_rating
                        premiere_recuperation_1 = soup_livre2.find_all("td")
                        liste_recuperation_1 = []
                        for premiere_recuperation_2 in premiere_recuperation_1:
                            liste_recuperation_1.append(premiere_recuperation_2.string)
                        universal_product_code = [liste_recuperation_1[0]]
                        price_including = [liste_recuperation_1[2]]
                        price_excluding = [liste_recuperation_1[3]]
                        review_rating = [liste_recuperation_1[-1]]

                        # quantite_stock_1 = number_available
                        quantite_stock_1 = soup_livre2.find_all("td")
                        liste_quantite_stock_1 = []
                        for quantite_stock_2 in quantite_stock_1:
                            quantite_stock_3 = quantite_stock_2.string
                            #quantite_stock_4 = str(quantite_stock_3)
                            resultat = ([str(s) for s in re.findall(r"-?\d+\.?\d*", quantite_stock_3)])
                            liste_quantite_stock_1.append(resultat)
                        number_available = liste_quantite_stock_1[5]

                        # description_produit_1 = product_description
                        description_produit_1 = soup_livre2.find_all("p")
                        liste_description_produit_1 = []
                        for description_produit_2 in description_produit_1:
                            liste_description_produit_1.append(description_produit_2.string)
                        product_description = [liste_description_produit_1[3]]
                        #print("Ligne 148", product_description)

                        sleep(1)
                        # titre_1 = title
                        titre_1 = soup_livre2.find_all("img")
                        liste_titre_1 = []
                        for titre_2 in titre_1:
                            liste_titre_1.append(titre_2.get("alt"))
                        title1 = liste_titre_1[0]
                        title2 = re.sub('\W', " ", title1)
                        title = [title2]

                        sleep(1)
                        # recuperation_categorie_1 = category
                        recuperation_categorie_1 = soup_livre2.find_all("a")
                        liste_categorie_1 = []
                        for recuperation_categorie_2 in recuperation_categorie_1:
                            liste_categorie_1.append(recuperation_categorie_2.string)
                        category = [liste_categorie_1[3]]





                        sleep(1)
                        # lien_image_1 = image_url
                        lien_image_1 = soup_livre2.find_all("img")
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
                        title3 = title2

                        z = open(f"C:\BooksToScrape\Catégories\{category2}\Images\{title3}.jpg", "wb")
                        reponse = requests.get(image_url2)
                        z.write(reponse.content)
                        z.close()
                    #print("Sorite de boucle")

                        print(f"Enregistrement des informations du livre '{title3}' dans un fichier au format csv dans le répertoire : {category2} \nEmplacement du fichier csv : C:\BooksToScrape\Catégories\{category2}")


                        print("\n \n \n")
                        # Création de l'en-tête
                        en_tete = ["product_page_url", "universal_product_code(upc)", "title", "price_including_tax",
                                   "price_excluding_tax", "number_available", "product_description", "category",
                                   "review_rating", "image_url"]
                        # Création d'un répertoire image par catégorie

                        if os.path.exists(f"C:\BooksToScrape\Catégories\{category2}\output.csv"):
                            print()
                        else:
                            with open(f"C:\BooksToScrape\Catégories\{category2}\output.csv", "w", encoding="utf-8") as fichier_csv:
                                writer = csv.writer(fichier_csv, delimiter=";")
                                writer.writerow(en_tete)

                        # Ajout des données dans le fichier csv
                        with open(f"C:\BooksToScrape\Catégories\{category2}\output.csv", "a", encoding="utf8") as fichier_csv:
                            writer = csv.writer(fichier_csv, delimiter=";")

                            for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url in zip(
                                    product_page_url, universal_product_code, title, price_including, price_excluding,
                                    number_available, product_description, category, review_rating, image_url):
                                writer.writerow(
                                    [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                                     number_available, product_description, category, review_rating, image_url])



