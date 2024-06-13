# Elevator Project in Pygame

## Overview:
This project is for elevators management. The elevators are scheduled in an optimal way so that the waiting time for the passenger is the shortest

## Overview of the Project Achitecture and Core Algorithm
The project's core algorithm controls the scheduling and operation of elevators in response to floor requests. It works as follows:

When a user clicks a floor's call button, the call_elevator() function is invoked.
This function identifies the optimal elevator to receive the request using the choose_elevator() method.
The choose_elevator() method loops through all the elevators, calculating the total response time for each one based on factors such as the wait time for the elevator to clear and the floor from which the elevator exits.

The elevator with the shortest overall response time is selected as the optimal choice.

Elevator movement and queue management:
The requested floor is added to the elevator queue selected as optimal using the enqueue() method.
If the elevator is free, it immediately begins its movement to the requested floor.
If the elevator is currently occupied or in motion, the request is queued until the elevator becomes available.
The elevator constantly updates its location, responds to floor calls and manages its passenger queue.

Optimization and efficiency:
The algorithm takes into account factors such as waiting time, distance and the current elevator occupancy.
By intelligently managing elevator scheduling and operation, the algorithm maximizes efficiency, minimizes passenger wait times, and provides a seamless user experience within the simulated building environment.

## Features:
The project focuses on elevator management and includes the following capabilities:

* Receiving requests from floors and reaching them.
* Managing queues of passengers in the elevator.
* Use of audio and images to convey an excellent user experience when using the elevator.
* Activating a timer that updates the remaining waiting time until the elevator arrives.

## Installation:
1. Install Python.
2. Install the Pygame library.
3. Run the code.

## Files Menu:
* **constants.py:** Contains general constants for the project.
* **main.py:** Contains the core logic for initializing the game, handling events, updating the game state, and managing the main game loop.
* **Floor.py:** Contains the Floor class representing a floor.
* **Elevator.py:** Contains the Elevator class representing an elevator.
* **Building.py:** Contains the Building class representing the building where the elevators operate.
* **settings.json:** Contains settings for the game configuration.

## Usage Instructions:
1. Define the desired number of elevators and floors in the settings.json file (default: 5 elevators and 14 floors)
2. Run the main code file - "main.py".
3. Use the mouse to call the elevator to the desired floor.
4. Enjoy the game!

## Good luck and have fun!

