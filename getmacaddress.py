from getmac import get_mac_address as gma
mac_address= "40:23:43:E8:F3:69"
currentMac= str(gma())
print(mac_address.lower())
print(currentMac)

if currentMac==mac_address.lower():
    print("Welcome")