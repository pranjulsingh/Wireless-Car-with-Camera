#!/usr/bin/python
#Author: Pranjul Singh
#Date: 25, October, 2017
#Time: 01:40 am

'''
import os
pwd = os.getcwd()
dirsplit = str.split(pwd, '/')
dirsplit[-1] = 'db_init'
parentdir = '/'.join(dirsplit)
print parentdir
'''

from db_init import Database
from time import sleep


class command:

    def __init__(self):
        # setting controls to initial position
        self.left_motor_speed = 0
        self.right_motor_speed = 0
        self.servo_zero_angle = 0
        self.servo_one_angle = 0
        self.servo_two_angle = 0
        self.servo_three_angle = 0
        self.car_movement = 0
        self.arm_movement = 0
        self.db = Database()

    def get_current_pos(self):
        # prints the current status
        print 'Left motor speed: '+str(self.left_motor_speed)
        print 'Right motor speed: '+str(self.right_motor_speed)
        print 'Servo one angle: '+str(self.servo_one_angle)
        print 'Servo two angle: '+str(self.servo_two_angle)
        print 'Servo three angle: '+str(self.servo_three_angle)

    def read_directions(self):
        # reads the directions of arm and the base from the database
        self.db.database_connect()
        self.db.get_direction_state()
        self.db.close_connection()


if __name__ == '__main__':
    cmd = command()
    while True:
        sleep(0.2
              )
        cmd.read_directions()

