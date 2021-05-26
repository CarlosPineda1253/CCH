import samsung_tv

class TV_Remote():
    def __init__(self):
        self.tv = samsung_tv.SamsungTV('192.168.0.6', '12845350')

    def power_tv(self, event):
        self.tv.power()

    def up_tv(self, event):
        self.tv.up()

    def down_tv(self, event):
        self.tv.down()