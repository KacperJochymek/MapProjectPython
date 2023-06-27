from Autobusy.dane2 import user_list2

from Kierowca.funkcje3 import show_user_list3, say_hello3, prepare_group_of_maps3, get_user3, \
    get_coooridinates3, prepare_single_map3


def main3():
    say_hello3(user_list2[0]["name"])
    show_user_list3(user_list2)
    prepare_group_of_maps3(user_list2)

    lista_do_przygotowania_zbiorczej_mapy = []
    lista_do_przygotowania_zbiorczej_tekstow = []

    for user in user_list2[0:]:
        lista_do_przygotowania_zbiorczej_tekstow.append(
            get_user3(
                user["name"], user["kierowca"], user["miejsce"]
            )
        )
        lista_do_przygotowania_zbiorczej_mapy.append(
            get_coooridinates3(
                user['miejsce']
            )
        )

    prepare_single_map3(
        lista_do_przygotowania_zbiorczej_mapy,
        lista_do_przygotowania_zbiorczej_tekstow
    )


if __name__ == '__main__':
    main3()
