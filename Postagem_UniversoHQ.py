import requests
import re

print('VERIFICAÇÃO DE POSTAGENS DE NOTÍCIAS NO SITE UNIVERSO HQ')

page = 1
verif = None
data = input('Digite a data de notícia que deseja verificar, no formato dd/mm/aaaa: ')

while (page <= 3):
    post = requests.get('http://www.universohq.com/category/noticias/page/' + str (page))
    verif = re.search(data, post.text)
    if (verif):
        break
    page = page + 1
if (verif):
    print('Há postagem do dia escolhido nas três primeiras páginas do blog')
else:
    print ('Não há postagem do dia escolhido nas três primeiras páginas do blog')

