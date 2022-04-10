import json
import os
import argparse

from matplotlib.font_manager import json_dump, json_load


parser = argparse.ArgumentParser()
parser.add_argument("--dzikir_type", dest="dzikir_type", type=str, help="Please Add Al Matsurat Type")
args = parser.parse_args()

dzikir_type = args.dzikir_type


if dzikir_type == None:
    dzikir_type = "sugro"

__dir__ = os.path.dirname(__file__)

arabic_file_kubro = open(f"{__dir__}/data/kubro.json")
arabic_file_sugro = open(f"{__dir__}/data/sugro.json")

if dzikir_type == "sugro":
    dzikirData = json.loads(arabic_file_sugro.read())
else:
    dzikirData = json.loads(arabic_file_kubro.read())

dhikrSections = {}

count = 0
currentId = 0
for dhikrIdSection in dzikirData:
    currentId = dhikrIdSection['id']
    print(currentId)

    for i in range(len(dhikrIdSection['contents'])):
        contents = dhikrIdSection['contents'][i]
        dhikrSections[str(count)] = f"{currentId}.{i}"
        
        count+=1

open(f"{__dir__}/data/{dzikir_type}_section.json", "w").write(str(dhikrSections).replace("'", "\""))
