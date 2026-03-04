import pyautogui
import time
#pyautogui.click->Clica
#pyautogui.write->escreve
#pyautogui.press->Aperta uma tecla
#pyautogui.hotkey->aperta um atalho

pyautogui.PAUSE=1
link= "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Passo 1: Abrir o navegador
pyautogui.click(x=167, y=753)
pyautogui.write("Chrome")
pyautogui.press("Enter")
time.sleep(2)
#Passo 2:Entrar no site
pyautogui.click(x=166, y=59)
pyautogui.write(link)
pyautogui.press("Enter")
time.sleep(5)
#Passo 3:Logar no site
pyautogui.press("Tab")
pyautogui.write("Grazi")
pyautogui.press("Tab")
pyautogui.write("Linda")
pyautogui.press("Tab")
pyautogui.press("Enter")
time.sleep(3)
#Passo 4:Importar a base de dados
import pandas

tabela= pandas.read_csv("produtos.csv")

for linha in tabela.index:
#Passo 5: Cadastrar um produto
#codigo
    pyautogui.click(x=291, y=247)
    codigo= str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("Tab")

    #Marca
    marca= str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("Tab")

    #tipo
    tipo= str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("Tab")

    #categoria
    categoria= str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("Tab")

    #preço
    preco= str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("Tab")

    #custo
    custo= str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("Tab")
    #Observação
    
    obs= str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("Tab")

    pyautogui.press("Enter") #Clicar no enivar
    pyautogui.scroll(5000)
    time.sleep(2)
     #Voltar para o inicio da tela
     #Scroll negativo desce a pagina e o positivo sobe

#Passo 6: Repetir o processo com cada produto
