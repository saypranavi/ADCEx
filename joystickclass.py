import smbus
global address


class PCF8591:
  # for RPI version 1, use "bus = smbus.SMBus(0)"
  bus = smbus.SMBus(1)
  #check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
  def __init__(self, address):
    self.bus = smbus.SMBus(1)
    self.address = address
    #make an ADC var/obj

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address,0x40 | chn) 
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)


class Joystick:

  def __init__(self, address):
    self.pcf = PCF8591(address)

  def getX(self):
    return self.pcf.read(0x40)
    
  def getY(self):
    return self.pcf.read(0x41)
  
     
while True:
  js = Joystick(0x48)
  print(js.getX(), ", " , js.getY() )
  # print('X = ', js.getX())
  # print('Y = ', js.getY())