import re
import requests


url = input('Por favor, informe o link  desejado: ') 
print(re.match(r'((http|https)://)?(.*)\.wikipedia\.org/wiki/.*',url)) 
r= requests. get(url) 
html=r.text.encode("utf8") 

checar_imagens=[] 
checar_artigos=[] #lista vazia para verificação de repetição
checar_indice=[]

escolha=True
while escolha:
    print ("""""
    1.índice
    2.imagens
    3.links para artigos wiki
    4. Sair
    """"")
    escolha=input("O que deseja analisar?") 
    if escolha=="1":

        indice = str(re.findall(r'\w\=\"tocnumber\"\>(\d|\d.\d)</span> <span class\=\"toctext\"\>(.*?)\<\/',html.decode("utf8"), flags= re.DOTALL)) #
        topico=re.findall(r'(\d|\d.\d)(.*?)', indice)
        print(indice)
        for link in topico:
            if link not in checar_indice: 
                checar_indice.append(link)
        print(link)
        
    
    elif escolha=="2":
        imagens= re.findall("([\w]*)\.(jpg|png|jpeg|JPG|svg)?\/" ,html.decode("utf-8")) #encontra todas as imagens de quaisquer tipo e #checar se há repetição
        for link in imagens:
            if link not in checar_imagens:
             checar_imagens.append(link)
             print(link)
        
    
    elif escolha=="3":
        

        bodyArticle = str(re.findall(r'<div class="mw-parser-output">(.*?)<div id="catlinks".*?>', html.decode("utf8"), flags=re.DOTALL))

        artigos_wiki = re.findall(r'\<a href\=\"(/wiki/.*?")', bodyArticle)
        for link in artigos_wiki:
                 if link not in checar_artigos:
                    checar_artigos.append(link)
                    print(link) 
    elif escolha== "4" :
        print('encerrando')
        break

#https://pt.wikipedia.org/wiki/Alan_Turing
#https://pt.wikipedia.org/wiki/Aut%C3%B4mato