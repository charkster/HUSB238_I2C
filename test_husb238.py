from HUSB238 import HUSB238 # HUSB238.py needs to be modified for either Raspberry Pi or MicroPython operation
import smbus                # Raspberry Pi
i2c = smbus.SMBus(1)        # Raspberry Pi

#import machine             # MicroPython
#i2c = machine.I2C(1,sda=machine.Pin(6), scl=machine.Pin(7), freq=400000) #xiao rp2040 MicroPython

USB_PD = HUSB238(i2c=i2c, debug=True)
print(USB_PD.get_src_cap())
USB_PD.select_cap(5)
