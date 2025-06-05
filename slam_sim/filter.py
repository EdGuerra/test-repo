import numpy as np

class GaussianComponent:
    def __init__(self, mean, cov, weight=1.0):
        self.mean = np.array(mean)
        self.cov = np.array(cov)
        self.weight = weight

class MultimodalFilter:
    """A simple Gaussian mixture filter for SLAM."""

    def __init__(self, components):
        self.components = components

    def predict(self, control):
        for c in self.components:
            c.mean = c.mean + np.array(control)

    def update(self, measurement):
        # fake update step: adjust weights based on measurement vector length
        total = 0.0
        for c in self.components:
            c.weight *= 1.0 / (1.0 + np.linalg.norm(measurement))
            total += c.weight
        for c in self.components:
            c.weight /= total

    def estimate(self):
        total_weight = sum(c.weight for c in self.components)
        mean = sum(c.weight * c.mean for c in self.components) / total_weight
        return mean
