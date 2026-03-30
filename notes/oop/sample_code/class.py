class Robot:
  def __init__(self, name):
    self.name = name
    print(f"{self.name} is created.")

  def speak(self, message):
    print(f"{self.name} says: {message}")
  
  def __del__(self):
    print(f"{self.name} is shutting down.")

bot1 = Robot("RoboCop")
bot1.speak("Don't move.")