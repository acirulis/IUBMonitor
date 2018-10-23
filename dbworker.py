"""
ORM from http://docs.peewee-orm.com/en/latest/index.html
"""
from peewee import *
from datetime import datetime
import os

DB_FILE = os.path.join(os.path.dirname(__file__), 'iub.sqlite')


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(DB_FILE)


class IUBArchive(BaseModel):
    file = CharField(primary_key=True)
    parsed_date = DateField(default=datetime.now)
    created_date = DateTimeField(default=datetime.now)
    general_name = CharField(max_length=500)
    general_authority_name = CharField(max_length=500)
    general_procurement_type = CharField()
    general_price_from = CharField(null=True)
    general_price_to = CharField(null=True)
    main_cpv_code = CharField(null=True, index=True)
    main_cpv_lv = CharField(null=True)
    is_processed = BooleanField(default=False)


if __name__ == "__main__":
    db = SqliteDatabase(DB_FILE)
    db.create_tables([IUBArchive])
    if (True):  # debug - lets insert & select record
        try:
            IUBArchive.create(file="test.xml", general_name="Test iepirkums", general_authority_name="SIA",
                              general_procurement_type=1)
        except Exception as e:
            print('ERRR: ', e)
        print(IUBArchive.get(IUBArchive.file == 'test.xml').created_date)
