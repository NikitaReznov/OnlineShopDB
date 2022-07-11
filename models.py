from peewee import *

# Создание БД
db = SqliteDatabase('database.db')

# Создание базовой модели


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

# Создние таблиц


class TypeProduct(BaseModel):
    type = CharField()

    class Meta:
        db_table = 'typesproduct'


class Product(BaseModel):
    type_id = ForeignKeyField(TypeProduct)
    product_name = CharField()
    price = FloatField()
    amount = FloatField()

    class Meta:
        db_table = 'products'


class Client(BaseModel):
    fio = CharField()
    email = CharField()
    phone = CharField()

    class Meta:
        db_table = 'clietns'


class Order(BaseModel):
    product_id = ForeignKeyField(Product)
    client_id = ForeignKeyField(Client)

    class Meta:
        db_table = 'orders'
