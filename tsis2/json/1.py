import json

with open("\Users\admin\OneDrive\Документы\pp2\tsis2\json\sample_data.json") as file:
    y = json.load(file)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in y["imdata"]:
    x = i["l1PhysIf"]
    dict1 = x["attributes"]
    dn = dict1["dn"]
    speed = dict1["speed"]
    mtu = dict1["mtu"]
    y = " "
    if len(dn) == 41:
        y += dn + " " *30 + speed + "   " + mtu
    else:
        y += dn + " " *29 + speed + "   " + mtu
    print(y)