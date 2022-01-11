# Toy Robot Simulation

[![Master Actions Status](https://github.com/rlupat/ToyRobotProject/actions/workflows/unit-tests/badge.svg)]

## Description 

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. 
There are no other obstructions on the table surface. 
The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. 
Any movement that would result in the robot falling from the table must be prevented, 
however further valid movement commands must still be allowed.

The console applications can read in commands in the following form:
- PLACE X,Y,F
- MOVE
- LEFT
- RIGHT
- REPORT

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
- The origin (0,0) can be considered to be the SOUTH WEST most corner. 
- It is required that the first command to the robot is a PLACE command, after that, 
  any sequence of commands may be issued, in any order, including another PLACE command.   
- The application will discard all commands in the sequence until a valid PLACE command has been executed.


MOVE will move the toy robot one unit forward in the direction it is currently facing.

LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

REPORT will announce the X,Y and F of the robot to stdout.

Constraints
- A robot that is not on the table will ignore the MOVE, LEFT, RIGHT and REPORT commands.
- Toy robot can not fall off the table during movement. This also includes the initial placement of the toy robot.
Any move that cause the above will be ignored. 
  
## Installation

### From source

- Clone this github repository
- Setup virtual environment
    - python3 -m venv toyrobot-env
- Activate virtual environment
    - source toyrobot-env/bin/activate
- pip install <path-to-downloaded-source>


## Usage

- Activate virtaul environment (as above)
- python -m toyrobot.app -i <path-to-input-commands> 
