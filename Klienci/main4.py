from Autobusy.dane2 import user_list2
from Klienci.funkcje4 import show_user_list_klienci, say_hello_klienci, prepare_group_of_maps_klienci, get_user_klienci, \
    get_coooridinates_klienci, prepare_single_map_klienci


def main4():
    say_hello_klienci(user_list2[0]["name"])
    show_user_list_klienci(user_list2)
    prepare_group_of_maps_klienci(user_list2)

    lista_do_przygotowania_zbiorczej_mapy = []
    lista_do_przygotowania_zbiorczej_tekstow = []

    for user in user_list2[0:]:
        lista_do_przygotowania_zbiorczej_tekstow.append(
            get_user_klienci(
                user["name"], user["klienci"], user["miejsce"]
            )
        )
        lista_do_przygotowania_zbiorczej_mapy.append(
            get_coooridinates_klienci(
                user['miejsce']
            )
        )

    prepare_single_map_klienci(
        lista_do_przygotowania_zbiorczej_mapy,
        lista_do_przygotowania_zbiorczej_tekstow
    )


if __name__ == '__main__':
    main4()
