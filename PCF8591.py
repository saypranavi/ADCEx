# ADC.Setup(Address)  # Check it by sudo i2cdetect -y -1
import smbus

class PCF8591:
  # for RPI version 1, use "bus = smbus.SMBus(0)"
  bus = smbus.SMBus(1)
  #check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
  def _init_(self, address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address,0x40 | chn) 
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))
