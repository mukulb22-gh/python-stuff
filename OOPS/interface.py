"""
Interface in python:
"""

from abc import ABC, abstractmethod

class Speaker(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

class DogSpeaker(Speaker):
    def speak(self):
        return "Woof!"

    def volume_up(self):
        return "Dog volume increased."

    def volume_down(self):
        return "Dog volume decreased."

class RobotSpeaker(Speaker):
    def speak(self):
        return "Beep boop."

    def volume_up(self):
        return "Robot volume increased electronically."

    def volume_down(self):
        return "Robot volume decreased electronically."

# You cannot instantiate Speaker directly:
# speaker = Speaker()  # TypeError: Can't instantiate abstract class Speaker with abstract methods speak, volume_up, volume_down

dog_speaker = DogSpeaker()
robot_speaker = RobotSpeaker()

def announce(speaker):
    print(speaker.speak())

announce(dog_speaker)   # Output: Woof!
announce(robot_speaker) # Output: Beep boop.

