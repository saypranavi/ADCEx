import smbus
global address

#All from professor/kit code
class PCF8591:
  # for RPI version 1, use "bus = smbus.SMBus(0)"
  bus = smbus.SMBus(1)
  #check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
  #define class
  def __init__(self, address):
    self.bus = smbus.SMBus(1)
    self.address = address
    #make an ADC var/obj
  #read the channel values
  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address,0x40 | chn) 
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

#Joystick Class extends PCF8591
class Joystick:
  #Define class same as PCF8591
  def __init__(self, address):
    self.pcf = PCF8591(address) #inherit by composition 

  def getX(self):
    return str(self.pcf.read(0x40)) #get X Value and return string version of value
    
  def getY(self):
    return str(self.pcf.read(0x41)) #get Y Value and return string version of value
  
#Constantly run the code until quit reading values     
while True:
  js = Joystick(0x48) #create joystick with initial address
  print(js.getX()+", "+ js.getY()) #print X, Y