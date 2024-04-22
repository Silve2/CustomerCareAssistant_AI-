import gspread
from oauth2client.service_account import ServiceAccountCredentials


# set scopes
scope = ["https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file"]

# add credentials from file
creds = ServiceAccountCredentials.from_json_keyfile_name("ticketing.json", scope)

# authorization
client = gspread.authorize(creds)

# open file sheet
sheet = client.open_by_key('YOUR_SHEET_ID').sheet1


def inserisci_ticket(nome, email, testo, data):
    row_to_insert = [nome, email, testo, data]
    sheet.append_row(row_to_insert)
