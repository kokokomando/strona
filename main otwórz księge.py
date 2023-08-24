from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import codecs
import os
import sys
import time
import pathlib
import ctypes
import psutil
import win32com.client
import win32gui
import subprocess
import signal
import atexit
import execel

def mark_as_busy():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    status_file = os.path.join(script_dir, 'status.txt')
    with open(status_file, 'w') as file:
        file.write('busy')

def mark_as_available():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    status_file = os.path.join(script_dir, 'status.txt')
    with open(status_file, 'w') as file:
        file.write('available')

def mark_as_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    status_file = os.path.join(script_dir, 'status.txt')
    with open(status_file, 'w') as file:
        file.write('off')




def cleanup():
    PROCNAME = "EXCEL.EXE"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()
    PROCNAME2 = "WINWORD.EXE"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME2:
            proc.kill()
    #Signal
    Signal = 'Signal.xlsm'
    Signallocation = (pathlib.Path().absolute())
    deleteSignal = (os.path.join(Signallocation, Signal))
    if os.path.isfile('signal.xlsm') == True:
        os. remove(deleteSignal)
        
    Signal1 = 'Signal.docx'
    Signallocation1 = (pathlib.Path().absolute())
    deleteSignal1 = (os.path.join(Signallocation1, Signal1))
    if os.path.isfile('Signal.docx') == True:
        os. remove(deleteSignal1)

    Signal11 = 'Sprzeda¿ Lokalu1.docx'
    Signall1ocation1 = (pathlib.Path().absolute())
    deleteSignal11 = (os.path.join(Signallocation1, Signal11))
    if os.path.isfile('Sprzeda¿ Lokalu1.docx') == True:
        os. remove(deleteSignal11)


    #zmienić cleanupa jak dodam halo nowe
    halo = 'UmowaSprzedaży.docx'
    halo1ocation1 = (pathlib.Path().absolute())
    deletehalo = (os.path.join(halo1ocation1, halo))
    if os.path.isfile('UmowaSprzedaży.docx') == True:
        os. remove(deletehalo)

    
    przetwarzane = 'plain_text.txt'
    Signallocation1 = (pathlib.Path().absolute())
    deleteprzetwarzane = (os.path.join(Signallocation1, przetwarzane))
    if os.path.isfile('plain_text.txt') == True:
        os. remove(deleteprzetwarzane)


    przetwarzane = 'przetwarzane.txt'
    Signallocation1 = (pathlib.Path().absolute())
    deleteprzetwarzane = (os.path.join(Signallocation1, przetwarzane))
    if os.path.isfile('przetwarzane.txt') == True:
        os. remove(deleteprzetwarzane)
    
     
    #księgi

    #Lokalowa
    for x in range (0, 5):
        page_lokal = "page" + str(x) + ".html"
        page_lokal_location = (pathlib.Path().absolute())
        deletepage_lokal = (os.path.join(page_lokal_location, page_lokal))
        if os.path.isfile(page_lokal) == True:
            os. remove(deletepage_lokal)


            #LokalowaPDF
    for x in range (0, 5):
        page_lokal = "page" + str(x) + ".pdf"
        page_lokal_location = (pathlib.Path().absolute())
        deletepage_lokal = (os.path.join(page_lokal_location, page_lokal))
        if os.path.isfile(page_lokal) == True:
            os. remove(deletepage_lokal)

    #MacierzPDF
    for x in range (0, 5):
        page_macierz = "pagemacierz" + str(x) + ".html"
        page_macierz_location = (pathlib.Path().absolute())
        delete_macierz = (os.path.join(page_macierz_location, page_macierz))
        if os.path.isfile(page_macierz) == True:
            os. remove(delete_macierz)


    page_macierz = "KWmacierz.pdf"
    page_macierz_location = (pathlib.Path().absolute())
    delete_macierz = (os.path.join(page_macierz_location, page_macierz))
    if os.path.isfile(page_macierz) == True:
        os. remove(delete_macierz)

    page_lokal = "KWlokal.pdf"
    page_lokal_location = (pathlib.Path().absolute())
    deletepage_lokal = (os.path.join(page_lokal_location, page_lokal))
    if os.path.isfile(page_lokal) == True:
        os. remove(deletepage_lokal)


    for x in range (0, 5):
        page_macierz = "pagemacierz" + str(x) + ".pdf"
        page_macierz_location = (pathlib.Path().absolute())
        delete_macierz = (os.path.join(page_macierz_location, page_macierz))
        if os.path.isfile(page_macierz) == True:
            os. remove(delete_macierz)

            
    #plaintext
    
    plain_txt = "plain_text.txt"
    plain_macierz = "plain_textmacierz.txt"
    location = (pathlib.Path().absolute())
    delete_txt = (os.path.join(location, plain_txt))
    delete_macierz = (os.path.join(location, plain_macierz))
    if os.path.isfile(plain_txt) == True:
        os. remove(delete_txt)
    if os.path.isfile(plain_macierz) == True:
        os. remove(delete_macierz)

