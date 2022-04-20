from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

############ Uncomment the following 4 lines if you are running for the first time, it will save your google account credentials in a pickle file
# scopes = ['https://www.googleapis.com/auth/calendar']
# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
# credentials = flow.run_console()
# pickle.dump(credentials, open("token.pkl", "wb")) 

############ Comment out the first part and uncomment the following after you saved your credentials to pull data
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()
calendar_id = result['items'][0]['id']
result = service.events().list(calendarId=calendar_id).execute()
print(result['items'][1]['start']['dateTime'])
