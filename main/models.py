# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy import Column, Integer, String
# # from .database import Base
# # from django.db import models
# # #
# # # # from django.db import models
# # #
# # #
# # # from sqlalchemy import Column, Integer, String, ForeignKey
# # # from sqlalchemy.orm import relationship
# # # from sqlalchemy.ext.declarative import declarative_base
# # #
# # # Base = declarative_base()
# # #
# # #
# # # class Product(Base):
# # #     __tablename__ = 'client'
# # #
# # #     id = Column(Integer, primary_key=True)
# # #     balance = Column(Integer)
# # #     lim = Column(Integer)
# # #     status = Column(String)
# # #     type_face = Column(String)
# # #     payments = Column(String)
# # #     expenses = Column(Integer)
# # #     services = Column(String)
# # #     adjustment = Column(String)
# # #
# # #     # Связь с таблицей Product через fk_users_id
# # #     client_data = relationship("Product", back_populates="product")
# # #
# # #
# # # class Product(Base):
# # #     __tablename__ = 'client_data'
# # #
# # #     id = Column(Integer, primary_key=True)
# # #     org_name = Column(String)
# # #     fio = Column(String)
# # #     phone_number = Column(String)
# # #     email = Column(String)
# # #     birthday_date = Column(String)
# # #     connection_address = Column(String)
# # #
# # #     # Связь с таблицей Product через fk_users_id
# # #     product = relationship("Product", back_populates="client_data")
# # #     fk_users_id = Column(Integer, ForeignKey('client.fk_users_id'))  # Столбец fk_users_id в таблице client_data ссылается на fk_users_id таблицы client
# # #
# # #
# # # class Product_1(models.Model):
# # #     id = models.IntegerField(primary_key=True, db_column='id')
# # #     balance = models.IntegerField(db_column='balance')
# # #     lim = models.IntegerField(db_column='lim')
# # #     status = models.CharField(max_length=255, db_column='status')
# # #     type_face = models.CharField(max_length=255, db_column='type_face')
# # #     payments = models.CharField(max_length=255, db_column='payments')
# # #     expenses = models.IntegerField(db_column='expenses')
# # #     services = models.CharField(max_length=255, db_column='services')
# # #     adjustment = models.CharField(max_length=255, db_column='adjustment')
# # #
# # #     class Meta:
# # #         managed = False
# # #         db_table = 'client'
# #
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy import Column, Integer, String, ForeignKey
# # from sqlalchemy.orm import relationship
# # from .database import Base
# #
# # from sqlalchemy import Column, Integer, String, ForeignKey
# # from sqlalchemy.orm import relationship
# # from .database import Base
# #
# # Base = declarative_base()
# #
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from .database import Base
# from django.db import models
#
#
# class ClientData(Base):
#     __tablename__ = 'client'
#
#     id = Column(Integer, primary_key=True)
#     balance = Column(Integer)
#     lim = Column(Integer)
#     status = Column(String)
#     type_face = Column(String)
#     payments = Column(String)
#     expenses = Column(Integer)
#     service = Column(String)
#     adjustment = Column(String)
#     fk_users_id = Column(Integer, ForeignKey('client_data.id'))
#
#     client_data = relationship("Product", back_populates="client")
#
#
# class Product(Base):
#     __tablename__ = 'client_data'
#
#     id = Column(Integer, primary_key=True)
#     org_name = Column(String)
#     fio = Column(String)
#     phone_number = Column(String)
#     email = Column(String)
#     birthday_date = Column(String)
#     connection_address = Column(String)
#
#     client = relationship("ClientData", back_populates="client_data")
#
#
# class Product_1(models.Model):
#     id = models.IntegerField(primary_key=True, db_column='id')
#     balance = models.IntegerField(db_column='balance')
#     lim = models.IntegerField(db_column='lim')
#     status = models.CharField(max_length=255, db_column='status')
#     type_face = models.CharField(max_length=255, db_column='type_face')
#     payments = models.CharField(max_length=255, db_column='payments')
#     expenses = models.IntegerField(db_column='expenses')
#     services = models.CharField(max_length=255, db_column='services')
#     adjustment = models.CharField(max_length=255, db_column='adjustment')
#
#     class Meta:
#         managed = False
#         db_table = 'client'

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class ClientData(Base):
    __tablename__ = 'client_data'

    id = Column(Integer, primary_key=True, index=True)
    org_name = Column(String)
    fio = Column(String)
    phone_number = Column(String)
    email = Column(String)
    birthday_date = Column(Date)
    connection_address = Column(String)

    # Определяем отношение между таблицами client_data и client
    clients = relationship("Client", back_populates="client_data")



class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Integer)
    adjustment = Column(String)
    lim = Column(Integer)
    status = Column(String)
    type_face = Column(String)
    payments = Column(String)
    expenses = Column(Integer)
    services = Column(String)

    # Определяем отношение между таблицами client и client_data
    fk_users_id = Column(Integer, ForeignKey('client_data.id'))
    client_data = relationship("ClientData", back_populates="clients")

