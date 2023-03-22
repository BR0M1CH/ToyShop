import Toys



shop = Toys.ToyShop()
while True:

    command = str(input("Введите команду: "))

    if command.lower()=="/add":
        print("Список игрушек у поставщика:\tTeddyBear\tBarbie\tBuzzlighter\tToyCar")
        name = str(input("Введите название игрушки: "))
        print(shop.add(name.lower()))
    
    elif command.lower()=="/rand":
        print(shop.rand_game())
    
    elif command.lower()=="/game":
        if shop.dif_toys()==0:
            print("В нашем магазине закончились все игрушки :( Позвоним поставщику")
        else:
            print(shop.dif_toys())
            name = str(input("Введите название игрушки: "))
            print(shop.game(name))
    
    elif command.lower()=="/take":
        print(shop.queue)
        shop.get_toy()

    elif command.lower()=="/look":
        print(shop.dif_toys())

    elif command.lower()=="/exit":
        break

    elif command.lower()=="/help":
        stroka = "/help\tВывод списка команд\n/add\tДобавление игрушки от поставщика\n/rand\tРозыгрыш случайной игрушки\n"
        stroka += "/game\tРозыгрыш конкретной игрушки\n/take\tЗабрать первую игрушку в выдаче\n/look\tПосмотреть список игрушек в магазине"
        stroka += "\n/exit\tПокинуть магазин"
        print(stroka)

    elif command.lower()=="/adm":
        print(shop.queue)


    elif command.lower()=="/list":
        print(shop.toys_list)

    else:
        print("Список команд: /help")

        

