#
# import random #импортирую модуль рандом
# print("Привет") #приветствие
#
#
# player = input("Выберите- камень ножницы или бумага: ") # вы выбераете камень ножницу или бумагу
# possible_things = ["камень", "ножницы", "бумага"] # лист для компьютера, тут он выберает на рандом
# computer = random.choice(possible_things) # компютер на рандом выберает
#
# try: # попытка если все отлично он работает
#
#     print(f"Вы выбрали - {player}, компьютер выбрал {computer}")  # тут выводятся ваши ответы
#     if computer == player: # условие если у компьютера и игрока ответы одиннакоые то он пишет ничья
#         print("Ничья!")
#     elif player == 'камень': # если игрок выбрал камень
#         if computer == 'ножницы': # а компьютер ножницы
#             print("Вы выиграли!") # то игрок выиграл
#         elif computer == 'бумага': # если компьютер выбрал бумагу
#             print("Вы проиграли") # то игрок проиграл
#
#
#     elif player == 'ножницы':
#         if computer == 'бумага':
#             print("Вы выиграли!")
#         elif computer == 'камень':
#             print("Вы проиграли")
#         else:
#             print("Error")
#
#     elif player == 'бумага':
#         if computer == 'камень':
#             print("Вы выиграли!")
#         elif computer == 'ножницы':
#             print("Вы проиграли")
#         else:
#             print("Error")
#     else:
#         print("Ошыбка - проиграли")
#
# except Exception as e: # если в коде будет ошибка
#     print(f" вас ошибка - {e}") # то код будет выводить вашу ошибку

import sys


