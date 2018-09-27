"""
ORM from http://docs.peewee-orm.com/en/latest/index.html
"""
from peewee import *
import datetime


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('iub.sqlite')


class IUBArchive(BaseModel):
    file = CharField(primary_key=True)
    created_date = DateField(default=datetime.datetime.now)
    is_processed = BooleanField(default=False)


if __name__ == "__main__":
    db.connect()
    db.create_tables([IUBArchive])
    # IUBArchive.create(file="1234.xml")
    # IUBArchive.get(IUBArchive.file == '1234.xml').created_date
