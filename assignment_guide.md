# Spin Motors

## 1. Overview
A robot needs to take actions. 
Electric motors, as the most commonly used actuators, play an essential role to make the robots interact with the environment.

In this assignment, you will need to: 
- Wire up and configure the [motor driver](https://www.pololu.com/product/713) board (TB6612FNG) with a Raspberry Pi Pico.
- Practice class inheritance, modification and instantiation.


## 2. Requirements

### 2.1. (30%) Wire Up the Motor Driver
1. Wire up the motor driver board with Pico board following the instructions below.
 - (2%) Use `GPIO12` for `PWMA` input.
 - (2%) Use `GPIO14` for `AIN1` input.
 - (2%) Use `GPIO13` for `AIN2` input.
 - (2%) Use `GPIO18` for `PWMB` input.
 - (2%) Use `GPIO16` for `BIN1` input.
 - (2%) Use `GPIO17` for `BIN2` input.
 - (2%) Use `GPIO15` for `STBY` input.
 - (4%) Correctly wire up the battery and the power pins (for both boards).

2. Show off your circuit picture in [README](README.md)
 - (7%) Please organize your circuit and reveal the connections with a clear view (position camera aptly and do not obscure key connections).
   You can upload more than one picture to better demonstrate. 
 - (5%) Images must be scaled to 800 × 600 pixels with a horizontal orientation.
 
> [!IMPORTANT]
> - The wiring of the motor driver board is different from the example.
> - Credits will be redeemed after the circuit picture is uploaded.

### 2.2 (57%) Coding Exercises
1. Upload the python module contains `Motor` class to the root of this repository.
2. Develop a `DiffDriver` class in [diff_driver.py](diff_driver.py) using the imported `Motor` class with following methods: 
 - (5%) `forward(speed)`: drives mobile base straight forward at `speed` percent of the max speed.
 - (5%) `backward(speed)`: drives mobile base straight backward at `speed` percent of the max speed.
 - (5%) `spin_left(speed)`: spins mobile base in place **counter-clockwisely** around the center of the axle at `speed` percent of the max speed.
 - (5%) `spin_right(speed)`: spins mobile base in place **clockwisely** around the center of the axle at `speed` percent of the max speed.
 - (5%) `stop()`: **short break** the motors.
 - (5%) `enable()`: Enable the motor driver.
 - (5%) `disable()`: Disable the motor driver.
> [!IMPORTANT]
> - When coding next four methods, use 50% max speed for the faster motor and 25% max speed for the slower motor.
 - (5%) `forward_left()`: drives mobile base forward and leaning left.
 - (5%) `forward_right()`: drives mobile base forward and leaning right. 
 - (5%) `backward_left()`: drives mobile backward and leaning left.  
 - (5%) `backward_right()`: drives mobile base backward and leaning right.
> [!TIP]
> - Test newly developed functions frequently using the test code below: `if __name__=="__main__":`.
3. (10%) Use `DiffDriver` Class
Please complete code in [test_diff_drive.py](test_diff_drive.py) to instantiate the `DiffDriver` class and use it to spin the motors.
- Import correct module and instantiate an object using `DiffDriver` class.
- Perform the following sequence of operations on mobile base. Each operation should last for **1 second**.
     1. (1%) `forward(0.5)`
     2. (1%) `forward_left()`.
     3. (1%) `spin_left(0.5)`.
     4. (1%) `backward_left()`.
     5. (1%) `backward(0.5)`.
     6. (1%) `backward_right()`
     7. (1%) `spin_right(0.5)`
     8. (1%) `forward_right()`

> [!NOTE]
> The grader will check your work using his/her own mobile base.
   
### 2.3. (3%) Acknowledge AI's contributions.
If AI helped with this assignment, please list out all the contributions.

