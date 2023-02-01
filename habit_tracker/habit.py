import requests
import datetime as dt
user_endpoint = "https://pixe.la/v1/users"
token =  "thegoblinmasterofthegalaxy"
username = "YOUR_USERNAME"
graph1_id = "graph1"
create_user = {
    "token":token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=user_endpoint, json=create_user)
# print(response.text)

graph_endpoint = f"{user_endpoint}/{username}/graphs"
create_graph = {
    "id": graph1_id,
    "name": "coding habit tracker",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
    "timezone": "Asia/Kolkata",
}

headers = {
    "X-USER-TOKEN": token,
}
# reponse = requests.post(url=graph_endpoint, json= create_graph, headers = headers)
# print(reponse.text)

pixel_endpoint = f"{user_endpoint}/{username}/graphs/{graph1_id}"

today_date = str(dt.datetime.date(dt.datetime.now())).replace("-","")


create_pixel = {
    "date": today_date,
    "quantity": "1000.5",
}

# reponse = requests.put(url=pixel_endpoint, json=create_pixel, headers=headers)
# print(reponse.text)

new_data = {
    "quantity": "10.0",
}
update_pixel = requests.put(url=f"{user_endpoint}/{username}/graphs/{graph1_id}/{today_date}", json=new_data, headers=headers)
print(update_pixel.text)

delete_pixel = requests.delete(url=f"{user_endpoint}/{username}/graphs/{graph1_id}/20230131",headers=headers)
