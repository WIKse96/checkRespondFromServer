import pandas as pd
import requests
from time import sleep
import urllib3


def read():
    #Dane testowe
    # data = {'url': ['https://stackoverflow.com/questions/18810777/how-do-i-read-a-response-from-python-requests',
    #               'https://dev321.seart.pl/product/list/id/16970/category/462/szafa-sosnowa-marika-80.html',
    #               'https://www.seart.pl/review/product/list/id/16970/category/462/szafa-sosnowa-marika-80.html']}
    # df = pd.DataFrame(data)
    #---------------------------------------------------------
    #W stringu ścieżka pliku, z którego zaciągamy urle
    df = pd.read_csv('./prod.csv')
    j = 0
    while j < len(df):

        url = df['url'][j]
        print('sprawdzam: ',url)
        df.loc[j, "Respond"] = whatRespond(url)#odpowiedź
        j += 1
    df.to_csv('./respond.csv', index=False)


# Funkcja sprawdzania odpowiedzi serwera
def whatRespond(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        sleep(4)
        response = requests.get(url, timeout=31)  # Timeout ustawiony na 31 sekund
        response.raise_for_status()  # Sprawdzenie kodu statusu odpowiedzi
        # Tutaj przetwarzaj odpowiedź
    except requests.Timeout:
        print("Przekroczono czas oczekiwania na odpowiedź")
    except requests.RequestException as e:
        print(f"Błąd zapytania: {e}")


    r = requests.get(f"{url}", verify=False)
    return r.status_code


if __name__ == '__main__':
    read()

