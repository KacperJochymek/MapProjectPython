from Autobusy.dane2 import user_list2
from Klienci.funkcje4 import my_gui4, my_fellow4, show_user_list4, delete_user4, view_user4, create_user4
from start import start_gui

licznik = 0
logging = True
while logging:
    if licznik < 3:
        nazwa_uzytkownika = input('podaj nazwe uzytkownika')
        haslo_uzytkownika = input('podaj hasło uzytkownika')
        for user in user_list2:
            if nazwa_uzytkownika == user["name"] and haslo_uzytkownika == user["hasło"]:
                print(f' Zalogowano jako: \n  \tnazwa: {user["name"]}')
                my_gui4()
                selected_option = input('Wybierz dostępną funkcje i zatwierdz klikając przycisk enter ')

                while selected_option != "0":
                    if selected_option == '1':
                        show_user_list4(user_list2)
                    elif selected_option == '2':
                        user_list2.append(create_user4())
                    elif selected_option == '3':
                        user_list2 = delete_user4(user_list2)
                    elif selected_option == '4':
                        view_user4(user_list2)
                    elif selected_option == '5':
                        user_nick = input('podaj numer kierowcy, ktory chcesz wyswietlic ')
                        fellow_list3 = [i for i in user_list2 if i['kierowca'] == user_nick][0]['kierowca']
                        [
                            [
                                my_fellow4(
                                    name=user['name'],
                                    miejsce=user['miejsce'],
                                    kierowca=user['kierowca'],
                                ) for user in
                                user_list2 if user['id'] == fellow3
                            ] for fellow3 in fellow_list3
                        ]

                    selected_option = input('\nWybierz dostępną funkcje i zatwierdz klikając przycisk enter ')

                start_gui()
        else:
            licznik += 1
    else:
        logging = False

# TODO OBIEKTÓWKA
# TODO DODAJ funkcje generowania MAPY DO GUI