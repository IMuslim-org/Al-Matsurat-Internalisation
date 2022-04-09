
import csv
import json
import os
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("--dzikir_type", dest="dzikir_type", type=str, help="Please Add Al Matsurat Type")
args = parser.parse_args()

dzikir_type = args.dzikir_type


if dzikir_type == None:
    dzikir_type = "sugro"

__dir__ = os.path.dirname(__file__)

arabic_file_kubro = open(f"{__dir__}/data/kubo.json")
arabic_file_sugro = open(f"{__dir__}/data/sugro.json")

latin_sugro = open(f"{__dir__}/data/latin_al-matsurat_sugro.csv", mode="r")


if dzikir_type == "sugro":
    dzikirData = json.loads(arabic_file_sugro.read())
else:
    dzikirData = json.loads(arabic_file_kubro.read())

with latin_sugro as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # print(csv_reader)

    currentId = 0
    contentsLength = 0
    latins = []

    for row in csv_reader:
        if contentsLength ==0:
            contentsLength = len(dzikirData[currentId]['contents'])
        
        latins.append(row["Latin Text"])

        if len(latins) == contentsLength:
            dzikirData[currentId]['latins'] = latins
            
            latins = []
            contentsLength = 0
            currentId += 1
        
if dzikir_type == "sugro" :
    # arabic_file_sugro.writable = True
    # arabic_file_sugro.writelines
    # print(json.dumps(dzikirData))
    open(f"{__dir__}/data/sugro.json", "w").write(str(list(dzikirData)).replace('\'', '"'))
    # arabic_file_sugro.write(json.dumps(dzikirData))


# print(csv)