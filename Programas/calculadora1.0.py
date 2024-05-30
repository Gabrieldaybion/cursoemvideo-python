filmes={
    "Drama":['Dois papas','O quarto de Jake','Sempre ao seu lado'],
    "Comedia":["Deadpool","America Pie","O auto da compadecida"],
    "Policial":["Dia de treinamento","Tropa de elite","Osinfiltrados"],
    "Guerra":["Até o ultimo homem","1917","Rambo"]
}

pagina=open("iddaybion.html","w")
pagina.write("""
<html lang="pt-BR">
<head>
    <title>Dicionario de filmes</title>
</head>
<body>
""")
for c,x in filmes.items():
    pagina.write("<h1>%s</h1>"%c)
    for e in x:
        pagina.write("<h1>%s</p>" % e)
pagina.write("""
</body>
</html>
""")
pagina.close()