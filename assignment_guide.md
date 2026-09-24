# Spin Motors

## 1. Overview
A robot needs to take actions. 
Electric motors, as the most commonly used actuators, play an essential role to make the robots interact with the environment.

In this assignment, you will need to: 
- Wire up and configure the [motor driver](https://www.pololu.com/product/713) board (TB6612FNG) with a Raspberry Pi Pico.
- Practice class inheritance, modification and instantiation.


## 2. Requirements

### 2.1. (35%) Wire Up the Motor Driver
1. (21%) Wire up the motor driver board with Pico board following the instructions below.
 - (2%) Use `GPIO12` for `PWMA` input.
 - (2%) Use `GPIO14` for `AIN1` input.
 - (2%) Use `GPIO13` for `AIN2` input.
 - (2%) Use `GPIO18` for `PWMB` input.
 - (2%) Use `GPIO16` for `BIN1` input.
 - (2%) Use `GPIO17` for `BIN2` input.
 - (2%) Use `GPIO15` for `STBY` input.
 - (7%) Correctly wire up the battery and the power pins (for both boards).

> [!IMPORTATNT]
> - The wiring of the motor driver board is different from the example.
> - Credits will be redeemed after the circuit picture is uploaded.

2. (14%) Show off your circuit picture in [README](README.md)
 - (7%) Please organize your circuit and reveal the connections with a clear view (position camera aptly and do not obscure key connections).
   You can upload more than one picture to better demonstrate. 
 - (7%) Images must be scaled to 800 × 600 pixels with a horizontal orientation.
 

### 2.2 (65%) Coding Exercises

#### 2.1. (55%) Build `DiffDriver` Class from Inheritance
Work in [diff_driver.py](diff_driver.py).
Develop a `DiffDriver` class by inheriting `DualMotorDriver` class.
> [!WARNING]
> - Nothing is allowed to be explicitly imported from `machine`.
> IOW, do not use `Pin`, `PWM`, `Timer`, etc..
 
1. (5%) Import correct module and inherit the `DualMotorDriver` class.
2. (10%) Instantiate a `DualMotorDriver` object in the test section below `if __name__=="__main__":`. Please strictly follow the motor channel definitions in [Wiring Pico and Motor Driver Board](#11-wiring-pico-and-motor-driver-board) section.
3. Introduce the following four methods/functions to the `DiffDriver` class and achieve the requested behavior.
   - (10%) `forward_left()`: drives mobile base forward and leaning left.
   - (10%) `forward_right()`: drives mobile base forward and leaning right. 
   - (10%) `backward_left()`: drives mobile backward and leaning left.  
   - (10%) `backward_right()`: drives mobile base backward and leaning right.

> [!IMPORTANT]
> - No need for variable motor speed.
> - Please use 50% max speed for the faster motor and 25% max speed for the slower motor.

> [!TIP]
> - Upload [motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/motor_driver.py) and [dual_motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/dual_motor_driver.py) to your Pico board.
> - Learn more about class inheritance from this interactive [tutorial](https://www.w3schools.com/python/python_inheritance.asp)
> - Test newly developed functions frequently using the test code below: `if __name__=="__main__":`. 

#### 2.2. (10%) Use `DiffDriver` Class
Please complete code in [test_diff_drive.py](test_diff_drive.py) to instantiate the `DiffDriver` class and use it to spin the motors.
1. (2%) Import correct module and instantiate an object using `DiffDriver` class.
2. (8%) Perform the following sequence of operations on mobile base. Each operation should last for **1 second**.
     1. (1%) `forward(0.5)`
     2. (1%) `forward_left()`.
     3. (1%) `spin_left(0.5)`.
     4. (1%) `backward_left()`.
     5. (1%) `backward(0.5)`.
     6. (1%) `backward_right()`
     7. (1%) `spin_right(0.5)`
     8. (1%) `forward_right()`


   
## AI Usage Policy
Please acknowledge AI's contribution following policies in the [syllabus](https://linzhanguca.github.io/_docs/robotics1-2025/syllabus.pdf).
