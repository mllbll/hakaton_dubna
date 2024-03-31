from django.core.cache import cache
from .database import SessionLocal
from .models import Client
from django.shortcuts import render, redirect
from .models import ClientData
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


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
            error_message = f"Произошла ошибка"
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


def add_client_data(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        fio = request.POST.get('fio')
        balance = request.POST.get('balance')
        lim = request.POST.get('lim')
        status = request.POST.get('status')
        type_face = request.POST.get('type_face')
        payments = request.POST.get('payments')
        expenses = request.POST.get('expenses')
        services = request.POST.get('services')
        adjustment = request.POST.get('adjustment')

        # Создаем сессию
        session = SessionLocal()

        try:
            # Находим запись в таблице ClientData по значению fio
            client_data = session.query(ClientData).filter(ClientData.fio == fio).first()

            # Если запись не найдена, возвращаем ошибку
            if not client_data:
                return render(request, 'error.html', {'error_message': 'Клиент не найден'})

            # Создаем новую запись в таблице Client
            client = Client(
                fk_users_id=client_data.id,
                balance=balance,
                lim=lim,
                status=status,
                type_face=type_face,
                payments=payments,
                expenses=expenses,
                services=services,
                adjustment=adjustment
            )

            # Добавляем запись в сессию и сохраняем изменения
            session.add(client)
            session.commit()

            # Перенаправляем на главную страницу или другую страницу по вашему желанию
            return redirect('home_page')
        except Exception as e:
            # Обработка ошибок
            print(f"Error: {e}")
            # Откатываем транзакцию в случае ошибки
            session.rollback()
        finally:
            # Закрываем сессию
            session.close()

    # Если запрос не POST, просто возвращаем пустую страницу или другую страницу по вашему желанию
    return render(request, 'third_page.html')




@csrf_exempt  # Позволяет обойти CSRF-защиту для этого представления (используется для демонстрации, лучше использовать правильное решение для CSRF)
def delete_user(request):
    if request.method == 'POST':
        fio = request.POST.get('fio')

        # Создаем сессию SQLAlchemy
        session = SessionLocal()

        try:
            # Находим пользователя по FIO
            client_data = session.query(ClientData).filter(ClientData.fio == fio).first()

            # Если пользователь найден, удаляем его и возвращаем успешный ответ
            if client_data:
                # Удаляем связанные с пользователем записи в таблице Client
                session.query(Client).filter(Client.fk_users_id == client_data.id).delete()
                session.commit()

                # Удаляем самого пользователя
                session.delete(client_data)
                session.commit()

                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Пользователь не найден'}, status=404)
        except Exception as e:
            # В случае ошибки возвращаем сообщение об ошибке
            return JsonResponse({'success': False, 'message': 'Произошла ошибка при удалении пользователя'}, status=500)
        finally:
            # Закрываем сессию
            session.close()

    # Если запрос не POST, возвращаем ошибку "Метод не разрешен"
    return JsonResponse({'success': False, 'message': 'Метод не разрешен'}, status=405)


def add_user_page(request):
    return render(request, 'second_page.html')


def edit_user_page(request):
    return render(request, 'third_page.html')
