def start_gui():
    print('----------------------------------------------')
    print('-                 Start Menu                 -')
    print('----------------------------------------------')
    print('|              Dostępne funkcje              |')
    print('|      1. Przejdź do sekcji z Autobusami     |')
    print('|      2. Przejdź do sekcji z Kierowcami     |')
    print('|      3. Przejdź do sekcji z Klientami      |')
    print('|      0. Zakończ program                    |')
    print('----------------------------------------------')

    while True:
        wybor = input('Wybierz opcję (0-3): ')

        if wybor == '1':
            from Autobusy import notatnik2
            notatnik2
        elif wybor == '2':
            from Kierowca import notatnik3
            notatnik3
        elif wybor == '3':
            from Klienci import notatnik4
            notatnik4
        elif wybor == '0':
            print('Zamykanie programu...')
            break
        else:
            print('Nieprawidłowy wybór. Wybierz opcję od 0 do 3.')


start_gui()
