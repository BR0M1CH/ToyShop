import random
import Queue

class ToyShop(object):

    n = 5                       #Размер корзины

    toys_list = []              #"Склад" магазина
    queue = Queue.Queue(n)      #"Корзина" выдачи

    def __init__(self):
        print("Магазин игрушек приветствует Вас!")

    def rand_game(self):            #Проверка не пуст ли список игрушек, если нет, то выбирается рандомная игрушка и разыгрывается
        if len(self.toys_list)==0:
            return("В нашем магазине закончились игрушки :(, попробуем позвонить поставщику")
        if len(self.toys_list)==self.n:
            return("Корзина выдачи переполнена, заберите игрушки")
        toy = random.choice(self.toys_list)
        return(toy.game(self))

    def game(self, name):           #Проверка не пуст ли список игрушек, если нет, то игрушка с таким именем ищется в списке игрушек магазина и разыгрывается
        if len(self.toys_list)==0:
            return("В нашем магазине закончились все игрушки :( Позвоним поставщику")
        if len(self.toys_list)==self.n:
            return("Корзина выдачи переполнена, заберите игрушки")
        for i in range(len(self.toys_list)):
            if self.toys_list[i].name.lower() == name.lower():
                return(self.toys_list[i].game(self))

    def add(self, name):            #На вход получаем имя, пробегаясь по всем классам смотрим: соответствует ли полученное имя с именем объекта класса
                                    #Если соответствует - добавляем в хранилище магазина новый объект нужного класса
        if name=="teddybear":
            self.toys_list.append(TeddyBear())
            return("Плюшевый мишка уже ждет Вас на полках нашего магазина!")
        elif name=="buzzlighter":
            self.toys_list.append(Buzzlighter())
            return("Баззлайтер уже ждет Вас на полках нашего магазина!")
        elif name=="barbie":
            self.toys_list.append(Barbie())
            return("Кукла Барби из новой коллекции уже ждет Вас на полках нашего магазина!")
        elif name=="toycar":
            self.toys_list.append(ToySportCar())
            return("Мощнейший мустанг уже ждет Вас на полках нашего магазина!")
        else:
            return("Такой игрушки у поставщиков нет, мы с ними обязательно свяжемся")

    def show_queue(self):
        print(self.queue)

    def dif_toys(self):             #Выводит список видов игрушек в магазине
                                    #Пробегаемся по всем игрушкам, закидываем ID каждой(от 1 до 4) в буферный список, затем преобразовываем в множество
                                    #И обратно в список, чтобы были уникальные элементы и в соответствии с уникальными элементами(id) выводим список игрушек
        if len(self.toys_list)==0:
            return(0)
        stack = []
        for i in range(len(self.toys_list)):
            if self.toys_list[i].name=="TeddyBear":
                stack.append(1)
            elif self.toys_list[i].name=="Buzzlighter":
                stack.append(2)
            elif self.toys_list[i].name=="ToySportCar":
                stack.append(3)
            elif self.toys_list[i].name=="Barbie":
                stack.append(4)
        stack=list(set(stack))
        string = "У нас есть: "
        if 1 in stack:
            string+=("TeddyBear ")
        if 2 in stack:
            string+=("Buzzlighter ")
        if 3 in stack:
            string+=("ToySportCar ")
        if 4 in stack:
            string+=("Barbie ")
        return(string)    
    
    def get_toy(self):
        self.queue.get_element()

        
###########################################################################################################################################



class Toys(object):
    name = ""
    drop_chance = 10

    def game(self, other):                    #Просто розыгрыш на рандоме. Если игрушка "выпала", то убираем из хранилища магазина ёё и вставляем в корзину
        if random.randint(0, 100) <= self.drop_chance:
            other.queue.add_element(self)  
            other.toys_list.remove(self) 
            return(f"Игрушка {self.name} выпала! Поздравляем!")
        else:
            return(f"Игрушка {self.name} не выпала. Какая досада, приходите еще.")
        
    def __repr__(self) -> str:
        return(self.name)
    


    


class TeddyBear(Toys):
    def __init__(self):
        self.name = "TeddyBear"
        self.drop_chance = 60


class ToySportCar(Toys):
    def __init__(self):
        self.name = "ToySportCar"
        self.drop_chance = 40


class Barbie(Toys):
    def __init__(self):
        self.name = "Barbie"
        self.drop_chance = 20


class Buzzlighter(Toys):
    def __init__(self):
        self.name = "Buzzlighter"
        self.drop_chance = 10


