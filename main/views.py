from django.shortcuts import render, redirect
# from .models import Product, Product
from main.database import SessionLocal
from django.core.cache import cache


# def input_values(request):
#     error_message = None
#     balance = None
#     lim = None
#     status = None
#     type_face = None
#     payments = None
#     expenses = None
#     services = None
#     adjustment = None
#
#     if request.method == 'POST':
#         # Получаем значение fio из POST-запроса
#         fio = request.POST.get('fio')
#
#         # Создаем сессию
#         session = SessionLocal()
#
#         try:
#             # Получаем client_data_row из таблицы client_data по значению fio
#             client_data_row = session.query(Product).filter_by(fio=fio).first()
#
#             if client_data_row:
#                 fk_users_id = client_data_row.fk_users_id
#
#                 # Получаем данные из таблицы client по fk_users_id
#                 client_info = session.query(Product).filter_by(id=fk_users_id).first()
#
#                 if client_info:
#                     # Получаем значения нужных столбцов
#                     balance = client_info.balance
#                     lim = client_info.lim
#                     status = client_info.status
#                     type_face = client_info.type_face
#                     payments = client_info.payments
#                     expenses = client_info.expenses
#                     services = client_info.services
#                     adjustment = client_info.adjustment
#
#                     # Сохраняем значения в кэш
#                     cache.set('balance', balance)
#                     cache.set('lim', lim)
#                     cache.set('status', status)
#                     cache.set('type_face', type_face)
#                     cache.set('payments', payments)
#                     cache.set('expenses', expenses)
#                     cache.set('services', services)
#                     cache.set('adjustment', adjustment)
#
#                 else:
#                     error_message = "Данные о продукте не найдены"
#             else:
#                 error_message = "Клиент с таким ФИО не найден"
#         except Exception as e:
#             # Обработка ошибок
#             error_message = "Произошла ошибка при обращении к базе данных"
#             print(f"Error: {e}")
#         finally:
#             # Закрываем сессию
#             session.close()
#
#     return render(request, 'input_product_id.html', {
#         'error_message': error_message,
#         'balance': balance,
#         'lim': lim,
#         'status': status,
#         'type_face': type_face,
#         'payments': payments,
#         'expenses': expenses,
#         'services': services,
#         'adjustment': adjustment
#     })
#
#
#
# def add_user_data(request):
#     if request.method == 'POST':
#         org_name = request.POST.get('organization_name')
#         fio = request.POST.get('fio')
#         phone_number = request.POST.get('phone_number')
#         email = request.POST.get('email')
#         birthday_date = request.POST.get('birthday_date')
#         connection_address = request.POST.get('connection_address')
#
#         # Создаем сессию SQLAlchemy
#         session = SessionLocal()
#
#         try:
#             # Получаем fk_users_id (client_id) из таблицы client по значению fio
#             client_id = session.query(Product).filter_by(fio=fio).first().fk_users_id
#
#             # Создаем объект Product с использованием client_id для связи с таблицей client
#             client_data = Product(
#                 org_name=org_name,
#                 fio=fio,
#                 phone_number=phone_number,
#                 email=email,
#                 birthday_date=birthday_date,
#                 connection_address=connection_address,
#                 client_id=client_id  # Используем полученный fk_users_id (client_id) для связи
#             )
#
#             # Добавляем объект в сессию и сохраняем его в базе данных
#             session.add(client_data)
#             session.commit()
#
#             # Можно выполнить другие действия, например, перенаправление на страницу с подтверждением или домашнюю страницу.
#             return redirect('home_page')
#         except Exception as e:
#             # Обработка ошибок
#             print(f"Error: {e}")
#             # Откатываем транзакцию в случае ошибки
#             session.rollback()
#         finally:
#             # Закрываем сессию
#             session.close()
#
#     # Если запрос не POST, просто возвращаем пустую страницу
#     return render(request, 'second_page.html')
#
# def add_user_page(request):
#     return render(request, 'second_page.html')

from django.shortcuts import render, redirect
from .models import ClientData  # Импортируем модели Product и ClientData
from main.database import SessionLocal
from django.core.cache import cache

