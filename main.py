# Импортирование
import datetime
from models import *
from colorama import init
init()
from colorama import Fore, Back, Style

# Логика работы программы
while True:
    print(Fore.GREEN + 'Добро Пожаловать в Центр Управления Базой Данных!' + Fore.RESET + ' \nВыберете одно из дейстивий:')
    print('1) Ввести запись в таблицу.\n2) Удалить запись из таблицы.\n3) Изменить данные в таблице \n4) Вывести на экран данные из таблицы\n0) Выйти из ЦУБД.')
    cmd = input()

    if cmd == "1":
        print('В какую таблицу вы хотите внести данные?\n1) Типы товара\n2) Клиент\n3) Товары\n4) Заказы.')
        num = input()

        if num=="1":
            print('Выбрана таблица "Типы товара". Напишите названия типа товара.')
            string1 = str(input())
            with db:
                string1 = TypeProduct(type = string1).save()

                print('Запись добавлена!')

        elif num=="2":
                print('Выбрана таблица "Клиенты". Напишите ФИО.')
                string1 = str(input())
                print('Напишите адрес электронной почты.')
                string2 = str(input())
                print('Напишите телефонный номер.')
                string3 = str(input())
                with db:
                    clietns = [{'fio':string1, 'email':string2, 'phone':string3}]
                    Client.insert_many(clietns).execute()

                    print('Запись добавлена!')

        elif num=="3":
                print('Выбрана таблица "Товары". Напишите к какому типу относится данный товар.')
                int1 = int(input())
                print('Напишите наименование товара.')
                string1 = str(input())
                print('Напишите стоимость товара.')
                string2 = str(input())
                print('Напишите количество товара.')
                string3 = str(input())
                with db:
                    typesproduct = TypeProduct.select()
                    products = [{'type_id':typesproduct[int1], 'product_name':string1,
                    'price':string2, 'amount':string3}]
                    Product.insert_many(products).execute()

                    print('Запись добавлена!')

        elif num=="4":
                print('Выбрана таблица "Заказы". Напишите к какому товару относится данный заказ.')
                int1 = int(input())
                print('Напишите к какому клиенту относится данный заказ.')
                int2 = int(input())
                with db:
                    products = Product.select()
                    clietns = Client.select()
                    orders = [{'product_id':products[int1], 'client_id':clietns[int2]}]
                    Order.insert_many(orders).execute()

                    print('Запись добавлена!')
        else:
            print(Fore.RED + 'Введите число от 1 до 4!'+ Fore.RESET)

    elif cmd == "2":
        print('В какой таблице вы хотите удалить запись?\n1) Типы товара\n2) Клиенты\n3) Товары\n4) Заказы')
        num = input()

        if num == "1":
            print('Выбрана таблица "Типы товаров"\nВведите id записи, которую вы хотите удалить.')
            n = input()
            with db:
                delete = TypeProduct.get(TypeProduct.id == n)
                delete.delete_instance()
            print('Запись удалена!')
        elif num == "2":
            print('Выбрана таблица "Клиенты"\nВведите id записи, которую вы хотите удалить.')
            n = input()
            with db:
                delete = Client.get(Client.id == n)
                delete.delete_instance()
            print('Запись удалена!')
        elif num =="3":
            print('Выбрана таблица "Товары"\nВведите id записи, которую вы хотите удалить.')
            n = input()
            with db:
                delete = Product.get(Product.id == n)
                delete.delete_instance()
            print('Запись удалена!')
        elif num == "4":
            print('Выбрана таблица "Заказы"\nВведите id записи, которую вы хотите удалить.')
            n = input()
            with db:
                delete = Order.get(Order.id == n)
                delete.delete_instance()
            print('Запись удалена!')
        else:
            print(Fore.RED + '!!!!!Вы ввели неправильное значение!!!!!!' + Fore.RESET)

    elif cmd == "3":
        print ('В какой таблице вы хотите изменить данные?\n1) Типы товара\n2) Клиенты\n3) Товары\n4) Заказы')
        num = input()

        if num == "1":
            print('Выбрана таблица "Типы товара"\nВведите id записи, которую хотите изменить:')
            q = int(input())
            print('Введите измененный тип товара:')
            s = str(input())
            with db:
                query = TypeProduct.update(type=s).where(TypeProduct.id == q)
                query.execute()
        elif num == "2":
            print('Выбрана таблица "Клиенты"\n Введите название поля, которое хотите изменить:')
            print('1) fio\n2) email\n3) phone')
            strname = input()
            print('Введите id записи, которую хотите изменить:')
            q = int(input())
            print('Введите изменения:')
            s = str(input())
            if strname == "1":
                with db:
                    query = Client.update(fio=s).where(Client.id==q)
                    query.execute()
            elif strname == "2":
                with db:
                    query = Client.update(email=s).where(Client.id==q)
                    query.execute()
            elif strname == "3":
                with db:
                    query = Client.update(phone=s).where(Client.id==q)
                    query.execute()
            else:
                print(Fore.RED + '!!!!!Вы ввели неправильное значение!!!!!!' + Fore.RESET)
        elif num == "3":
            print('Выбрана таблица "Товары"\n Введите название поля, которое хотите изменить:')
            print('1) type_id\n2) product_name\n3) price\n4) amount')
            strname = input()
            print('Введите id записи, которую хотите изменить:')
            q = int(input())
            print('Введите изменения:')
            s = str(input())
            if strname == "1":
                with db:
                    query = Product.update(type_id=s).where(Product.id==q)
                    query.execute()
            elif strname == "2":
                with db:
                    query = Product.update(product_id=s).where(Product.id==q)
                    query.execute()
            elif strname == "3":
                with db:
                    query = Product.update(price=s).where(Product.id==q)
                    query.execute()
            elif strname == "4":
                with db:
                    query = Product.update(amount=s).where(Product.id==q)
                    query.execute()
            else:
                print(Fore.RED + '!!!!!Вы ввели неправильное значение!!!!!!' + Fore.RESET)
        elif num == "4":
            print('Выбрана таблица "Заказы"\n Введите название поля, которое хотите изменить:')
            print('1) product_id\n2) client_id')
            strname = input()
            print('Введите id записи, которую хотите изменить:')
            q = int(input())
            print('Введите изменения:')
            s = str(input())
            if strname == "1":
                with db:
                    query = Order.update(product_id=s).where(Order.id==q)
                    query.execute()
            elif strname == "2":
                with db:
                    query = Order.update(client_id=s).where(Order.id==q)
                    query.execute()
            else:
                print(Fore.RED + '!!!!!Вы ввели неправильное значение!!!!!!' + Fore.RESET)
        else:
            print(Fore.RED + '!!!!!Вы ввели неправильное значение!!!!!!' + Fore.RESET)
    elif cmd == "4":
        print('Какую таблицу вы хотите вывести?\n1) Типы товара\n2) Клиенты\n3) Товары\n4) Заказы')
        num = input()

        if num == "1":
            print('Выбрана таблица "Типы товара":')
            with db:
                query = TypeProduct.select()
                for q in query:
                    print(q.id, q.type)
        elif num == "2":
            print('Выбрана таблица"Клиенты"')
            with db:
                query = Client.select()
                for q in query:
                    print(q.id, q.fio, q.email, q.phone)
        elif num == "3":
            print('Выбрана таблица Товары')
            with db:
                query = Product.select()
                for q in query:
                    print(q.id, q.type_id, q.product_name, q.price, q.amount)
        elif num == "4":
            print('Выбрана таблица "Заказы"')
            with db:
                query = Order.select()
                for q in query:
                    print(q.id, q.product_id, q.client_id)
        else:
            print(Fore.RED + '!!!!!Вы ввели неправильное значение!!!!!!' + Fore.RESET)
    elif cmd == "0":
        break
    else:
        print(Fore.RED + '!!!!!Вы ввели неправильное значение!!!!!!' + Fore.RESET)



# cmd == 0:
#    break




# with db:



# print ('DONE')
# Toster = TypeProduct.create(name='Тостер')
