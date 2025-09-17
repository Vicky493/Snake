

Overview

This is a classic Snake game implemented in Python using the curses library. The snake moves around the terminal window, eating food to grow longer while avoiding collisions with the walls and itself. The game supports both arrow keys and WASD controls for movement, with a pause feature.

Requirements





Python 3.x



A terminal that supports the curses library (e.g., Linux, macOS, or Windows with a compatible terminal like Windows Subsystem for Linux)



No additional packages are required as curses is included in the Python standard library on supported platforms.

How to Run





Save the game code in a file named snake.py.



Open a terminal and navigate to the directory containing snake.py.



Run the game using the command:

python3 snake.py



Ensure your terminal window is at least 10x10 characters in size to avoid errors.

Gameplay Instructions





Objective: Control the snake to eat food (represented by the π symbol) to increase your score. Avoid hitting the walls or the snake's own body.



Controls:





Arrow keys or WASD: Move the snake up (W/Up), down (S/Down), left (A/Left), or right (D/Right).



P: Pause or resume the game.



The snake moves continuously in the last valid direction.



The game ends if the snake hits the walls, itself, or if a drawing error occurs.



Your final score is the number of food items eaten (snake length minus the initial length of 3).

Features





Smooth movement with a 100ms timeout between updates.



Collision detection with walls and the snake's body.



Random food placement that avoids spawning on the snake.



Debugging display showing the last key code pressed at the bottom of the screen.



Pause functionality using the 'P' key.



Error handling for small terminal windows and drawing issues.

Notes





The game uses the curses library, which may not work in some IDE terminals (e.g., VS Code's integrated terminal). Use a system terminal for best results.



The game window dynamically adjusts to the size of your terminal.



The snake cannot reverse direction directly to prevent immediate self-collision (e.g., moving up then immediately down).

Troubleshooting





Error: "Terminal window is too small!": Resize your terminal window to be at least 10x10 characters.



Curses not working on Windows: Use Windows Subsystem for Linux (WSL) or a Linux/macOS system, as curses is not fully supported on native Windows terminals.



Game feels too fast or slow: Adjust the stdscr.timeout(100) value in the code (in milliseconds) to change the snake's speed.

License

This project is unlicensed and provided as-is for educational purposes.
