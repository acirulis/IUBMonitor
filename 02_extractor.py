import datetime
import os
import tarfile
from dbworker import IUBArchive

now = datetime.datetime.now()
year, month, day = now.strftime("%Y,%m,%d").split(',')

day = '26'

filename = '{}_{}_{}.tar.gz'.format(day,month,year)

tar = tarfile.open(filename, "r:gz")
tar.extractall('xmls')
tar.close()

os.remove(filename)



