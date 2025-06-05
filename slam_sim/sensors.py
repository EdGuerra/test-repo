class Sensor:
    def __init__(self, name):
        self.name = name

    def read(self):
        raise NotImplementedError("Sensor.read must be overridden")

class Lidar(Sensor):
    def __init__(self):
        super().__init__('Lidar')

    def read(self):
        # placeholder: return fake distance measurements
        return {'ranges': [1.0, 1.5, 2.0]}

class IMU(Sensor):
    def __init__(self):
        super().__init__('IMU')

    def read(self):
        # placeholder: return fake acceleration data
        return {'accel': [0.0, 0.0, -9.81]}
