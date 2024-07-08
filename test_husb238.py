from HUSB238 import HUSB238
#import smbus
#i2c = smbus.SMBus(1) # raspberry pi

import machine
i2c = machine.I2C(1,sda=machine.Pin(6), scl=machine.Pin(7), freq=400000) #xiao rp2040

USB_PD = HUSB238(i2c=i2c, debug=True)
print(USB_PD.get_src_cap())
USB_PD.select_cap(5)