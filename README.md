# Asteroids Game

A classic Asteroids arcade game built with Python and Pygame, featuring power-ups, progressive difficulty, and a scoring system.

## Credits

This project is based on the guided project **"Build Asteroids using Python and Pygame"** from [Boot.dev](https://boot.dev), with additional features and enhancements.

## Prerequisites

- Python 3.8 or higher
- Pygame library

## Installation

### Option 1: Using UV

If you have [uv](https://github.com/astral-sh/uv) installed:

```bash
# Clone or download the project
cd asteroids

# Run the game (uv will handle dependencies automatically)
uv run main.py
```

### Option 2: Using pip

```bash
# Clone or download the project
cd asteroids

# Install dependencies
pip install pygame

# Run the game
python main.py
```

### Option 3: Using a virtual environment

```bash
# Clone or download the project
cd asteroids

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install pygame

# Run the game
python main.py
```

## Development

The game uses modular architecture for easy maintenance and extension:

- **GameState**: Manages all game variables and sprite groups
- **GameLogic**: Handles collision detection, scoring, and power-up spawning
- **UIRenderer**: Renders splash screen, game over screen, and HUD
- **InputHandler**: Processes keyboard events

## License

This project is based on educational content from Boot.dev.

## Acknowledgments

- Boot.dev for the guided project foundation
- Pygame community for the game development framework
