import curses
import random
import time

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.keypad(True)  # Enable keypad mode for arrow keys
    stdscr.timeout(100)  # Set input timeout to 100ms
    
    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()
    
    # Ensure window is large enough
    if sh < 10 or sw < 10:
        raise ValueError("Terminal window is too small!")
    
    # Create game window
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(True)  # Enable keypad for the window
    w.timeout(100)  # Set timeout for the window
    
    # Initial snake position
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    
    # Initial food position
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], curses.ACS_PI)
    
    # Initial direction
    key = curses.KEY_RIGHT
    last_key = key
    
    # Debugging: Display key codes at the bottom
    def show_debug_key(key_code):
        w.addstr(sh - 1, 0, f"Last key code: {key_code} (Arrow keys: UP=259, DOWN=258, LEFT=260, RIGHT=261, WASD=wasd, P=pause)  ")
    
    while True:
        # Get user input
        next_key = w.getch()
        show_debug_key(next_key)  # Display key code for debugging
        
        # Update direction only for valid keys
        if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT,
                        ord('w'), ord('a'), ord('s'), ord('d'), ord('p')]:
            key = next_key
        
        # Pause game on 'p' key
        if key == ord('p'):
            w.addstr(sh - 2, 0, "Paused (press 'p' to resume)")
            w.refresh()
            while w.getch() != ord('p'):
                pass
            w.addstr(sh - 2, 0, "                        ")
            continue
        
        # Prevent snake from reversing direction
        if (key == curses.KEY_UP and last_key == curses.KEY_DOWN) or \
           (key == curses.KEY_DOWN and last_key == curses.KEY_UP) or \
           (key == curses.KEY_LEFT and last_key == curses.KEY_RIGHT) or \
           (key == curses.KEY_RIGHT and last_key == curses.KEY_LEFT):
            key = last_key
        else:
            last_key = key
        
        # Calculate new head position
        if key == curses.KEY_UP or key == ord('w'):
            new_head = [snake[0][0] - 1, snake[0][1]]
        elif key == curses.KEY_DOWN or key == ord('s'):
            new_head = [snake[0][0] + 1, snake[0][1]]
        elif key == curses.KEY_LEFT or key == ord('a'):
            new_head = [snake[0][0], snake[0][1] - 1]
        elif key == curses.KEY_RIGHT or key == ord('d'):
            new_head = [snake[0][0], snake[0][1] + 1]
        else:
            new_head = [snake[0][0], snake[0][1]]  # No movement if invalid key
        
        # Insert new head
        snake.insert(0, new_head)
        
        # Check for collisions
        if (snake[0][0] <= 0 or snake[0][0] >= sh - 1 or
            snake[0][1] <= 0 or snake[0][1] >= sw - 1 or
            snake[0] in snake[1:]):
            return len(snake) - 3
        
        # Check if food is eaten
        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')
        
        # Draw new head
        try:
            w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        except curses.error:
            return len(snake) - 3  # Handle any drawing errors
        
        w.refresh()

# Run the game
try:
    score = curses.wrapper(main)
    print(f"Game Over! Your score: {score}")
except Exception as e:
    print(f"Error: {e}")
  
