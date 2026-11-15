# Three Body Problem

A small gravity simulation in two dimensions, animated with matplotlib. Three bodies of equal mass are started close together with small initial velocities and left to pull on each other under Newton's law of gravitation.

## How it works

Each body keeps its mass, position, velocity and acceleration. On every step the simulation works out the acceleration on each body from every other body, using a = Gm / r^2 and splitting it into x and y components by the angle between the pair. All accelerations are calculated from the current positions before any body is moved, so the update is consistent across the system.

Bodies are then stepped forward with the constant acceleration equations, using the average of the previous and newly calculated acceleration. The new acceleration is stored for the next step.

The animation redraws one dot per body on each frame, with the simulation advancing one step per frame.

## Files

- `body.py` holds the `Body` class and the position and velocity update.
- `simulation.py` holds the `Simulation` class, the pairwise acceleration and the step over all bodies.
- `main.py` sets up three bodies and runs the animation.
- `test.py` is a short check with two bodies at rest, plotting their start and end positions after a few steps.

## Running it

Python 3 with matplotlib is needed.

```
pip install -r requirements.txt
python3 main.py
```

`main.py` sets a path for ffmpeg near the top. It is a Windows path from the machine the project was written on and is only needed if the animation is saved to a video file, which the script does not currently do. It can be changed or ignored.