class PizzaFreddyFazber:


    def Ordering(self):
        print("чтобы одтвердить пишите - потдверждаю и чтобы отменить - отменяю а дальше сами разберетесь")
        pizzas = input("Какую пиццу вы будете - Пепперони, Барбекю, Дары Моря: ")
        try:
            match pizzas:
                case 'Пепперони':
                    pricePepperoni = 5000
                    corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю: ")
                    if corfirmation == 'потдверждаю':
                        print(f"Вы должны заплатить {pricePepperoni}")
                        sys.exit()

                    elif corfirmation == 'отменяю':
                        sys.exit()

                    elif corfirmation == 'Продолжаю':
                        Daughs = input("Какое тесто вы будете - Бездрожжевое  или Дрожжевое: ")
                        match Daughs:
                            case 'Бездрожжевое':
                                Yeastfree = 1000
                                corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю: ")
                                if corfirmation == 'потдверждаю':
                                    print(f"Вы должны заплатить {Yeastfree + pricePepperoni}")
                                    sys.exit()
                                elif corfirmation == 'отменяю':
                                    sys.exit()
                                elif corfirmation == 'Продолжаю':
                                    sauces = input("Какой соус вы будете - томатный или красный")
                                    match sauces:
                                        case 'томатный':
                                            tomato = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                        case 'красный':
                                            red = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {red + pricePepperoni + Yeastfree}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeastfree + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(f"Вы должны заплатить {red + pricePepperoni + Yeastfree + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())

                                else:
                                    print("Ошибка", sys.exit())

                            case 'Дрожжевое':
                                Yeast = 500
                                corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                if corfirmation == 'потдверждаю':
                                    print(f"Вы должны заплатить {Yeast + pricePepperoni}")
                                    sys.exit()
                                elif corfirmation == 'отменяю':
                                    sys.exit()

                                elif corfirmation == 'Продолжаю':
                                    sauces = input("Какой соус вы будете - томатный или красный")
                                    match sauces:
                                        case 'томатный':
                                            tomato = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {tomato + pricePepperoni + Yeast}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeast + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeast + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                        case 'красный':
                                            red = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {red + pricePepperoni + Yeast}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeast + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeast + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                else:
                                    print("Ошибка", sys.exit())
                    else:
                        print("Ошибка", sys.exit())





                case 'Барбекю':
                    pricePepperoni = 5000
                    corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю: ")
                    if corfirmation == 'потдверждаю':
                        print(f"Вы должны заплатить {pricePepperoni}")
                        sys.exit()

                    elif corfirmation == 'отменяю':
                        sys.exit()

                    elif corfirmation == 'Продолжаю':
                        Daughs = input("Какое тесто вы будете - Бездрожжевое  или Дрожжевое: ")
                        match Daughs:
                            case 'Бездрожжевое':
                                Yeastfree = 1000
                                corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю: ")
                                if corfirmation == 'потдверждаю':
                                    print(f"Вы должны заплатить {Yeastfree + pricePepperoni}")
                                    sys.exit()
                                elif corfirmation == 'отменяю':
                                    sys.exit()
                                elif corfirmation == 'Продолжаю':
                                    sauces = input("Какой соус вы будете - томатный или красный")
                                    match sauces:
                                        case 'томатный':
                                            tomato = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                        case 'красный':
                                            red = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {red + pricePepperoni + Yeastfree}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeastfree + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeastfree + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())

                                else:
                                    print("Ошибка", sys.exit())

                            case 'Дрожжевое':
                                Yeast = 500
                                corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                if corfirmation == 'потдверждаю':
                                    print(f"Вы должны заплатить {Yeast + pricePepperoni}")
                                    sys.exit()
                                elif corfirmation == 'отменяю':
                                    sys.exit()

                                elif corfirmation == 'Продолжаю':
                                    sauces = input("Какой соус вы будете - томатный или красный")
                                    match sauces:
                                        case 'томатный':
                                            tomato = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {tomato + pricePepperoni + Yeast}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeast + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeast + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                        case 'красный':
                                            red = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {red + pricePepperoni + Yeast}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeast + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeast + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                else:
                                    print("Ошибка", sys.exit())
                    else:
                        print("Ошибка", sys.exit())

                case 'Дары Моря':
                    pricePepperoni = 5000
                    corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю: ")
                    if corfirmation == 'потдверждаю':
                        print(f"Вы должны заплатить {pricePepperoni}")
                        sys.exit()

                    elif corfirmation == 'отменяю':
                        sys.exit()

                    elif corfirmation == 'Продолжаю':
                        Daughs = input("Какое тесто вы будете - Бездрожжевое  или Дрожжевое: ")
                        match Daughs:
                            case 'Бездрожжевое':
                                Yeastfree = 1000
                                corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю: ")
                                if corfirmation == 'потдверждаю':
                                    print(f"Вы должны заплатить {Yeastfree + pricePepperoni}")
                                    sys.exit()
                                elif corfirmation == 'отменяю':
                                    sys.exit()
                                elif corfirmation == 'Продолжаю':
                                    sauces = input("Какой соус вы будете - томатный или красный")
                                    match sauces:
                                        case 'томатный':
                                            tomato = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeastfree + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                        case 'красный':
                                            red = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {red + pricePepperoni + Yeastfree}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeastfree + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeastfree + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())

                                else:
                                    print("Ошибка", sys.exit())

                            case 'Дрожжевое':
                                Yeast = 500
                                corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                if corfirmation == 'потдверждаю':
                                    print(f"Вы должны заплатить {Yeast + pricePepperoni}")
                                    sys.exit()
                                elif corfirmation == 'отменяю':
                                    sys.exit()

                                elif corfirmation == 'Продолжаю':
                                    sauces = input("Какой соус вы будете - томатный или красный")
                                    match sauces:
                                        case 'томатный':
                                            tomato = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {tomato + pricePepperoni + Yeast}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeast + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {tomato + pricePepperoni + Yeast + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                        case 'красный':
                                            red = 100
                                            corfirmation = input("Вы подтвеждаете или отменяете или Продолжаю")
                                            if corfirmation == 'потдверждаю':
                                                print(f"Вы должны заплатить {red + pricePepperoni + Yeast}")
                                                sys.exit()
                                            elif corfirmation == 'отменяю':
                                                sys.exit()
                                            elif corfirmation == 'Продолжаю':
                                                fillings = input("Какие начинки вы будете - халапеньо или оливки")
                                                match fillings:
                                                    case 'халапеньо':
                                                        jalapeno = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeast + jalapeno}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                                    case 'оливки':
                                                        olives = 50
                                                        if corfirmation == 'потдверждаю':
                                                            print(
                                                                f"Вы должны заплатить {red + pricePepperoni + Yeast + olives}")
                                                            sys.exit()
                                                        elif corfirmation == 'отменяю':
                                                            sys.exit()
                                                        else:
                                                            print("Ошибка", sys.exit())
                                            else:
                                                print("Ошибка", sys.exit())
                                else:
                                    print("Ошибка", sys.exit())
                    else:
                        print("Ошибка", sys.exit())

        except Exception as e:
            print(f" вас ошибка - {e}")

pizza = PizzaFreddyFazber()
print(pizza.Ordering())