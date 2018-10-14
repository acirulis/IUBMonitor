class ProcessingClass:
    def __init__(self, startdate, enddate):
        self.startdate = startdate
        self.enddate = enddate

    def download_archive(self):
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