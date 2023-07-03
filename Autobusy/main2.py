from Autobusy.dane2 import user_list2
from Autobusy.funkcje2 import show_user_list_autobus, say_hello_autobus, prepare_group_of_maps_autobus, get_user_autobus, \
    get_coordinates_autobus, prepare_single_map_autobus



def main2():
    say_hello_autobus(user_list2[0]["name"])
    show_user_list_autobus(user_list2)
    prepare_group_of_maps_autobus(user_list2)

    lista_do_przygotowania_zbiorczej_mapy = []
    lista_do_przygotowania_zbiorczej_tekstow = []

    for user in user_list2[1:]:
        lista_do_przygotowania_zbiorczej_tekstow.append(
            get_user_autobus(
                user["name"], user["nr_autobusu"], user["miejsce"]
            )
        )
        lista_do_przygotowania_zbiorczej_mapy.append(
            get_coordinates_autobus(
                user['miejsce']
            )
        )

    prepare_single_map_autobus(
        lista_do_przygotowania_zbiorczej_mapy,
        lista_do_przygotowania_zbiorczej_tekstow
    )


if __name__ == '__main__':
    main2()
