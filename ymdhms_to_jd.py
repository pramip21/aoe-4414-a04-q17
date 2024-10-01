# ymdhms_to_JD.py
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Pramil Patel
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
# if len(sys.argv)==3:
#   arg1 = sys.argv[1]
#   arg2 = sys.argv[2]
#   ...
# else:
#   print(\
#    'Usage: '\
#    'python3 arg1 arg2 ...'\
#   )
#   exit()

# write script below this line

def ymdhms_to_jd(year, month, day, hour, minute, second):
    if month <= 2:
        year -= 1
        month += 12
    jd = math.floor(365.25*(year+4716)) + math.floor(30.6001*(month+1)) + day + (2-(math.floor(year/100)) + math.floor((math.floor(year/100))/4)) - 1524.5
    day_fract = (hour + (minute/60) + (second/3600)) / 24
    return jd + day_fract

if len(sys.argv) == 7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
else:
    print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')

jd_fract = ymdhms_to_jd(year, month, day, hour, minute, second)

print(jd_fract)