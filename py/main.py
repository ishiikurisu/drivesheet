import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('../config/secrets.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('qotsa').sheet1
    members = sheet.get_all_records()
    print(members)
    print(sheet.row_values(3))
    print(sheet.col_values(3))
    print(sheet.cell(2, 3)) # 2nd row, third col
    sheet.update_cell(2, 3, 'Guitar and Vocals')
    print(sheet.get_all_records())
    sheet.update_cell(2, 3, 'Guitar')
    print(sheet.get_all_records())

    row = [6, 'Jon Theodore', 'Drums']
    sheet.insert_row(row, row[0]+1)
    print(sheet.get_all_records())
    sheet.delete_row(row[0]+1)
    print(sheet.get_all_records())
    print(sheet.row_count)

if __name__ == '__main__':
    main()
