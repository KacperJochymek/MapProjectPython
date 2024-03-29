# kod do pobierania pobierania wspolrzednych ze storny wikipedii
import re
import folium
import requests
import random

from bs4 import BeautifulSoup


def say_hello_klienci(tekst):
    print(f'Witaj {tekst} ! ')


def prepare_group_of_maps_klienci(lista_uzytkownikow: list) -> None:
    for user in lista_uzytkownikow[0:]:
        wspolrzedne = get_coooridinates_klienci(user["miejsce"])
        tekst = get_user_klienci(user["name"], user['klienci'], user["miejsce"])
        id = user["id"]
        prepare_map_klienci(wspolrzedne, tekst, id)
        # print(f'trwa przygotowanie mapy {user["miejsce"]} nr {id} ')


def show_user_list_klienci(lista_uzytkownikow: list) -> None:
    for user in lista_uzytkownikow[0:]:
        print(get_user_klienci(user["name"], user["klienci"], user["miejsce"]))


def get_user_klienci(nick, klienci, miejsce):
    return f'Twój znajomy {nick} opublikował {klienci} miejscowosc:{miejsce}, ' \
           f'wspolrzedne {get_coooridinates_klienci(miejsce)}'


def get_coooridinates_klienci(nazwa_miejscowosci: str) -> list:
    # 1.pobierz strone
    adres_url = f'https://pl.wikipedia.org/wiki/{nazwa_miejscowosci}'
    res = requests.get(adres_url)
    res_html = BeautifulSoup(res.text, 'html.parser')
    # 2. get coordinates
    latitude = str(res_html.select('.latitude')[1])  # szerokosc
    longitude = str(res_html.select('.longitude')[1])  # dlugosc

    latitude = re.sub("(\<).*?(\>)", "", string=latitude, count=0, flags=0).replace(',', '.')
    longitude = re.sub("(\<).*?(\>)", "", string=longitude, count=0, flags=0).replace(',', '.')
    return [latitude, longitude]


def prepare_map_klienci(nazwa_miejscowosci: list, tresc_popup: str, id: int) -> None:
    mapka = folium.Map(location=nazwa_miejscowosci, tiles="OpenStreetMap", zoom_start=12)
    folium.Marker(location=nazwa_miejscowosci, popup=f'{tresc_popup}').add_to(mapka)
    mapka.save(f'./mapkaKlienci_{id}.html')


def prepare_single_map_klienci(lista_wspolrzednych: list[int], tekst: list[str]) -> None:
    mapka = folium.Map(location=[52.30, 21.0], tiles="OpenStreetMap", zoom_start=6)
    for index, _ in enumerate(lista_wspolrzednych):
        folium.Marker(location=lista_wspolrzednych[index], popup=f'{tekst[index]}').add_to(mapka)
    mapka.save(f'./mapaKlienci.html')


def create_user_klienci():
    name = input('podaj nazwe uzytkownika')
    place = input('podaj miejsce uzytkownika')
    klienci = input('podaj nazwisko klienta')
    password = input('podaj hasło')
    new_user = {
        'id': random.randint(0, 10000000), 'name': name,
        'miejsce': place,
        'klienci': klienci,
        'hasło': password,
        'lista_klientow': [],
    }
    print(new_user)
    return new_user


def delete_user_klienci(user_list2: list) -> list:
    zmienna = input('Podaj nazwisko klienta do usuniecia')
    updated_list = [i for i in user_list2 if i['klienci'] != zmienna]
    print('Poprawnie usunieto klienta:', zmienna)
    return updated_list


def my_gui4():
    print('-------------------------------------------------------------')
    print('-                    Lista Klientów                         -')
    print('-------------------------------------------------------------')
    print('|              Dostępne funkcje                             |')
    print('|        1. Wyświetl listę klientów                         |')
    print('|        2. Dodaj klienta (create)                          |')
    print('|        3. Usun klienta (delete)                           |')
    print('|        4. Wyswietl klienta                                |')
    print('|        5. Wyswietl klienta wybranej linii autobusowej     |')
    print('|        0. Powrót do menu głównego                         |')
    print('-------------------------------------------------------------')


def my_fellow_klienci(linia_autobusu: str, user_list2: list) -> None:
    print(f'Wybierz linię autobusu, dla której mają zostąc wyświetleni klienci')
    linia = input("Podaj linię autobusu: ")

    for user in user_list2:
        if 'nr_autobusu' in user and 'klienci' in user and 'linia_autobus' in user:
            klienci = user['klienci']
            linie_autobusy = user['linia_autobus']

            if linia in linie_autobusy:
                name = user['name']
                miejsce = user['miejsce']

                print('---------------------------------------------')
                print(f'         {name}                 ')
                print('---------------------------------------------')
                print(f'    klienci: {(klienci)}')
                print(f'    miejsce: {miejsce}                      ')
                print('---------------------------------------------')
                return

    print('Nie znaleziono podanej linii autobusu.')


def view_user_klienci(user_list2: list[dict]) -> None:
    user_nick = input('Podaj nazwisko klienta do wyświetlenia: ')
    selected_users = [user for user in user_list2 if user_nick in user['klienci']]

    if selected_users:
        for user in selected_users:
            matching_names = [name for name in user['klienci'] if name == user_nick]
            if matching_names:
                print(f'Nazwisko klienta: {matching_names[0]}')
    else:
        print('Nie znaleziono klienta o podanym nazwisku.')
