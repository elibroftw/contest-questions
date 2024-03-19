"""
Take this image of an analog clock showing 09:30
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3sqvzs82go0f3sQH_kzu1smcrk6IAJld2a5bUXNmnOg&s
Think about how the minute affects the position of the hour hand
max hour ticks = 60 minutes * 12
max minute ticks = 60
Keep track of the position of the hands either in degrees (pre-compute) or percentages
My solution using percentages and uses the minute hand as an adjustment rather than doing a divide by 60 * 12
Lastly, now that we have two percentages, we want to find the smallest distance which is either between each other (abs) or an overflow (1 - abs)
"""

import math

def getSmallestClockAngle(timeString, unit):
  # for each string in split, convert to int. since we expect INT:INT, this is safe
  h, m = [int(x) for x in timeString.split(':')]
  # calculate percentage minute hand takes up
  m_p = m / 60
  # calculate percentage hour is (00) and add adjustment due to minutes
  # each 100% minute hand contribute to 1/12 hour hand
  h_p = h / 12 + (m_p / 12)
  # suppose m = 10% and h = 90%
  # the difference is either 80% or 20%
  difference = abs(h_p - m_p)
  difference = min(difference, 1 - difference)
  # 100% == 360 degrees == 2pi
  if unit == 'degrees':
    # int(x) rounds positives down so use round(x)
    return round(360 * difference)
  return round(difference * 2 * math.pi, 4)
