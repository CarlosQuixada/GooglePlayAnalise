from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://play.google.com/store/apps/details?id=com.supercell.clashroyale")
soup = BeautifulSoup(page.content, 'html.parser')
reviews = soup.select(".single-review")

autores = []
datas = []
notas = []
commentarios = []

for review in reviews:
    autores.append(review.select(".review-info .author-name")[0].get_text())
    datas.append(review.select(".review-info .review-date")[0].get_text())
    nota = review.select(".review-info-star-rating .tiny-star")[0]
    notas.append(nota['aria-label'])
    commentarios.append(review.select(".review-body")[0].get_text())

dados = pd.DataFrame({
    "autor":autores,
    "nota":notas,
    "data":datas,
    "comentario":commentarios
})

dados.to_csv("clash_royale.csv",index=False)