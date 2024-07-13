
class HUSB238:
    
    # Constructor
    def __init__(self, i2c, debug=False):
        self.i2c      = i2c
        self.slave_id = 0x08
        self.debug    = debug
    
    class bitfield_type:
        def __init__(self, NAME       = "",
                           ADDRESS    = 0x00,
                           RST_VAL    = 0x00,
                           WIDTH      = 0,
                           OFFSET     = 0,
                           ACCESS     = "",
                           TABLE_ENUM = {},
                           OTHER      = "" ):

            self.NAME        = NAME
            self.ADDRESS     = ADDRESS
            self.RST_VAL     = RST_VAL
            self.WIDTH       = WIDTH
            self.OFFSET      = OFFSET
            self.ACCESS      = ACCESS
            self.TABLE_ENUM  = TABLE_ENUM
            self.OTHER       = OTHER
            self.BIT_MASK    = int(2 ** self.WIDTH - 1) << self.OFFSET
    
     
    _PD_SRC_VOLTAGE = bitfield_type (
    NAME       = "PD_SRC_VOLTAGE",
    ADDRESS    = 0x00,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 4,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0, 1 : 5, 2 : 9 , 3 : 12, 4 : 15, 5 : 18, 6 : 20 } )

    _PD_SRC_CURRENT = bitfield_type (
    NAME       = "PD_SRC_CURRENT",
    ADDRESS    = 0x00,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 0,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0.5 , 1 : 0.7,  2  : 1.0,  3 : 1.25,  4 : 1.5,  5 : 1.75, 6 : 2.0,  7 : 2.25,
                   8 : 2.5,  9 : 2.75, 10 : 3.0, 11 : 3.25, 12 : 3.5, 13 : 4.0, 14 : 4.5, 15 : 5.0 } )
    
    _CC_DIR = bitfield_type (
    NAME       = "CC_DIR",
    ADDRESS    = 0x01,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 7,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "CC1", 1 : "CC2" } )
    
    _ATTACH = bitfield_type (
    NAME       = "ATTACH",
    ADDRESS    = 0x01,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 6,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "UNATTACHED", 1 : "OTHER" } )
    
    _PD_RESPONSE = bitfield_type (
    NAME       = "PD_RESPONSE",
    ADDRESS    = 0x01,
    RST_VAL    = 0x00,
    WIDTH      = 3,
    OFFSET     = 3,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "NO RESPONSE", 1 : "SUCCESS", 3 : "INVALID COMMAND OR ARGUEMENT" , 4 : "COMMAND NOT SUPPORTED", 5 : "TRANSACTION FAIL" } )
    
    _5V_VOLTAGE = bitfield_type (
    NAME       = "5V_VOLTAGE",
    ADDRESS    = 0x01,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 2,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "OTHERS", 1 : "5V" } )
    
    _5V_CURRENT = bitfield_type (
    NAME       = "5V_CURRENT",
    ADDRESS    = 0x01,
    RST_VAL    = 0x00,
    WIDTH      = 2,
    OFFSET     = 0,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0.5, 1 : 1.5, 2 : 2.4, 3 : 3.0 } )
    
    _SRC_5V_DETECT = bitfield_type (
    NAME       = "SRC_5V_DETECT",
    ADDRESS    = 0x02,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 7,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "NOT DETECTED", 1 : "DETECTED" } )
    
    _SRC_5V_CURRENT = bitfield_type (
    NAME       = "SRC_5V_CURRENT",
    ADDRESS    = 0x02,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 0,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0.5 , 1 : 0.7,  2  : 1.0,  3 : 1.25,  4 : 1.5,  5 : 1.75, 6 : 2.0,  7 : 2.25,
                   8 : 2.5,  9 : 2.75, 10 : 3.0, 11 : 3.25, 12 : 3.5, 13 : 4.0, 14 : 4.5, 15 : 5.0 } )
    
    _SRC_9V_DETECT = bitfield_type (
    NAME       = "SRC_9V_DETECT",
    ADDRESS    = 0x03,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 7,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "NOT DETECTED", 1 : "DETECTED" } )
    
    _SRC_9V_CURRENT = bitfield_type (
    NAME       = "SRC_9V_CURRENT",
    ADDRESS    = 0x03,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 0,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0.5 , 1 : 0.7,  2  : 1.0,  3 : 1.25,  4 : 1.5,  5 : 1.75, 6 : 2.0,  7 : 2.25,
                   8 : 2.5,  9 : 2.75, 10 : 3.0, 11 : 3.25, 12 : 3.5, 13 : 4.0, 14 : 4.5, 15 : 5.0 } )
    
    _SRC_12V_DETECT = bitfield_type (
    NAME       = "SRC_12V_DETECT",
    ADDRESS    = 0x04,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 7,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "NOT DETECTED", 1 : "DETECTED" } )
    
    _SRC_12V_CURRENT = bitfield_type (
    NAME       = "SRC_12V_CURRENT",
    ADDRESS    = 0x04,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 0,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0.5 , 1 : 0.7,  2  : 1.0,  3 : 1.25,  4 : 1.5,  5 : 1.75, 6 : 2.0,  7 : 2.25,
                   8 : 2.5,  9 : 2.75, 10 : 3.0, 11 : 3.25, 12 : 3.5, 13 : 4.0, 14 : 4.5, 15 : 5.0 } )
    
    _SRC_15V_DETECT = bitfield_type (
    NAME       = "SRC_15V_DETECT",
    ADDRESS    = 0x05,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 7,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "NOT DETECTED", 1 : "DETECTED" } )
    
    _SRC_15V_CURRENT = bitfield_type (
    NAME       = "SRC_15V_CURRENT",
    ADDRESS    = 0x05,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 0,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0.5 , 1 : 0.7,  2  : 1.0,  3 : 1.25,  4 : 1.5,  5 : 1.75, 6 : 2.0,  7 : 2.25,
                   8 : 2.5,  9 : 2.75, 10 : 3.0, 11 : 3.25, 12 : 3.5, 13 : 4.0, 14 : 4.5, 15 : 5.0 } )

    _SRC_18V_DETECT = bitfield_type (
    NAME       = "SRC_18V_DETECT",
    ADDRESS    = 0x06,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 7,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "NOT DETECTED", 1 : "DETECTED" } )
    
    _SRC_18V_CURRENT = bitfield_type (
    NAME       = "SRC_18V_CURRENT",
    ADDRESS    = 0x06,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 0,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0.5 , 1 : 0.7,  2  : 1.0,  3 : 1.25,  4 : 1.5,  5 : 1.75, 6 : 2.0,  7 : 2.25,
                   8 : 2.5,  9 : 2.75, 10 : 3.0, 11 : 3.25, 12 : 3.5, 13 : 4.0, 14 : 4.5, 15 : 5.0 } )

    _SRC_20V_DETECT = bitfield_type (
    NAME       = "SRC_20V_DETECT",
    ADDRESS    = 0x07,
    RST_VAL    = 0x00,
    WIDTH      = 1,
    OFFSET     = 7,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : "NOT DETECTED", 1 : "DETECTED" } )
    
    _SRC_20V_CURRENT = bitfield_type (
    NAME       = "SRC_20V_CURRENT",
    ADDRESS    = 0x07,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 0,
    ACCESS     = "RO",
    TABLE_ENUM = { 0 : 0.5 , 1 : 0.7,  2  : 1.0,  3 : 1.25,  4 : 1.5,  5 : 1.75, 6 : 2.0,  7 : 2.25,
                   8 : 2.5,  9 : 2.75, 10 : 3.0, 11 : 3.25, 12 : 3.5, 13 : 4.0, 14 : 4.5, 15 : 5.0 } )

    _PDO_SELECT = bitfield_type (
    NAME       = "PDO_SELECT",
    ADDRESS    = 0x08,
    RST_VAL    = 0x00,
    WIDTH      = 4,
    OFFSET     = 4,
    ACCESS     = "RW",
    TABLE_ENUM = { 0 : 0, 5 : 1, 9 : 2 , 12 : 3, 15 : 8, 18 : 9, 20 : 10 } )

    _COMMAND_FUNC = bitfield_type (
    NAME       = "COMMAND_FUNC",
    ADDRESS    = 0x09,
    RST_VAL    = 0x00,
    WIDTH      = 5,
    OFFSET     = 0,
    ACCESS     = "RW",
    TABLE_ENUM = { "REQUEST PDO_SELECT SETTING" : 1, "SEND GET_SRC_CAP" : 4, "REQUEST HARD RESET" : 16 } )

    LIST_OF_BITFIELDS = [ _PD_SRC_VOLTAGE, _PD_SRC_CURRENT,
                          _CC_DIR, _ATTACH, _PD_RESPONSE, _5V_VOLTAGE, _5V_CURRENT,
                          _SRC_5V_DETECT,  _SRC_5V_CURRENT,
                          _SRC_9V_DETECT,  _SRC_9V_CURRENT,
                          _SRC_12V_DETECT, _SRC_12V_CURRENT,
                          _SRC_15V_DETECT, _SRC_15V_CURRENT,
                          _SRC_18V_DETECT, _SRC_18V_CURRENT,
                          _SRC_20V_DETECT, _SRC_20V_CURRENT,
                          _PDO_SELECT,     _COMMAND_FUNC ]

    def write_byte_data(self, address=0x00, data=0x00):
