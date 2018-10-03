import datetime
import os
import tarfile

now = datetime.datetime.now()
year, month, day = now.strftime("%Y,%m,%d").split(',')

day = '02'

filename = '{}_{}_{}.tar.gz'.format(day,month,year)

tar = tarfile.open(filename, "r:gz")
tar.extractall('xmls')
tar.close()

os.remove(filename)



