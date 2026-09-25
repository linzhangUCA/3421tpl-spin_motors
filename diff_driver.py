from machine import Pin
from motor import Motor

class DiffDriver:
  def __init__(self, left_id, right_id, stby_id):
    pass
  
  def enable(self):
    self.stby_pin.value(1)
        
  def disable(self):
    self.stby_pin.value(0)

  def stop(self):  # active break
    pass

  def forward(self, speed=0):  # 0 <= speed <= 1
    pass
    
  def backward(self, speed=0):  # 0 <= speed <= 
    pass
    
  def spin_left(self, speed=0):  # in place, ccw
    pass

  def spin_right(self, speed=0):  # in place, cw
    pass

  def forward_left(self):
    pass

  def forward_right(self):
    pass

  def backward_left(self):
    pass

  def backward_right(self):
    pass
    
# TEST
if __name__=="__main__":
  from time import sleep
  
  # SETUP
  dd = DiffDriver(left_ids=(None, None, None), right_ids=(None, None, None), stby_id=None)  # Fill in correct ids to instantiate an object

  # LOOP
  # Terminate
  dd.stop()
  print("motors stopped.")
  sleep(0.1)  # full stop
  dd.disable()  # disable motor driver
  print("motor driver disabled.")
