import pyautogui
import time
import pandas

# pyautogui.write -> escrever texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar tecla
# pyautogui.hotkey -> apertar um atalho
# pyautogui.PAUSE = 1

tabela = pandas.read_csv("produtos.csv")

print(tabela)

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("Opera")

pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

time.sleep(1)

pyautogui.click(x=534, y=391)

pyautogui.write("randa4238@uorak.com")

pyautogui.press("tab")

pyautogui.write("minha senha")

pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(2)

for linha in tabela.index:

    pyautogui.click(x=586, y=275)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press("obs")

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)