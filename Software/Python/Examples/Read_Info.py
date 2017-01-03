#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading BrickPi3 information
#
# Results: Print information about the attached BrickPi3.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

try:
    # Each of the following BP.get functions return a list of 2 values
    #     The first item in the list is the value (what we want to display).
    #     The second item in the list is the error value (should be equal to BP.SUCCESS if the value was read successfully)
    print("Manufacturer    : ", BP.get_manufacturer()[0]    ) # read and display the serial number
    print("Board           : ", BP.get_board()[0]           ) # read and display the serial number
    print("Serial Number   : ", BP.get_id()[0]              ) # read and display the serial number
    print("Hardware version: ", BP.get_version_hardware()[0]) # read and display the hardware version
    print("Firmware version: ", BP.get_version_firmware()[0]) # read and display the firmware version
    print("Battery voltage : ", BP.get_voltage_battery()[0] ) # read and display the current battery voltage
    print("9v voltage      : ", BP.get_voltage_9v()[0]      ) # read and display the current 9v regulator voltage
    print("5v voltage      : ", BP.get_voltage_5v()[0]      ) # read and display the current 5v regulator voltage
    print("3.3v voltage    : ", BP.get_voltage_3v3()[0]     ) # read and display the current 3.3v regulator voltage
    
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    pass