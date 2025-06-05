from .sensors import Lidar, IMU
from .filter import GaussianComponent, MultimodalFilter
from .map_manager import MapManager

class SLAMSimulator:
    def __init__(self):
        self.lidar = Lidar()
        self.imu = IMU()
        components = [GaussianComponent([0.0, 0.0], [[1.0, 0.0], [0.0, 1.0]])]
        self.filter = MultimodalFilter(components)
        self.map = MapManager()

    def step(self, control):
        # Predict step
        self.filter.predict(control)

        # Simulated sensor readings
        lidar_data = self.lidar.read()
        imu_data = self.imu.read()

        # Update step using arbitrary combination of sensor data
        measurement = lidar_data['ranges'] + imu_data['accel']
        self.filter.update(measurement)

        # Map management: add fake landmark based on filter estimate
        est = self.filter.estimate()
        self.map.add_landmark(tuple(float(x) for x in est))
        return est
