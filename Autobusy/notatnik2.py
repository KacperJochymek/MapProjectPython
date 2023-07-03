from Autobusy.funkcje2 import my_gui2, create_user_autobus, show_user_list_autobus, my_fellow_autobus, \
    view_user_autobus, \
    delete_user_autobus
from Autobusy.dane2 import user_list2
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
                my_gui2()
                selected_option = input('Wybierz dostępną funkcje i zatwierdz klikając przycisk enter ')

                while selected_option != "0":
                    if selected_option == '1':
                        show_user_list_autobus(user_list2)
                    elif selected_option == '2':
                        user_list2.append(create_user_autobus())
                    elif selected_option == '3':
                        user_list2 = delete_user_autobus(user_list2)
                    elif selected_option == '4':
                        view_user_autobus(user_list2)
                    elif selected_option == '5':
                        my_fellow_autobus(user_list2)

                    selected_option = input('\nWybierz dostępną funkcje i zatwierdz klikając przycisk enter ')

                start_gui()
        else:
            licznik += 1
    else:
        logging = False

# TODO OBIEKTÓWKA
# TODO DODAJ funkcje generowania MAPY DO GUI
