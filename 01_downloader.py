from ftplib import FTP
import datetime

ftp = FTP("open.iub.gov.lv")
ftp.login("anonymous", "")

now = datetime.datetime.now()
year, month, day = now.strftime("%Y,%m,%d").split(',')

day = '26'

# template to current file
path = '/{}/{}_{}/{}_{}_{}.tar.gz'.format(year, month, year, day, month, year)
filename = '{}_{}_{}.tar.gz'.format(day, month, year)

try:
    file = open(filename, 'wb')
    ftp.retrbinary('RETR {}'.format(path), file.write)
    file.close()
except Exception as e:
    print(e)
finally:
    ftp.quit()
