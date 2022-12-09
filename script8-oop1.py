# ООП основи
# Python підтримує лише основні ідеї ООП, але не має грунтовної їх реалізації
class MyClass :
    x = 10           # static


def main() -> None :
    obj1 = MyClass() 
    obj2 = MyClass()
    print( obj1.x, obj2.x )    #  (10,10) - всі посилаються до статичного поля
    obj1.y = 30                # динамічна типізація дозволяє додавати поля "runtime"
    obj1.x = 20                # не зміна статичного "х", а створення нового динамічного
    print( obj1.x,             # (20,10): при конфлікті імен динамічна змінна має пріоритет:
           obj2.x )            #  obj1.x - динамічна (об'єктна), obj2.x - статична (класова)
    MyClass.x = 40             # Змінюємо статичну змінну:
    print( obj1.x, obj2.x )    #  (20,40): obj1 - має своє поле "х", obj2 - не має і звертається до статичного



if __name__ == "__main__" :
    main()