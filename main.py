import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.environ.get('TOKEN')
PIXELA_USERNAME = os.environ.get('PIXELA_USERNAME')
#-----------------------CREATE PIXELA USER-----------------------#
pixela_endpoint = 'https://pixe.la/v1/users'

user_parameters = {
    "token": TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

#response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)
#-----------------------CREATE PIXELA GRAPH-----------------------#
graph_endpoint = f'https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs'


graph_params = {
    #Tweak parameters according to your desired graph
    'id': 'hbttrck01',
    'name': 'Gym Tracker Graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#--------------------COMMIT PIXEL TO YOUR GRAPH-----------------#
add_pixel_endpoint = f'{graph_endpoint}/hbttrck01'
today = datetime.today().strftime('%Y%m%d')
pixel_parameters = {
    'date': today,
    'quantity': '1'
}
#response = requests.post(url=add_pixel_endpoint, json=pixel_parameters, headers=headers)
#-------------------UPDATE EXISTING PIXEL VALUE---------------#
update_endpoint = f'{add_pixel_endpoint}/20230418/'
#Adjust date and quantity to your needs
update_params = {
    'quantity':'0'
}
#response = requests.put(url=update_endpoint, json=update_params,headers=headers)
#----------------DELETE PIXEL---------------------#
#response = requests.put(url=update_endpoint,headers=headers)
#print(response.text)