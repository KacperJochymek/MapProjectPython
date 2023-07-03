# kod do pobierania pobierania wspolrzednych ze storny wikipedii
import re
import folium
import requests
import random

from bs4 import BeautifulSoup


def say_hello_kierowca(tekst):
    print(f'Witaj {tekst} ! ')


def prepare_group_of_maps_kierowca(lista_uzytkownikow: list) -> None:
    for user in lista_uzytkownikow[1:]:
        wspolrzedne = get_coooridinates3(user["miejsce"])
        tekst = get_user3(user["name"],user["kierowca"], user["miejsce"])
        id = user["id"]
        prepare_map3(wspolrzedne, tekst, id)
        # print(f'trwa przygotowanie mapy {user["miejsce"]} nr {id} ')


def show_user_list_kierowca(lista_uzytkownikow: list) -> None:
    for user in lista_uzytkownikow[0:]:
        print(get_user3(user["name"], user['kierowca'], user["miejsce"]))


def get_user_kierowca(name, kierowca, miejsce):
    return f'Twój znajomy {name} dodał nowego kierowcę: {kierowca} w miejscowosci:{miejsce}, ' \
           f'wspolrzedne {get_coooridinates3(miejsce)}'


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
    print('Kierowca usunięty poprawnie')
    return updated_list


def my_gui3():
    print('---------------------------------------------')
    print('-                Lista Kierowców                   -')
    print('---------------------------------------------')
    print('|    Dostępne funkcje                       |')
    print('|        1. Wyświetl listę kierowców   |')
    print('|        2. Dodaj kierowcę (create)        |')
    print('|        3. Usun kierowcę (delete)         |')
    print('|        4. Wyswietl kierowcę              |')
    print('|        0. Powrót do menu głównego          |')
    print('---------------------------------------------')


def my_fellow_kierowca(name: str, miejsce: str, kierowca: list[str]) -> None:
    print('---------------------------------------------')
    print(f'         {name}                            ')
    print('---------------------------------------------')
    print(f'    kierowca: {kierowca}                        ')
    print(f'    miejsce: {miejsce}                      ')
    print('---------------------------------------------')


def view_user_kierowca(user_list2: list[dict]) -> None:
    user_nick = input('Podaj imię kierowcy do wyświetlenia: ')
    selected_user = [user for user in user_list2 if user['kierowca'] == user_nick]

    if selected_user:
        print(f'Imię kierowcy: {selected_user[0]["kierowca"]}')
    else:
        print('Nie znaleziono kierowcy o podanym imieniu.')


