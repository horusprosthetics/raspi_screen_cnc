# d.setSpindleState(SpindleState.OFF)
# print("Spindle stopped")

import os
import json
import requests
# Comment this:
from ___GUI import Gui
from ___DEVICE import Device, State, Axis
d = Device()
gui = Gui(d.getComm())
# Until here

filepath = d.getGCodeFilePath()
# C:\Users\Horus Server\Desktop\Mateo\CNC_Automation\autoCNC\ORDERS\order_UA000014_TF001_BER01_10112023\order_UA000014_TF001_BER01_10112023.tap

filepath_dirname = os.path.splitext(os.path.dirname(filepath))[0]
# C:\Users\Horus Server\Desktop\Mateo\CNC_Automation\autoCNC\ORDERS\order_UA000016_TF001_BER01_10112023
print(filepath_dirname)

basename_without_tap = os.path.splitext(os.path.basename(filepath))[0]
# order_UA000014_TF001_BER01_10112023
print(basename_without_tap)

# Here we need to get the active directory

# open config file
f = open('./SCRIPTS/' + 'config.json', 'r')
config = json.loads(f.read())


url = config['baseURL']

print("trying to open ===>", filepath_dirname + "\\" + basename_without_tap + '.tap')
d = open(filepath_dirname + "\\" + basename_without_tap + '.json', 'r')
order_data = json.loads(d.read())

recordId = order_data["id"]

headers = {"Content-Type": "application/json", "Authorization": ""}

data = {"Is_Milled": "TRUE"}

# Send the patch request with the updated JSON data
response = requests.patch(url + "/" + recordId, headers=headers, json=data)

if response.status_code == 200:
    print("Output_data PATCHed successfully back to database and JSON file updated.")
else:
    print("Failed to update database with Output_data !!!")
