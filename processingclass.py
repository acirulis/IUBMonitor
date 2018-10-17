from ftplib import FTP
import datetime
import os
import tarfile
import xmltodict
from dbworker import IUBArchive


class ProcessingClass:

    def __init__(self, date_time_obj):
        if isinstance(date_time_obj, dict):
            self.start_date = date_time_obj[0]
            self.end_date = date_time_obj[1]
        elif isinstance(date_time_obj, datetime.datetime):
            self.start_date = date_time_obj
        else:
            self.start_date = datetime.datetime.today() - datetime.timedelta(1)

    def download_archive(self):
        ftp = FTP("open.iub.gov.lv")
        ftp.login("anonymous", "")
        year, month, day = self.start_date.strftime("%Y,%m,%d").split(',')
        path = '/{}/{}_{}/{}_{}_{}.tar.gz'.format(year, month, year, day, month, year)
        filename = '{}_{}_{}.tar.gz'.format(day, month, year)
        try:
            file = open(filename, 'wb')
            ftp.retrbinary('RETR {}'.format(path), file.write)
            file.close()
            return filename
        except Exception as e:
            print(e)
        finally:
            ftp.quit()

    @staticmethod
    def extract_archive(filename):
        tar = tarfile.open(filename, "r:gz")
        tar.extractall('xmls')
        tar.close()
        os.remove(filename)

    @staticmethod
    def parse_insert():
        for filename in os.listdir('xmls'):
            if filename.endswith('.xml'):
                full_path = os.path.join('xmls', filename)
                print(full_path, ' started')
                with open(full_path, 'r', encoding='utf-8') as f:
                    x = xmltodict.parse(f.read())
                    document = x['document']
                    if document['type'] in ['notice_299_contract', 'notice_299_results', 'notice_299_changes']:
                        continue
                    if not 'price_to' in document['general']:
                        document['general']['price_to'] = None
                    IUBArchive.create(file=filename,
                                      created_date=datetime.datetime.fromtimestamp(
                                          int(document['creation_date_stamp'])),
                                      general_name=document['general']['name'],
                                      general_authority_name=document['general']['authority_name'],
                                      general_procurement_type=document['general']['procurement_type'],
                                      general_price_from=document['general']['price_from'],
                                      general_price_to=document['general']['price_to'],
                                      main_cpv_code=document['general']['main_cpv']['code'],
                                      main_cpv_lv=document['general']['main_cpv']['lv'],
                                      )
