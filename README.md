# HUSB238_I2C
Python driver for I2C control of HUSB238 [Adafruit $6 board](https://www.adafruit.com/product/5807)

![picture](https://cdn-shop.adafruit.com/970x728/5807-04.jpg)

Python driver for I2C interface, works on both Raspberry Pi and MicroPython. Pull-up resistors to 3.3V are needed for both SDA and SCL (not on the board) as well as a GND connection (never forget to share ground between HUSB238 and Raspberry Pi). I was hoping to use PPS, but HUSB238 does not support it. I use this for automated battery charger IC testing (using real world wall adapters).
