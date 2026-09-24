class DiffDriver:
  pass

# TEST
if __name__=="__main__":
  from time import sleep
  
  # INSTANTIATE
  dd = DiffDriver(left_ids=(), right_ids=(), stby_id=)  # Fill in correct ids

  # Execute
  dd.left_forward()
  print("LF")
  sleep(4)
  dd.right_forward()
  print("RF")
  sleep(4)
  dd.left_backward()
  print("LB")
  sleep(4)
  dd.right_backward()
  print("RB")
  sleep(4)

  # Terminate
  dd.stop()
  print("motors stopped.")
  sleep(0.1)  # full stop
  dd.disable()  # disable motor driver
  print("motor driver disabled.")
