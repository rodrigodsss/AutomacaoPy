# Passo a Passo da projeto
# Passo 1: Entrar no sistema da empresa
#   https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 0.5

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Dar uma pausa um pouco maior (3 segundos)
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=450, y=377)
pyautogui.write("emailgenerico@gmail.com")

#Escrever a senha
pyautogui.press("tab")
pyautogui.write("emaigenerico123321")

#Clicar no botão login
pyautogui.click(x=650, y=533)
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)


# Passo 4: Cadastrar 1 produto
#Para cada linha da minha tabela
for linha in tabela.index:

#Clicar no primeiro campo
    pyautogui.click(x=505, y=262)

    #Codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #Marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    #Tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #Categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #Preço unitário do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #Custo do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #OBS do produto
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    #Enviar
    pyautogui.press("enter")
    pyautogui.scroll("3700")

    # Passo 5: Repetir o processo de cadastro até acabar a base de dados

