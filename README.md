# 🐍 Snake Game

A terminal-based Snake game implemented in Python. Navigate the snake to eat food, grow longer, and avoid crashing into yourself. Don't fear the walls—the game space wraps around!

## Project Structure

- **`main.py`** — Entry point, starts the game loop, handles score-related tasks.
- **`snake.py`** — Manages snake movement, growth, and collision logic.
- **`food.py`** — Handles food generation and placement.
- **`constants.py`** — Stores game constants like game difficulty and screen size.
- **`scores.json`** — Keeps track of high scores between sessions.

## How To Run

1. Clone the repository:

    ```sh
    git clone https://github.com/benedekpal/snake.git
    cd snake
    ```

2. Install `uv`:

    ```sh
    pip install uv
    ```

3. Install dependencies:

    ```sh
    uv pip install -r pyproject.toml
    ```

4. Run the game:

    ```sh
    python main.py
    ```

## Controls

- Use arrow keys to move
- Eat food to grow longer
- Avoid eating yourself
