# SLAM Simulator Repository

This repository contains a simple modular simulator for multimodal filter based SLAM.

## Structure

- `slam_sim/` - Package containing the simulator modules:
  - `sensors.py` - Example sensor classes.
  - `filter.py` - Implementation of a lightweight Gaussian mixture filter.
  - `map_manager.py` - Handles map management separately from the filter.
  - `simulator.py` - Combines everything into a simple SLAM loop.
- `run_sim.py` - Example script demonstrating usage.
- `tests/` - Unit tests.

## Usage

Install dependencies (numpy):

```bash
pip install numpy
```

Run the simulator example:

```bash
python run_sim.py
```

Run tests:

```bash
python -m unittest discover -v -s tests
```
