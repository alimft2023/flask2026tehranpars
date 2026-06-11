from peewee import SqliteDatabase, Model, IntegerField, CharField

db = SqliteDatabase("mft.db")


class Student(Model):
    sname = CharField(max_length=15)
    sfamily = CharField(max_length=20)
    age = IntegerField()

    class Meta:
        database = db
        db_table = "st"


# Student.create_table()
db.create_tables([Student])
