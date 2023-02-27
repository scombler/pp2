import json

x = open("sample.json")
y = json.load(x)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in y["imdata"]:
    z = i["l1PhysIf"]
    w = z["attributes"]
    dn = w["dn"]
    speed = w["speed"]
    mtu = w["mtu"]
    res = " "
    if len(dn) == 41:
        res += dn + " " *30 + speed + "   " + mtu
    else:
        res += dn + " " *29 + speed + "   " + mtu
    print(res)