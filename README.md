# Asteroids

An Asteroids game built with Python and Pygame as part of the
Boot.dev curriculum.

## Features

- Player movement and rotation
- Shooting with a cooldown
- Randomly spawning asteroids
- Collision detection
- Large and medium asteroids split into smaller, faster rocks
- Game over when the player collides with an asteroid

## Requirements

- Python 3.13 or newer
- uv for managing dependencies and running the game

## Getting Started

Clone the repository:

```sh
git clone https://github.com/SqushyWushy/asteroids.git
cd asteroids
```

Install the dependencies:

```sh
uv sync
```

Run the game:

```sh
uv run main.py
```

## Controls

| Key   | Action        |
| ----- | ------------- |
| W     | Move forward  |
| S     | Move backward |
| A     | Turn left     |
| D     | Turn right    |
| Space | Shoot         |

Close the window to quit. After a game over, run the command again
to restart.

## About This Project

I built this project to learn Python, object-oriented programming,
game loops, vectors, and collision detection.

The project follows the Boot.dev Asteroids curriculum and includes
course-provided code.