cleanup()




file_path = os.path.realpath(__file__)
AppData_path = os.path.join(os.path.dirname(file_path), "AppData", "Czyta")




stop_flag = False

def czyta():   
        

    while not os.path.isfile('przetwarzane.txt') == True:
        print("czekam")
        time.sleep(3)  # Wait for 1 second before checking again
        
    try:
        
        locate_python = sys.exec_prefix
        mark_as_busy()
        restart = False
        with open('done.txt', "r") as file:
            file_content = file.readlines()
        
        file_content = [line.strip() for line in file_content]
        print("done1")
        print(file_content)
        # file content to lista z done, poniżej sprawdza czy było
        
       


        with open('przetwarzane.txt', "r") as file1:
            file_content1 = file1.readlines()
        
            file_content1 = [line.strip() for line in file_content1]
            
        # file content to lista przetwarzane.txt
        
        print("przetwarzane")
        print(file_content1)
        print("podziel")
        
        # inp 0 to do porównania czy było już

        inp0 = file_content1[0]
        inp1 = file_content1[1]
        print(inp0)
        
        if inp0 in file_content:
            print("To już było, pass")
            pass
        else:
            

            # inp 1 to NUMER sądu np 2 to numer KW
            inp1 = file_content1[1]
            inp2 = file_content1[2]
            print(inp1)
            print(inp2)
            

             
            numerwydz = inp1
            srodek = inp2
            wagi = [1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7]

            slownik_znakow = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                   '6': 6, '7': 7,
                   '8': 8, '9': 9,
                   'X': 10, 'A': 11, 'B': 12, 'C': 13, 'D': 14,
                   'E': 15, 'F': 16,
                   'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21,
                   'L': 22, 'M': 23,
                   'N': 24, 'O': 25, 'P': 26, 'R': 27, 'S': 28,
                   'T': 29, 'U': 30,
                   'W': 31, 'Y': 32, 'Z': 33}

            KWtest = inp1 + srodek

            KW2 = KWtest.replace("/","")

            char_list = [char for char in KW2]

            print(char_list)

            replaced_list = [slownik_znakow[char] if char in slownik_znakow else char for char in char_list]
            print(replaced_list)
            numbers = replaced_list

            multiplied_list = [num * weight for num, weight in zip(numbers, wagi)]

            total = sum(multiplied_list)

            kontrolna = total % 10

            inp3 = kontrolna
                    
            with open('przetwarzane.txt', "a") as file:
                file.write(str(inp3) + '\n')
            
            
            print(inp1)
            print(inp2)
            print(inp3)

            atexit.register(mark_as_off)    
            
            
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-blink-features=AutomationControlled')
            

            driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
            driver.get(
                "https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/pokazWydruk")
            inputWydzialu = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "kodWydzialuInput"))
            )
            inputWydzialu.send_keys(inp1)
            inputNrKsiegi = driver.find_element(by=By.ID, value="numerKsiegiWieczystej")
            inputNrKsiegi.send_keys(inp2)
            inputCyfraKontrolna = driver.find_element(by=By.ID, value="cyfraKontrolna")
            inputCyfraKontrolna.send_keys(inp3)
            buttonWyszukaj = driver.find_element(by=By.ID, value="wyszukaj")
            buttonWyszukaj.click()


            try:
                buttonZwyklyWydruk = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "przyciskWydrukZwykly"))
                )
            except:
                print("Nie znaleziono księgi wieczystej")
                with open('done.txt', 'a') as file:
                    # Write each element of the list on a new lin             
                        file.write(inp0 + '\n')

                
            buttonZwyklyWydruk.click()
            tableNawigacja = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "contentDzialu"))
            )
            tableDzialy = driver.find_element(by=By.ID, value="nawigacja")
            size = len(tableDzialy.find_elements(by=By.CSS_SELECTOR, value='tr td'))
            for x in range(size):
                if x == 0:
                    text = driver.find_element(by=By.TAG_NAME, value="body").text
                    n = os.path.join(os.getcwd(), f'plain_text.txt')
                    f = codecs.open(n, "w", "utf−8")
                    f.write(text)

                
                                        
                with open('plain_text.txt', 'r', encoding='utf-8') as f:
                # Read the contents of the file
                    text = f.read()

                lines = text.split('\n')

                # Get the lines after the third and fourth 'enter'
                start = 2  # line number after which to start capturing text
                end = 3    # line number after which to stop capturing text
                captured_lines = lines[start:end]


                captured_text = '\n'.join(captured_lines)


                print(captured_text)



                
                tableDzialy = driver.find_element(by=By.ID, value="nawigacja")
                table = tableDzialy.find_elements(by=By.CSS_SELECTOR, value='tr td')
                table2 = table[x].find_elements(by=By.CSS_SELECTOR, value='form input')
                button = table2[-1]
                button.submit()
                sleep(1)
                n = os.path.join(os.getcwd(), f'page{x}.html')
                f = codecs.open(n, "w", "utf−8")
                h = driver.page_source
                f.write(h)





            driver.quit()
            
    except:
            print("Wywaliło przy pierwszym otwarciu, dodaje do done:")
            brakKW()
            

    if "LOKAL STANOWIĄCY ODRĘBNĄ NIERUCHOMOŚĆ" in captured_text:
                      
        try:
            driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
            now = os.getcwd()
            print(now)
            print(now+"\page1.html")
            driver.get(now+"\page1.html")
            try:          
                text = driver.find_element(By.XPATH, '//*[@id="contentDzialu"]/table[2]/tbody/tr[7]/td[4]').text
            except:
                text = driver.find_element(By.XPATH, '//*[@id="contentDzialu"]/table[2]/tbody/tr[8]/td[4]').text

            print(len(text))
            
            

            if len(text) < 19:
                with open('przetwarzane.txt', "r") as file1:
                    file_content1 = file1.readlines()
        
                file_content1 = [line.strip() for line in file_content1]

                numerwydz = inp1
                print(numerwydz)
                srodek1 = text.replace(" ", "")
                srodek = srodek1.replace("/", "")
                
               
                print(srodek)
                wagi = [1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7]

                slownik_znakow = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7,
               '8': 8, '9': 9,
               'X': 10, 'A': 11, 'B': 12, 'C': 13, 'D': 14,
               'E': 15, 'F': 16,
               'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21,
               'L': 22, 'M': 23,
               'N': 24, 'O': 25, 'P': 26, 'R': 27, 'S': 28,
               'T': 29, 'U': 30,
               'W': 31, 'Y': 32, 'Z': 33}

                KWtest = inp1 + srodek

                KW2 = KWtest.replace("/","")

                char_list = [char for char in KW2]

                print(char_list)

                replaced_list = [slownik_znakow[char] if char in slownik_znakow else char for char in char_list]
                print(replaced_list)
                numbers = replaced_list

                multiplied_list = [num * weight for num, weight in zip(numbers, wagi)]

                total = sum(multiplied_list)

                kontrolna = total % 10

                macierz1 = str(inp1) + str(srodek1) + str(kontrolna)

                print(macierz1)
                macierz = macierz1.split("/",)
                
            else:
                
                macierz = text.split(" / ",)
            


            KR1P = macierz[0]
            print(KR1P)
            jeden = macierz[1]
            kontrolna = macierz[2]





            print(KR1P)
            print(jeden)
            print(kontrolna)
            driver.get(
                "https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/pokazWydruk")
            inputWydzialu = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "kodWydzialuInput"))
            )
            inputWydzialu.send_keys(KR1P)
            inputNrKsiegi = driver.find_element(by=By.ID, value="numerKsiegiWieczystej")
            inputNrKsiegi.send_keys(jeden)
            inputCyfraKontrolna = driver.find_element(by=By.ID, value="cyfraKontrolna")
            inputCyfraKontrolna.send_keys(kontrolna)
            buttonWyszukaj = driver.find_element(by=By.ID, value="wyszukaj")
            buttonWyszukaj.click()
            buttonZwyklyWydruk = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "przyciskWydrukZwykly"))
            )
            buttonZwyklyWydruk.click()
            tableNawigacja = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "contentDzialu"))
            )

            tableDzialy = driver.find_element(by=By.ID, value="nawigacja")
            size = len(tableDzialy.find_elements(by=By.CSS_SELECTOR, value='tr td'))
            for x in range(size):
                if x == 0:
                    text = driver.find_element(by=By.TAG_NAME, value="body").text
                    n = os.path.join(os.getcwd(), f'plain_textmacierz.txt')
                    f = codecs.open(n, "w", "utf−8")
                    f.write(text) 
                

                
                 
                tableDzialy = driver.find_element(by=By.ID, value="nawigacja")
                table = tableDzialy.find_elements(by=By.CSS_SELECTOR, value='tr td')
                table2 = table[x].find_elements(by=By.CSS_SELECTOR, value='form input')
                button = table2[-1]
                button.submit()
                sleep(1)
                n = os.path.join(os.getcwd(), f'pagemacierz{x}.html')
                f = codecs.open(n, "w", "utf−8")
                h = driver.page_source
                f.write(h)


            driver.quit()
            
            
            
            print("otwieranie execla")
            execel.start()
            
            
        except Exception as e:
                print("brakmacierzy, pisanie bez ....  trzeba dodać")
                print("An error occurred:", str(e))
                brakmacierzy()
                

    else:
        if "SPÓŁDZIELCZE WŁASNOŚCIOWE PRAWO DO LOKALU" in captured_text:        
            print("To SPÓŁDZIELCZE WŁASNOŚCIOWE PRAWO DO LOKALU :PP")
            time.sleep(4)
        if "NIERUCHOMOŚĆ GRUNTOWA" in captured_text:
            print("To działka :PP")
            
            time.sleep(4)
            
        else:
            print("To działka :PP")

        
       

def brakKW():
    driver.quit()
    with open('przetwarzane.txt', "r") as file1:
        file_content1 = file1.readlines()
        
        file_content1 = [line.strip() for line in file_content1]
            
   

        inp0 = file_content1[0]
        


    
    with open('done.txt', 'a') as file:
        file.write(str(inp0) + '\n') 

    time.sleep(1)

def brakmacierzy():
    driver.quit()

    with open('przetwarzane.txt', "r") as file1:
        file_content1 = file1.readlines()
        
        file_content1 = [line.strip() for line in file_content1]
            
   

        inp0 = file_content1[0]
    
    with open('done.txt', 'a') as file:
        file.write(str(inp0) + '\n') 
    time.sleep(1)
    driver.quit()
    cleanup()
     


def exit_handler(signum, frame):
    mark_as_off()
    sys.exit(0)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    
    mark_as_available()
    restart = True

    
      # Register mark_as_off() to be called on exit
    
script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path)
file_name = "przetwarzane_file.txt"



while restart:
    try:
        cleanup()
        czyta()
        mark_as_available()  # Mark as available before the next iteration
        restart = True
    except Exception:
        
        mark_as_available()
        restart = True  # Set restart to True to initiate script restart
    
