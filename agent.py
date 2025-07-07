import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

#Define API scopes
# Tells Google which APIs I want this code to access
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

#Load credentials
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)

#Create a client that can make API calls to Google Sheets
client = gspread.authorize(creds)

#Open spreadsheet and select individual sheets
spreadsheet = client.open("Compra y menu")
product_sheet = spreadsheet.worksheet("AgentDB")
shopping_sheet = spreadsheet.worksheet("Lista")

#Get all records into dataframes
product_df = pd.DataFrame(product_sheet.get_all_records())
shopping_df = pd.DataFrame(shopping_sheet.get_all_records())

#Print everything
print(product_df)
print(shopping_df)