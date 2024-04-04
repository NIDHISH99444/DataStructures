from abc import ABC, abstractmethod

# Define Traffic Light States
class TrafficLightState(ABC):
    @abstractmethod
    def change_state(self, traffic_light):
        pass

# Concrete State: Green
class GreenState(TrafficLightState):
    def change_state(self, traffic_light):
        print("Traffic light is green. Proceed with caution.")
        traffic_light.set_state(YellowState())

# Concrete State: Yellow
class YellowState(TrafficLightState):
    def change_state(self, traffic_light):
        print("Traffic light is yellow. Prepare to stop.")
        traffic_light.set_state(RedState())

# Concrete State: Red
class RedState(TrafficLightState):
    def change_state(self, traffic_light):
        print("Traffic light is red. Stop.")
        traffic_light.set_state(GreenState())

# Context: Traffic Light
class TrafficLight:
    def __init__(self):
        self._state = GreenState()

    def set_state(self, state):
        self._state = state

    def change_state(self):
        self._state.change_state(self)

# Example usage
if __name__ == "__main__":
    traffic_light = TrafficLight()

    traffic_light.change_state()  # Traffic light is green
    traffic_light.change_state()  # Traffic light is yellow
    traffic_light.change_state()  # Traffic light is red
    traffic_light.change_state()  # Traffic light is green again
