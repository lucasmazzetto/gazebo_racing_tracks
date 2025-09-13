#  Racing Track Simulation

## 🏁 About

This package provides predefined racing track models for use in Gazebo Harmonic simulations. It includes four simple tracks that can be used to gather synthetic data for training neural networks for autonomous driving, or to experiment with computer vision and control algorithms.


## 📚 Requirements

To use this package, you'll need the following:

- [Linux Ubuntu 24.04](https://ubuntu.com/blog/tag/ubuntu-24-04-lts)
- [ROS2 Jazzy Jalisco](https://docs.ros.org/en/rolling/Releases/Release-Jazzy-Jalisco.html)
- [Gazebo Harmonic](https://gazebosim.org/docs/harmonic/getstarted/)

## 🛠️ Setup

This project is designed for Linux Ubuntu 24.04. It may work on other versions or distributions, but some adjustments could be necessary. To avoid changing your OS, you can use Docker containers for an easier and more consistent setup across environments.

### Clone the Repository

Clone this repository into your ```workspace/src``` folder. If you don't have a workspace set up, you can learn more about creating one in the [ROS 2 workspace tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).

```bash
cd <path_to_your_workspace>/src
git clone git@github.com:lucasmazzetto/gazebo_racing_tracks.git
```

### Build the Package
Source the ROS 2 environment and build the package:

```bash
source /opt/ros/jazzy/setup.bash
cd <path_to_your_workspace>
colcon build
```

## 🚀 Usage

This package provides 4 different tracks for simulation in Gazebo Harmonic:

1. **Grass Track**  
2. **Dirt Track**
3. **Snow Track**  
4. **Sand Track**

Each track has a unique format, background, and style, and comes with its own dedicated launch file, making it easy to start a simulation with the desired environment directly from ROS 2.

### Launching a Track

After building the package, you can launch any of the available tracks from the `gazebo_racing_tracks` package. Each track has its own launch file:

- `grass_track.launch.py`
- `dirt_track.launch.py`
- `snow_track.launch.py`
- `sand_track.launch.py`

For example, to launch the Grass Track:

```bash
source /opt/ros/jazzy/setup.bash
cd <path_to_your_workspace>
source install/setup.bash
ros2 launch gazebo_racing_tracks grass_track.launch.py
```