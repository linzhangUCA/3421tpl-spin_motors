# Spin Motors

## 1. Overview
A robot needs to take actions. 
Electric motors, as the most commonly used actuators, play an essential role to make the robots interact with the environment.

In this assignment, you will need to: 
- Wire up and configure the [motor driver](https://www.pololu.com/product/713) board (TB6612FNG) with a Raspberry Pi Pico.
- Practice class inheritance, modification and instantiation.


## 2. Requirements

### 2.1. (35%) Wire Up the Motor Driver
> [!NOTE]
> The wiring of the motor driver board is different from the example.
- Control left motor using `A` channel of the motor driver board.
- Control right motor using `B` channel.
- (2%) Use `GPIO15` for motor A's `PWM` input.
- (2%) Use `GPIO13` for motor A's `IN1` input.
- (2%) Use `GPIO14` for motor A's `IN2` input.
- (2%) Use `GPIO16` for motor B's `PWM` input.
- (2%) Use `GPIO18` for motor B's `IN1` input.
- (2%) Use `GPIO17` for motor B's `IN2` input.
- (2%) Use `GPIO12` for motor driver's `STBY` input.

Circuit Picture
-
- Please take a picture of your circuit and display it below 👇

![circuit_pic](circuit_pic.jpg)

> [!IMPORTANT]
> - Please make sure your picture **clearly** illustrates the wiring as required above.
> - You'll get your points after picture is correctly rendered.  
> - Only the signal wiring section is mandatory.
> illustrating motor and battery connections is optional. 

### 2. (65%) Coding Exercises

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
