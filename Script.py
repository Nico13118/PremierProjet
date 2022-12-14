import re
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
url_accueil = "https://books.toscrape.com/"
url = "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Création de l'en-tête
en_tete = ["product_page_url", "universal_product_code(upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
with open("output.csv", "w", encoding="utf-8") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=";")
    writer.writerow(en_tete)

# Récupération d'un lien d'un livre
product_page_url = [url]

# premiere_recuperation_1 = universal_product_code, price_including, price_excluding, review_rating
premiere_recuperation_1 = soup.find_all("td")
liste_recuperation_1 = []
for premiere_recuperation_2 in premiere_recuperation_1:
    liste_recuperation_1.append(premiere_recuperation_2.string)
universal_product_code = [liste_recuperation_1[0]]
price_including = [liste_recuperation_1[2]]
price_excluding = [liste_recuperation_1[3]]
review_rating = [liste_recuperation_1[-1]]

# quantite_stock_1 = number_available
quantite_stock_1 = soup.find_all("td")
liste_quantite_stock_1 = []
for quantite_stock_2 in quantite_stock_1:
    quantite_stock_3 = quantite_stock_2.string
    quantite_stock_4 = str(quantite_stock_3)
    resultat = ([str(s) for s in re.findall(r"-?\d+\.?\d*", quantite_stock_3)])
    liste_quantite_stock_1.append(resultat)
number_available = liste_quantite_stock_1[5]

# description_produit_1 = product_description
description_produit_1 = soup.find_all("p")
liste_description_produit_1 = []
for description_produit_2 in description_produit_1:
    liste_description_produit_1.append(description_produit_2.string)
product_description = [liste_description_produit_1[3]]

sleep(2)
# titre_1 = title
titre_1 = soup.find_all("img")
liste_titre_1 = []
for titre_2 in titre_1:
    liste_titre_1.append(titre_2.get("alt"))
title = [liste_titre_1[0]]

sleep(2)
#recuperation_categorie_1 = category
recuperation_categorie_1 = soup.find_all("a")
liste_categorie_1 = []
for recuperation_categorie_2 in recuperation_categorie_1:
    liste_categorie_1.append(recuperation_categorie_2.string)
category = [liste_categorie_1[3]]

sleep(2)
# lien_image_1 = image_url
lien_image_1 = soup.find_all("img")
liste_lien_image_1 = []
for lien_image_2 in lien_image_1:
    lien_image_3 = (lien_image_2.get("src"))
    lien_image_4 = re.sub("\../", "", lien_image_3)
    lien_image_5 = url_accueil + lien_image_4
    liste_lien_image_1.append(lien_image_5)
image_url = [liste_lien_image_1[0]]

with open("output.csv", "a", encoding="utf8") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=";")

    for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url in zip(product_page_url, universal_product_code, title, price_including, price_excluding, number_available, product_description, category, review_rating, image_url):
        writer.writerow([product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url])


