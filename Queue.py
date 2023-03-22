class Queue(object):            #Простая реализация очереди под эту задачу

    def __init__(self, maxlen):         
        self.queue = []
        self.size = maxlen

    def fully(self):
        return(f"{len(self.queue)} из {self.size}")

    def add_element(self, toy):
        if (len(self.queue) < self.size):
            self.queue.append(toy)
        else:
            print("Корзина выдачи переполнена, заберите игрушки!")
    
    def get_element(self):              #Помимо простого удаления из начала очереди происходит запись в файл-список выданых игрушек
        if len(self.queue) > 0:
            with open ("MyToys.txt", "a", encoding="utf-8") as file:
                file.write(str(self.get())+" ")
            print(f"Игрушка {self.get().name} выдана! ")
            self.queue.pop(0)
        
        return("Игрушек на выдачу нет")

    def __repr__(self):                 #dunder-метод для вывода корзины
        if len(self.queue)==0:
            return("Игрушек на выдачу нет")
        else :
            string = "Список игрушек на выдачу:"
            for i in range(len(self.queue)):
                string+=(f" {str(self.queue[i])}")
            return(string)

    
    def get(self):
        return(self.queue[0])