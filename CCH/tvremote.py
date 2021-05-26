import samsung_tv


class TVRemote:
    def __init__(self):
        # self.tv = samsung_tv.SamsungTV('192.168.0.6', '12845350')
        pass

    def power(self):
        self.tv.power()

    def up_tv(self):
        self.tv.up()

    def down_tv(self):
        self.tv.down()

    def volumen_up_tv(self):
        self.tv.volume_up()

    def volumen_down_tv(self):
        self.tv.volume_down()
