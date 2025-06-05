class MapManager:
    """Manages the map separately from the filter."""

    def __init__(self):
        # simple list of landmarks
        self.landmarks = []

    def add_landmark(self, position):
        self.landmarks.append(position)

    def get_landmarks(self):
        return list(self.landmarks)

    def clear(self):
        self.landmarks.clear()