# def input_values(request):
#     error_message = None
#     balance = None
#     lim = None
#     status = None
#     type_face = None
#     payments = None
#     expenses = None
#     services = None
#     adjustment = None
#
#     if request.method == 'POST':
#         # Получаем значение fio из POST-запроса
#         fio = request.POST.get('fio')
#
#         # Создаем сессию
#         session = SessionLocal()
#
#         try:
#             # Получаем id из таблицы client_data по значению fio
#             client_data_row = session.query(ClientData).filter_by(fio=fio).first()
#
#             if client_data_row:
#                 fk_users_id = client_data_row.id
#
#                 # Получаем данные из таблицы client по fk_users_id
#                 client_info = session.query(Product).filter_by(fk_users_id=fk_users_id).first()
#
#                 if client_info:
#                     # Получаем значения нужных столбцов
#                     balance = client_info.balance
#                     lim = client_info.lim
#                     status = client_info.status
#                     type_face = client_info.type_face
#                     payments = client_info.payments
#                     expenses = client_info.expenses
#                     services = client_info.services
#                     adjustment = client_info.adjustment
#
#                     # Сохраняем значения в кэш
#                     cache.set('balance', balance)
#                     cache.set('lim', lim)
#                     cache.set('status', status)
#                     cache.set('type_face', type_face)
#                     cache.set('payments', payments)
#                     cache.set('expenses', expenses)
#                     cache.set('services', services)
#                     cache.set('adjustment', adjustment)
#
#                 else:
#                     error_message = "Данные о продукте не найдены"
#             else:
#                 error_message = "Клиент с таким ФИО не найден"
#         except Exception as e:
#             # Обработка ошибок
#             error_message = "Произошла ошибка при обращении к базе данных"
#             print(f"Error: {e}")
#         finally:
#             # Закрываем сессию
#             session.close()
#
#     return render(request, 'input_product_id.html', {
#         'error_message': error_message,
#         'balance': balance,
#         'lim': lim,
#         'status': status,
#         'type_face': type_face,
#         'payments': payments,
#         'expenses': expenses,
#         'services': services,
#         'adjustment': adjustment
#     })
def input_values(request):
    error_message = None
    balance = None
    lim = None
    status = None
    type_face = None
    payments = None
    expenses = None
    services = None
    adjustment = None

    if request.method == 'POST':
        # Получаем значение fio из POST-запроса
        fio = request.POST.get('fio')

        # Создаем сессию
        session = SessionLocal()

        try:
            # Выполняем запрос к базе данных
            client_data = session.query(ClientData).filter(ClientData.fio == fio).first()

            # Если клиентные данные не найдены, возвращаем ошибку
            if not client_data:
                error_message = "Не найдено совпадений по ФИО"
            else:
                # Получаем коллекцию клиентов через связь с ClientData
                clients = client_data.clients

                # Получаем первого клиента из коллекции, если она не пуста
                if clients:
                    client = clients[0]

                    # Получаем значения нужных столбцов
                    balance = client.balance
                    lim = client.lim
                    status = client.status
                    type_face = client.type_face
                    payments = client.payments
                    expenses = client.expenses
                    services = client.services
                    adjustment = client.adjustment

                    # Сохраняем значения в кэш
                    cache.set('balance', balance)
                    cache.set('lim', lim)
                    cache.set('status', status)
                    cache.set('type_face', type_face)
                    cache.set('payments', payments)
                    cache.set('expenses', expenses)
                    cache.set('services', services)
                    cache.set('adjustment', adjustment)
                else:
                    error_message = "Не найдено совпадений по ФИО"
        except Exception as e:
            # Обработка ошибок
            error_message = f"Произошла ошибка: {e}"
        finally:
            # Закрываем сессию
            session.close()

    return render(request, 'input_product_id.html', {
        'error_message': error_message,
        'balance': balance,
        'lim': lim,
        'status': status,
        'type_face': type_face,
        'payments': payments,
        'expenses': expenses,
        'services': services,
        'adjustment': adjustment
    })


def add_user_data(request):
    if request.method == 'POST':
        org_name = request.POST.get('organization_name')
        fio = request.POST.get('fio')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        birthday_date = request.POST.get('birthday_date')
        connection_address = request.POST.get('connection_address')

        # Создаем сессию SQLAlchemy
        session = SessionLocal()

        try:
            # Создаем объект ClientData с использованием данных из формы
            client_data = ClientData(
                org_name=org_name,
                fio=fio,
                phone_number=phone_number,
                email=email,
                birthday_date=birthday_date,
                connection_address=connection_address
            )

            # Добавляем объект в сессию и сохраняем его в базе данных
            session.add(client_data)
            session.commit()

            # Можно выполнить другие действия, например, перенаправление на страницу с подтверждением или домашнюю страницу.
            return redirect('home_page')
        except Exception as e:
            # Обработка ошибок
            print(f"Error: {e}")
            # Откатываем транзакцию в случае ошибки
            session.rollback()
        finally:
            # Закрываем сессию
            session.close()

    # Если запрос не POST, просто возвращаем пустую страницу
    return render(request, 'second_page.html')

def add_user_page(request):
    return render(request, 'second_page.html')
