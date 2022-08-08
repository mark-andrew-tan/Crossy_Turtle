# Crossy_Turtle
A simple version of the classic Frogger game. Made with Python using Turtle Graphics

### Project Goal
Create the classic Frogger game utilizing the methods from the Python Turtle graphics module to practice OOP concepts: Class, Object, Method, Inheritance, Polymorphism.

### Design

#### Game
The player (white turtle) starts at the bottom of the screen, and must reach the finsh line (cyan) to advance to the next level. The player has a time limit, and must navigate through barriers (green) and avoid the moving cars (rectangles). Each new level adds more obstacles and cars to the field.

#### Controls
'WASD' keys to move the turtle up, down, left, or right, one square.

#### Object Collision
To prevent the turtle from crossing over a barrier (green) the Player has attributes on valid directions it can move depending on it's surrondings. For example, if the Player attribute 'valid_up' is False, then pressing the 'W' key will not move the Player.

To determine the Players attributes on valid directions there is a 'shield' object, which is made of multiple 'SidePlayer' objects, and surronds the Player. Each 'SidePlayer' constantly checks if it has hit a barrier, and depending on the orientation of the sideplayer, will set the corresponding direction attribute for the player to False.
(A shield is made from multiple SidePlayers, a SidePlayer is a Player)


### Playthough
Demonstrating a level completion, and the collision system with 'shield object' (pink 'SidePlayer' blocks left visible for demonstration):

https://user-images.githubusercontent.com/98869613/183318589-533f293d-6c35-4ddd-893d-ec45d30ac1e6.mp4
