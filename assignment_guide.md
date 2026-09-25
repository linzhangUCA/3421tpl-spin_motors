# Spin Motors

## 1. Overview
A robot needs to take actions. 
Electric motors, as the most commonly used actuators, play an essential role to make the robots interact with the environment.

In this assignment, you will need to: 
- Wire up and configure the [motor driver](https://www.pololu.com/product/713) board (TB6612FNG) with a Raspberry Pi Pico.
- Practice class inheritance, modification and instantiation.


## 2. Requirements

### 2.1. (18%) Wire Up the Motor Driver
Wire up the motor driver board with Pico board following the instructions below.
   - (2%) Use `GPIO12` for `PWMA` input.
   - (2%) Use `GPIO14` for `AIN1` input.
   - (2%) Use `GPIO13` for `AIN2` input.
   - (2%) Use `GPIO18` for `PWMB` input.
   - (2%) Use `GPIO16` for `BIN1` input.
   - (2%) Use `GPIO17` for `BIN2` input.
   - (2%) Use `GPIO15` for `STBY` input.
   - (4%) Correctly wire up the battery and the power pins (for both boards).
 
> [!IMPORTANT]
> - Please show off your circuit picture in [README](README.md)
> - Organize your circuit and reveal the connections with a clear view (position camera aptly and do not obscure key connections).
    You can upload more than one picture to better demonstrate. 
> - Images must be scaled to 800 × 600 pixels with a horizontal orientation.
> - Credits will be redeemed after the circuit pictures are documented.

### 2.2. (20%) Spin a motor
A `Motor` class has been constructed and available at [motor.py](motor.py).
Please use this class to test the motor by spinning it back and forth at varied speed. 
> [!NOTE]
> You can drop the test code under the `if __name__ == "__main__":` section.

1. (5%) Forwardly ramp up motor speed from 0 to maximum in 5 seconds. Increase the dutycycle 5% at a time.
2. (5%) Forwardly ramp down motor speed from maximum to 0 in 5 seconds. Decrease the dutycycle 4% at a time.
3. (5%) Backwardly ramp up motor speed from 0 to maximum in 5 seconds. Increase the dutycycle 4% at a time.
4. (5%) Backwardly ramp down motor speed from maximum to 0 in 5 seconds. Decrease the dutycycle 5% at a time.

### 2.3. (50%) Develop a dual motor driver for differential drive 
Develop a `DiffDriver` class in [diff_driver.py](diff_driver.py) using the `Motor` class from [motor.py](motor.py).
   - (5%) Configure left and right motors and the `stby_pin` in class's `__init__` function.
   - (5%) `forward(speed)`: drives mobile base straight forward at normalized speed between 0 (stall) and 1 (full speed).
   - (5%) `backward(speed)`: drives mobile base straight backward at normalized speed between 0 (stall) and 1 (full speed).
   - (5%) `spin_left(speed)`: spins mobile base in place **counter-clockwisely** around the center of the axle at normalized speed between 0 (stall) and 1 (full speed).
   - (5%) `spin_right(speed)`: spins mobile base in place **clockwisely** around the center of the axle at normalized speed between 0 (stall) and 1 (full speed).
   - (5%) `stop()`: **actively break** to stop both motors.
   - (5%) `forward_left()`: drives mobile base forward and leaning left.
   - (5%) `forward_right()`: drives mobile base forward and leaning right. 
   - (5%) `backward_left()`: drives mobile backward and leaning left.  
   - (5%) `backward_right()`: drives mobile base backward and leaning right.
> [!IMPORTANT]
> - You'll need to upload [motor.py](motor.py) to Pico.
> - For `forward_left()`, `forward_right()`, `backward_left()` and `backward_right()`, use 50% max speed for the faster motor and 25% max speed for the slower motor.
> - You can test newly developed methods using the section below: `if __name__=="__main__":`.

### 2.4. (10%) Use `DiffDrive` class
Complete code in [test_diff_drive.py](test_diff_drive.py) to instantiate the `DiffDriver` class and use it to spin the motors.
- (2%) Import correct module and instantiate an object using `DiffDriver` class.
- (8%) Perform the following sequence of operations on mobile base. Each operation should last for **1 second**.
     1. `forward(0.5)`
     2. `forward_left()`.
     3. `spin_left(0.5)`.
     4. `backward_left()`.
     5. `backward(0.5)`.
     6. `backward_right()`
     7. `spin_right(0.5)`
     8. `forward_right()`

### 2.5. (2%) Acknowledge AI's contributions.
If AI helped with this assignment, please list out all the contributions.

## 3. Resources
[Pololu TB6612FNG Dual Motor Driver Carrier](https://www.pololu.com/product/713)
[TB6612FNG Datasheet](https://toshiba.semicon-storage.com/info/TB6612FNG_datasheet_en_20141001.pdf?did=10660&prodName=TB6612FNG)
