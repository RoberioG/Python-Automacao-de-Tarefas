
import pyautogui as py
import pandas
import time 


py.PAUSE = 1
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

py.press("win")
py.write("chrome")
py.press("enter")


time.sleep(3)

py.write(site)
py.press("enter")

time.sleep(3)

py.press("tab")
py.write("email@email.com")
py.press("tab")
py.write("senha123")
py.press("enter")

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    py.click(390, 256)

    codigo = tabela.loc[linha, "codigo"]
    py.write(codigo)
    py.press("tab")

    
    py.write(tabela.loc[linha, "marca"])
    py.press("tab")


    py.write(tabela.loc[linha, "tipo"])
    py.press("tab")


    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")


    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")


    py.write(str(tabela.loc[linha, "custo"]))
    py.press("tab")

    if not pandas.isna(tabela.loc[linha, "obs"]):
        py.write(tabela.loc[linha, "obs"])
    py.press("tab")

    py.press("enter")
    py.scroll(1000)