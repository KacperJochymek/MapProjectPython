from Autobusy.dane2 import user_list2

from Kierowca.funkcje3 import show_user_list_kierowca, say_hello_kierowca, prepare_group_of_maps_kierowca, get_user_kierowca, \
    get_coooridinates_kierowca, prepare_single_map_kierowca


def main3():
    say_hello_kierowca(user_list2[0]["name"])
    show_user_list_kierowca(user_list2)
    prepare_group_of_maps_kierowca(user_list2)

    lista_do_przygotowania_zbiorczej_mapy = []
    lista_do_przygotowania_zbiorczej_tekstow = []

    for user in user_list2[0:]:
        lista_do_przygotowania_zbiorczej_tekstow.append(
            get_user_kierowca(
                user["name"], user["kierowca"], user["miejsce"]
            )
        )
        lista_do_przygotowania_zbiorczej_mapy.append(
            get_coooridinates_kierowca(
                user['miejsce']
            )
        )

    prepare_single_map_kierowca(
        lista_do_przygotowania_zbiorczej_mapy,
        lista_do_przygotowania_zbiorczej_tekstow
    )


if __name__ == '__main__':
    main3()
