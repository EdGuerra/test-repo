import unittest
from slam_sim import SLAMSimulator

class TestSLAMSimulator(unittest.TestCase):
    def test_run(self):
        sim = SLAMSimulator()
        est = sim.step(control=[0.0, 0.0])
        self.assertEqual(len(sim.map.get_landmarks()), 1)
        self.assertEqual(len(est), 2)

if __name__ == '__main__':
    unittest.main()
