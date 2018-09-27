"""
ORM from http://docs.peewee-orm.com/en/latest/index.html
"""
from peewee import *
import datetime

DB_FILE = 'iub.sqlite'

class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(DB_FILE)


class IUBArchive(BaseModel):
    file = CharField(primary_key=True)
    created_date = DateField(default=datetime.datetime.now)
    is_processed = BooleanField(default=False)


if __name__ == "__main__":
    db = SqliteDatabase(DB_FILE)
    db.create_tables([IUBArchive])
    if (True): # debug - lets insert & select record
        try:
            IUBArchive.create(file="test.xml")
        except IntegrityError as e:
            print('Record already inserted')
        print(IUBArchive.get(IUBArchive.file == 'test.xml').created_date)
