from Autobusy.dane2 import user_list2
from Autobusy.funkcje2 import show_user_list2, say_hello2, prepare_group_of_maps2, get_user2, \
    get_coordinates2, prepare_single_map2



def main2():
    say_hello2(user_list2[0]["name"])
    show_user_list2(user_list2)
    prepare_group_of_maps2(user_list2)

    lista_do_przygotowania_zbiorczej_mapy = []
    lista_do_przygotowania_zbiorczej_tekstow = []

    for user in user_list2[1:]:
        lista_do_przygotowania_zbiorczej_tekstow.append(
            get_user2(
                user["name"], user["nr_autobusu"], user["miejsce"]
            )
        )
        lista_do_przygotowania_zbiorczej_mapy.append(
            get_coordinates2(
                user['miejsce']
            )
        )

    prepare_single_map2(
        lista_do_przygotowania_zbiorczej_mapy,
        lista_do_przygotowania_zbiorczej_tekstow
    )


if __name__ == '__main__':
    main2()
