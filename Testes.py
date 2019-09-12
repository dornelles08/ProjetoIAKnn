from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv
import time
import random


def acessarBrowser(dados):
    ritmo = browser.find_element_by_xpath('//*[@id="ritmo"]')
    drible = browser.find_element_by_xpath('//*[@id="drible"]')
    finalizacao = browser.find_element_by_xpath('//*[@id="finalizacao"]')
    defesa = browser.find_element_by_xpath('//*[@id="defesa"]')
    passe = browser.find_element_by_xpath('//*[@id="passe"]')
    fisico = browser.find_element_by_xpath('//*[@id="fisico"]')
    goleiro = browser.find_element_by_xpath('//*[@id="goleiro"]')

    ritmo.send_keys(str(dados[0]))
    drible.send_keys(str(dados[1]))
    finalizacao.send_keys(str(dados[2]))
    defesa.send_keys(str(dados[3]))
    passe.send_keys(str(dados[4]))
    fisico.send_keys(str(dados[5]))
    goleiro.send_keys(str(dados[6]))

    btn = browser.find_element_by_xpath('/html/body/div/div/div[1]/form/button')
    btn.click()

def limparCampus():
    ritmo = browser.find_element_by_xpath('//*[@id="ritmo"]')
    drible = browser.find_element_by_xpath('//*[@id="drible"]')
    finalizacao = browser.find_element_by_xpath('//*[@id="finalizacao"]')
    defesa = browser.find_element_by_xpath('//*[@id="defesa"]')
    passe = browser.find_element_by_xpath('//*[@id="passe"]')
    fisico = browser.find_element_by_xpath('//*[@id="fisico"]')
    goleiro = browser.find_element_by_xpath('//*[@id="goleiro"]')

    ritmo.clear()
    drible.clear()
    finalizacao.clear()
    defesa.clear()
    passe.clear()
    fisico.clear()
    goleiro.clear()

#i = int(input("Número de 1 a 1500: "))

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

browser = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe')

browser.get("http://localhost:8080")
browser.maximize_window()

arq = open('testes.csv', 'r')
dados = list(csv.reader(arq))
arq.close()

for j in range(1):
    i = random.randint(1, 1500)
    acessarBrowser(dados[i])
    time.sleep(1)
    #limparCampus()
    print("Posiçao Esperada: {}".format(dados[i][7]))
    print("Overrall Esperado: {}".format(dados[i][8]))
    input()


