def show_all():
    import machine
    import ssd1306
    from decouple import config
    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
    oled = ssd1306.SSD1306_I2C(128, 32, i2c)
    oled.fill(0)
    oled.text(config('NAMETAG_HEADER', ''), 0, 0)
    oled.text(config('NAMETAG_BODY', ''), 0, 12)
    oled.text(config('NAMETAG_FOOTER', ''), 0, 24)
    oled.show()
