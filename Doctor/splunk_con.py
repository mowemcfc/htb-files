#!/usr/bin/python3

import splunklib.client as client

HOST = "10.129.11.123"
PORT = 8089
USERNAME = "admin"
PASSWORD = "admin"

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Print installed apps to the console to verify login
for app in service.apps:
    print(app.name)
