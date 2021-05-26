from pywebostv.discovery import *    # Because I'm lazy, don't do this.
from pywebostv.connection import *
from pywebostv.controls import *
from wakeonlan import send_magic_packet

#send_magic_packet('40:2F:86:DE:D4:6A')

store = {'client_key': u'd208233ace21685b0e801fd1550f18b6'}

# Scans the current network to discover TV. Avoid [0] in real code. If you already know the IP,
# you could skip the slow scan and # instead simply say:
client = WebOSClient("192.168.0.8")
client.connect()
for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("Please accept the connect on the TV!")
    elif status == WebOSClient.REGISTERED:
        print("Registration successful!")

# Keep the 'store' object because it contains now the access token
# and use it next time you want to register on the TV.
print(store)   # {'client_key': 'ACCESS_TOKEN_FROM_TV'}

media = MediaControl(client)
media.volume_up()          # Increase the volume by 1 unit. Doesn't return anything

system = SystemControl(client)
system.notify("This is a notification message!")  # Show a notification message on the TV.
system.power_off()

