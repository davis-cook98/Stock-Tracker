#https://gspread.readthedocs.io/en/latest/
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Used to communicate with Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Stock-Tracker Backend").sheet1
#Row, Column for writing