#        self.i2c.writeto_mem(self.slave_id, address, bytearray([data & 0xFF])) # MicroPython
        self.i2c.write_byte_data(self.slave_id, address, data) # Raspberry Pi smbus
    
    def read_byte_data(self, address=0x00):
#        int_read_byte = list(self.i2c.readfrom_mem(self.slave_id, address, 1))[0] # MicroPython
        int_read_byte = self.i2c.read_byte_data(self.slave_id, address) # Raspberry Pi smbus
        return int_read_byte # int value
    
    def i2c_bf_read(self, bit_field):
        try:
            address  = 0xFF & bit_field.ADDRESS
            read_int = self.read_byte_data(bit_field.ADDRESS)
            bf_read_data = ( read_int & bit_field.BIT_MASK ) >> bit_field.OFFSET 
            if (self.debug):
                print("Read bit_field {} address 0x{:02x}, bit mask is 0x{:02x}, value is 0x{:02x}".format(bit_field.NAME, address, bit_field.BIT_MASK, bf_read_data))
            return bf_read_data
        except:
            print("ERROR with i2c_bf_read")

    def i2c_bf_write(self, bit_field, bf_wdata):
        try:
            address = 0xFF & bit_field.ADDRESS
            read_int   = self.read_byte_data(bit_field.ADDRESS)
            wdata = ( read_int & ~bit_field.BIT_MASK) | ((bf_wdata << bit_field.OFFSET) & bit_field.BIT_MASK)
            self.write_byte_data(address, wdata)
            if (self.debug):
                print("Wrote bit_field {} address 0x{:02x}, bit mask is 0x{:04x}, data 0x{:02x}".format(bit_field.NAME, address, bit_field.BIT_MASK, bf_wdata))
        except:
            print("ERROR with i2c_bf_write")
    
    def req_src_cap(self):
        self.i2c_bf_write(self._COMMAND_FUNC, self._COMMAND_FUNC.TABLE_ENUM["SEND GET_SRC_CAP"])
    
    def get_5v_src_cap(self):
        if (self._SRC_5V_DETECT.TABLE_ENUM[self.i2c_bf_read(self._SRC_5V_DETECT)] == "DETECTED"):
            return [5, self._SRC_5V_CURRENT.TABLE_ENUM[self.i2c_bf_read(self._SRC_5V_CURRENT)]]
        else:
            return []
    
    def get_9v_src_cap(self):
        if (self._SRC_9V_DETECT.TABLE_ENUM[self.i2c_bf_read(self._SRC_9V_DETECT)] == "DETECTED"):
            return [9, self._SRC_9V_CURRENT.TABLE_ENUM[self.i2c_bf_read(self._SRC_9V_CURRENT)]]
        else:
            return []
    
    def get_12v_src_cap(self):
        if (self._SRC_12V_DETECT.TABLE_ENUM[self.i2c_bf_read(self._SRC_12V_DETECT)] == "DETECTED"):
            return [12, self._SRC_12V_CURRENT.TABLE_ENUM[self.i2c_bf_read(self._SRC_12V_CURRENT)]]
        else:
            return []
    
    def get_15v_src_cap(self):
        if (self._SRC_15V_DETECT.TABLE_ENUM[self.i2c_bf_read(self._SRC_15V_DETECT)] == "DETECTED"):
            return [15, self._SRC_15V_CURRENT.TABLE_ENUM[self.i2c_bf_read(self._SRC_15V_CURRENT)]]
        else:
            return []
    
    def get_20v_src_cap(self):
        if (self._SRC_20V_DETECT.TABLE_ENUM[self.i2c_bf_read(self._SRC_20V_DETECT)] == "DETECTED"):
            return [20, self._SRC_20V_CURRENT.TABLE_ENUM[self.i2c_bf_read(self._SRC_20V_CURRENT)]]
        else:
            return []
    
    def get_src_cap(self):
        self.req_src_cap()
        src_cap = []
        src_cap.append(self.get_5v_src_cap())
        src_cap.append(self.get_9v_src_cap())
        src_cap.append(self.get_12v_src_cap())
        src_cap.append(self.get_15v_src_cap())
        src_cap.append(self.get_20v_src_cap())
        return src_cap
    
    def select_cap(self, voltage=5):
        self.i2c_bf_write(self._PDO_SELECT, self._PDO_SELECT.TABLE_ENUM[voltage])
        self.i2c_bf_write(self._COMMAND_FUNC, self._COMMAND_FUNC.TABLE_ENUM["REQUEST PDO_SELECT SETTING"])
        
