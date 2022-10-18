from __future__ import print_function
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from config import *


class GoogleSheet:

    SPREADSHEET_ID = idLink
    SCOPES = link
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValues(self, range, values):
        dataForUpdate = [{
            'range': range,
            'values': values
        }]
        bodyForUpdate = {
            'valueInputOption': 'USER_ENTERED',
            'data': dataForUpdate
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId = self.SPREADSHEET_ID,
                                                                  body = bodyForUpdate).execute()
    
    def clearAllSheet(self):
        rangeAll = 'List1!A1:Z'.format(self.SCOPES)
        bodyForClear = {}
        resultClear = self.service.spreadsheets().values().clear(spreadsheetId = self.SPREADSHEET_ID, range = rangeAll,
                                                       body = bodyForClear).execute()


def importToSheet(range,values):
    GoogleSheet().updateRangeValues(range, values)

def clearingSheet():
    GoogleSheet().clearAllSheet()