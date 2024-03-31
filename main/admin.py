# from django.contrib import admin
# from .models import Product_1
# from django.core.cache import cache
# from main.views import input_values
#
#
# class ProductAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         # Получаем значения переменных из кэша
#         balance = cache.get('balance')
#         lim = cache.get('lim')
#         status = cache.get('status')
#         type_face = cache.get('type_face')
#         payments = cache.get('payments')
#         expenses = cache.get('expenses')
#         services = cache.get('service')
#         adjustment = cache.get('adjustment')
#
#         # Если хотя бы одно значение отсутствует в кэше, вернем пустой QuerySet
#         if None in (balance, lim, status, type_face, payments, expenses, services, adjustment):
#             return Product_1.objects.none()
#
#         # Возвращаем QuerySet с фильтрацией по значениям переменных
#         return Product_1.objects.filter(balance=balance, lim=lim, status=status, type_face=type_face, payments=payments,
#                                       expenses=expenses, services=services, adjustment=adjustment)
#
#
# # Регистрируем модель и связанный с ней класс администратора
# admin.site.register(Product_1, ProductAdmin)