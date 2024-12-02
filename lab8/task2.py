from peewee import *
from datetime import date

db = SqliteDatabase("orders.db")

class Transport(Model):
    id_transport = PrimaryKeyField()
    mark = TextField()
    registration_date = DateField()
    color = TextField()

    class Meta:
        database = db

class Recevier(Model):
    id_recevier = PrimaryKeyField()
    last_name = TextField()
    first_name = TextField()
    patronymic_name = TextField()
    date_of_birth = DateField()
    index = TextField()
    city = TextField()
    street = TextField()
    house = TextField()
    apartment = TextField()
    phone_number = TextField()

    class Meta:
        database = db

class Order(Model):
    id_order = PrimaryKeyField()
    id_sender = IntegerField()
    id_recevier = IntegerField() 
    order_date = DateField()
    delivery_date = DateField()
    delivery_price = FloatField()
    id_courier = IntegerField()
    id_transport = IntegerField()

    class Meta:
        database = db

if __name__ == "__main__":
    db.create_tables([Transport, Recevier, Order])
    sample_transport1 = Transport(mark="ford", registration_date=date(2022, 9, 13), color="white")
    sample_transport1.save()
    sample_transport2 = Transport(mark="audi", registration_date=date(1999, 5, 1), color="green")
    sample_transport2.save()
    sample_recevier1 = Recevier(last_name="Fedorov", first_name="Fedor", patronymic_name="Fedorovich", date_of_birth=date(1955, 3, 9),
                                index="333111", city="Moscow", street="Bolshoy val", house="3", apartment="1", phone_number="123456")
    sample_recevier1.save()
    sample_recevier2 = Recevier(last_name="Alexandrov", first_name="Alexandr", patronymic_name="Alexandrovich", date_of_birth=date(1967, 7, 1),
                                index="156789", city="Moscow", street="Tenistay", house="29", apartment="13", phone_number="89315054291")
    sample_recevier2.save()
    order1 = Order(id_sender=1, id_recevier=1, order_date=date(2024, 11, 15), delivery_date=date(2024, 11, 16),
                    delivery_price=100.50, id_courier=1, id_transport=2)
    order1.save()
    order1 = Order(id_sender=1, id_recevier=2, order_date=date(2024, 11, 14), delivery_date=date(2024, 11, 15),
                    delivery_price=131.23, id_courier=1, id_transport=1)
    order1.save()
    
