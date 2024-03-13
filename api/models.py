from django.db import models

# Create your models here.
class DeviceS7(models.Model):
    sensor = models.BooleanField(default=False)
    button = models.BooleanField(default=False)
    turn_on_robot = models.BooleanField(default=False)
    reset_counter = models.BooleanField(default=False)
    count_value = models.IntegerField(default=0)

    def __str__(self):
        return f"Sensor: {self.sensor}, Button: {self.button}, TurnOnRobot: {self.turn_on_robot}, ResetCounter: {self.reset_counter}, CountValue: {self.count_value}"