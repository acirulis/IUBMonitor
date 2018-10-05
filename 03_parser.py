import os
import xmltodict
from dbworker import IUBArchive
import datetime

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
                              created_date=datetime.datetime.fromtimestamp(int(document['creation_date_stamp'])),
                              general_name=document['general']['name'],
                              general_authority_name=document['general']['authority_name'],
                              general_procurement_type=document['general']['procurement_type'],
                              general_price_from=document['general']['price_from'],
                              general_price_to=document['general']['price_to'],
                              main_cpv_code=document['general']['main_cpv']['code'],
                              main_cpv_lv=document['general']['main_cpv']['lv'],
                              )
