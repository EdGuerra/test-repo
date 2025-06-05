from slam_sim import SLAMSimulator

if __name__ == '__main__':
    sim = SLAMSimulator()
    for i in range(5):
        est = sim.step(control=[0.1, 0.0])
        print(f"Step {i}: estimate {est}, landmarks: {sim.map.get_landmarks()}")
