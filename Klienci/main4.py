from Autobusy.dane2 import user_list2
from Klienci.funkcje4 import show_user_list4, say_hello4, prepare_group_of_maps4, get_user4, \
    get_coooridinates4, prepare_single_map4


def main4():
    say_hello4(user_list2[0]["name"])
    show_user_list4(user_list2)
    prepare_group_of_maps4(user_list2)

    lista_do_przygotowania_zbiorczej_mapy = []
    lista_do_przygotowania_zbiorczej_tekstow = []

    for user in user_list2[0:]:
        lista_do_przygotowania_zbiorczej_tekstow.append(
            get_user4(
                user["name"], user["klienci"], user["miejsce"]
            )
        )
        lista_do_przygotowania_zbiorczej_mapy.append(
            get_coooridinates4(
                user['miejsce']
            )
        )

    prepare_single_map4(
        lista_do_przygotowania_zbiorczej_mapy,
        lista_do_przygotowania_zbiorczej_tekstow
    )


if __name__ == '__main__':
    main4()
