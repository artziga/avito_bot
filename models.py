import datetime

import peewee
from peewee import SqliteDatabase, Model, TextField, DateTimeField, PrimaryKeyField, CharField, \
    IntegerField, BooleanField, TimestampField

db = SqliteDatabase('parser.db')


class BaseModel(Model):
    class Meta:
        database = db

class Advertisement(BaseModel):
    id = PrimaryKeyField(primary_key=True)
    id_avito = IntegerField(unique=True)
    url = CharField()
    name = CharField()
    description = TextField()
    category = CharField() #разделить
    location = CharField() #разделить
    time = DateTimeField()
    price = IntegerField() #разделить
    images = TextField() #разделить
    address = CharField()
    phone = BooleanField()
    delivery = BooleanField()
    message = BooleanField()
    parameters = CharField()
    coords_lat = IntegerField()
    coords_lng = IntegerField()
    created = DateTimeField(default=datetime.datetime.now)
    updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'Advertisements'
        order_by = 'id'
