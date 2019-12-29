def show(name='Your Name Here'):
    import machine
    import ssd1306
    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
    oled = ssd1306.SSD1306_I2C(128, 32, i2c)
    oled.fill(0)
    oled.text(name, 0, 0, 2)
    oled.show()
