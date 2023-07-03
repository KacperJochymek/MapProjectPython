import re
import folium
import requests
import random

from bs4 import BeautifulSoup


def say_hello_autobus(tekst):
    print(f'Witaj {tekst}! ')


def prepare_group_of_maps_autobus(lista_uzytkownikow: list) -> None:
    for user in lista_uzytkownikow:
        wspolrzedne = get_coordinates_autobus(user["miejsce"])
        tekst = get_user_autobus(user["name"], user["nr_autobusu"], user["miejsce"])
        id = user["id"]
        prepare_map_autobus(wspolrzedne, tekst, id)


def show_user_list_autobus(lista_uzytkownikow: list) -> None:
    for user in lista_uzytkownikow:
        print(get_user_autobus(user["name"], user["nr_autobusu"], user["miejsce"]))


def get_user_autobus(name, nr_autobusu, miejsce):
    return f'Twój znajomy {name} dodał autobus nr {nr_autobusu} w miejscowości: {miejsce}, współrzędne {get_coordinates_autobus(miejsce)}'


def get_coordinates_autobus(nazwa_miejscowosci: str) -> list:
    adres_url = f'https://pl.wikipedia.org/wiki/{nazwa_miejscowosci}'
    res = requests.get(adres_url)
    res_html = BeautifulSoup(res.text, 'html.parser')
    latitude = str(res_html.select('.latitude')[1])  # szerokość
    longitude = str(res_html.select('.longitude')[1])  # długość
    latitude = re.sub("(\<).*?(\>)", "", string=latitude, count=0, flags=0).replace(',', '.')
    longitude = re.sub("(\<).*?(\>)", "", string=longitude, count=0, flags=0).replace(',', '.')
    return [float(latitude), float(longitude)]


def prepare_map_autobus(nazwa_miejscowosci: list, tresc_popup: str, id: int) -> None:
    mapka = folium.Map(location=nazwa_miejscowosci, tiles="OpenStreetMap", zoom_start=12)
    folium.Marker(location=nazwa_miejscowosci, popup=f'{tresc_popup}').add_to(mapka)
    mapka.save(f'./mapkaAutobusy_{id}.html')


def prepare_single_map_autobus(lista_wspolrzednych: list, tekst: list) -> None:
    mapka = folium.Map(location=[52.30, 21.0], tiles="OpenStreetMap", zoom_start=6)
    for index, wspolrzedne in enumerate(lista_wspolrzednych):
        folium.Marker(location=wspolrzedne, popup=f'{tekst[index]}').add_to(mapka)
    mapka.save(f'./mapaAutobusy.html')


def create_user_autobus():
    name = input('Podaj nazwę użytkownika: ')
    place = input('Podaj miejsce użytkownika: ')
    nr_autobusu = input('Podaj numer autobusu: ')
    password = input('Podaj hasło: ')
    new_user = {
        'id': random.randint(0, 10000000),
        'name': name,
        'miejsce': place,
        'nr_autobusu': nr_autobusu,
        'hasło': password,
    }
    print(new_user)
    return new_user


def delete_user_autobus(user_list2: list) -> list:
    zmienna = input('Podaj numer autobusu do usunięcia: ')
    updated_list = [i for i in user_list2 if i['nr_autobusu'] != zmienna]
    print('Poprawnie usunięto autobus o numerze:', zmienna)
    return updated_list


def my_gui2():
    print('---------------------------------------------')
    print('-                Lista Autobusów            -')
    print('---------------------------------------------')
    print('|    Dostępne funkcje                        |')
    print('|        1. Wyświetl listę autobusów         |')
    print('|        2. Dodaj autobus (create)           |')
    print('|        3. Usuń autobus (delete)            |')
    print('|        4. Wyświetl autobus                 |')
    print('|        0. Powrót do menu głównego          |')
    print('---------------------------------------------')


def my_fellow_autobus(name: str, miejsce: str, nr_autobusu: int, lista_autobusu: list) -> None:
    print('---------------------------------------------')
    print(f'         {name}                              ')
    print('---------------------------------------------')
    print(f'    numer autobusu: {nr_autobusu}            ')
    print(f'    miejsce: {miejsce}                       ')
    for nr_autobusu in lista_autobusu:
        print(f'\tpost użytkownika {name}: {nr_autobusu}  ')
    print('---------------------------------------------')


def view_user_autobus(user_list2: list) -> None:
    nr_autobusu = input('Podaj numer autobusu do wyświetlenia: ')
    selected_user = [i for i in user_list2 if nr_autobusu in i['nr_autobusu']]

    if selected_user:
        print(f'Numer autobusu: {selected_user[0]["nr_autobusu"]}')
    else:
        print('Nie znaleziono autobusu o podanym numerze.')
