# kod do pobierania pobierania wspolrzednych ze storny wikipedii
import re
import folium
import requests
import random

from bs4 import BeautifulSoup


def say_hello_kierowca(tekst):
    print(f'Witaj {tekst} ! ')


def prepare_group_of_maps_kierowca(lista_uzytkownikow: list) -> None:
    for user in lista_uzytkownikow[0:]:
        wspolrzedne = get_coooridinates_kierowca(user["miejsce"])
        tekst = get_user_kierowca(user["name"], user["kierowca"], user["miejsce"])
        id = user["id"]
        prepare_map_kierowca(wspolrzedne, tekst, id)
        # print(f'trwa przygotowanie mapy {user["miejsce"]} nr {id} ')


def show_user_list_kierowca(lista_uzytkownikow: list) -> None:
    for user in lista_uzytkownikow[0:]:
        print(get_user_kierowca(user["name"], user['kierowca'], user["miejsce"]))


def get_user_kierowca(name, kierowca, miejsce):
    return f'Twój znajomy {name} dodał nowego kierowcę: {kierowca} w miejscowosci:{miejsce}, ' \
           f'wspolrzedne {get_coooridinates_kierowca(miejsce)}'


def get_coooridinates_kierowca(nazwa_miejscowosci: str) -> list:
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


def prepare_map_kierowca(nazwa_miejscowosci: list, tresc_popup: str, id: int) -> None:
    mapka = folium.Map(location=nazwa_miejscowosci, tiles="OpenStreetMap", zoom_start=12)
    folium.Marker(location=nazwa_miejscowosci, popup=f'{tresc_popup}').add_to(mapka)
    mapka.save(f'./mapkaKierowca_{id}.html')


def prepare_single_map_kierowca(lista_wspolrzednych: list[int], tekst: list[str]) -> None:
    mapka = folium.Map(location=[52.30, 21.0], tiles="OpenStreetMap", zoom_start=6)
    for index, _ in enumerate(lista_wspolrzednych):
        folium.Marker(location=lista_wspolrzednych[index], popup=f'{tekst[index]}').add_to(mapka)
    mapka.save(f'./mapaKierowca.html')


def create_user_kierowca():
    name = input('podaj nazwe uzytkownika')
    place = input('podaj miejsce uzytkownika')
    kierowca = input('podaj imię kierowcy')
    password = input('podaj hasło')
    new_user = {
        'id': random.randint(0, 10000000), 'name': name,
        'miejsce': place,
        'kierowca': kierowca,
        'hasło': password,
        'lista_kierowcow': [],
    }
    print(new_user)
    return new_user


def delete_user_kierowca(user_list2: list) -> list:
    zmienna = input('Podaj imię kierowcy do usuniecia')
    updated_list = [i for i in user_list2 if i['kierowca'] != zmienna]
    print('Kierowca usunięty poprawnie:', zmienna)
    return updated_list


def my_gui3():
    print('------------------------------------------------------------')
    print('-                       Lista Kierowców                    -')
    print('------------------------------------------------------------')
    print('|                        Dostępne funkcje                  |')
    print('|        1. Wyświetl listę kierowców                       |')
    print('|        2. Dodaj kierowcę (create)                        |')
    print('|        3. Usun kierowcę (delete)                         |')
    print('|        4. Wyswietl kierowcę                              |')
    print('|        5. Wyswietl kierowcę wybranej linii autobusowej   |')
    print('|        0. Powrót do menu głównego                        |')
    print('------------------------------------------------------------')


# def my_fellow_kierowca(kierowca: str, user_list2: list) -> None:
#     for user in user_list2:
#         if kierowca in user['kierowca']:
#                 name = user['name']
#                 miejsce = user['miejsce']
#                 linia_autobus = user['linia_autobus']
#                 klienci = user['klienci']
#
#                 print('---------------------------------------------')
#                 print(f'         {name}                 ')
#                 print('---------------------------------------------')
#                 print(f'    klienci: {klienci}                        ')
#                 print(f'    miejsce: {miejsce}                      ')
#                 print(f'    linia_autobus: {linia_autobus}                      ')
#                 print('---------------------------------------------')
#                 break
#     else:
#         print('Nie znaleziono kierowcy o podanym imieniu.')

def my_fellow_kierowca(linia_autobusu: str, user_list2: list) -> None:
    print(f'Wybierz linię autobusu, dla której mają zostąc wyświetleni kierowcy')
    linia = input("Podaj linię autobusu: ")

    for user in user_list2:
        if 'nr_autobusu' in user and 'kierowca' in user and 'linia_autobus' in user:
            kierowca = user['kierowca']
            linie_autobusy = user['linia_autobus']

            if linia in linie_autobusy:
                name = user['name']
                miejsce = user['miejsce']

                print('---------------------------------------------')
                print(f'         {name}                 ')
                print('---------------------------------------------')
                print(f'    kierowca: {(kierowca)}')
                print(f'    miejsce: {miejsce}                      ')
                print('---------------------------------------------')
                return

    print('Nie znaleziono podanej linii autobusu.')


def view_user_kierowca(user_list2: list[dict]) -> None:
    user_nick = input('Podaj imię kierowcy do wyświetlenia: ')
    selected_user = [user for user in user_list2 if user['kierowca'] == user_nick]

    if selected_user:
        print(f'Imię kierowcy: {selected_user[0]["kierowca"]}')
    else:
        print('Nie znaleziono kierowcy o podanym imieniu.')
