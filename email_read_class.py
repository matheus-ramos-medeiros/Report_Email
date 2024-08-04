from datetime import datetime, timedelta
from imbox import Imbox
import json
import os
import re

class MatheusMail:
    def __init__(self,
              credentials_path: str ,
              host: str = 'imap.gmail.com'):
        with open( credentials_path , 'r') as f:
            credentials_data = json.load(f)

        self.host = host 
        self.email = credentials_data['email']
        self.password = credentials_data['google_password']

        self.data_path = 'data/'

    def read_csv(self):
        if not os.path.exists(self.data_path):
            os.mkdir(self.data_path)

        with Imbox(self.host,username = self.email , password = self.password) as imbox:
            relatorio = imbox.messages(subject = 'Importante')
            anexo = relatorio[-1][1].attachments[0]

            report_data = anexo.get('content')
            filename = anexo.get('filename')
            self.filepath = os.path.join(self.data_path , filename)

            with open(self.filepath, 'wb') as fp:
                fp.write(report_data.read())


if __name__ =='__main__':
    Mailer = MatheusMail('creds.json')
    Mailer.read_csv()


