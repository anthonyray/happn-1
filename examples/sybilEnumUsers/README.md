# Happn Userbase Enumeration tool

IN PROGRESS

### Theory
Should work, but timely. Using sybils will decrease time by factor of n sybils

1. Set bottom x,y coordinates
2. Get recs, move radius amount
3. Get recs again
4. Repeat 2 given under HTTP 429 rate limiting time

__enumUsers.py__ - Main script

__TODO__:
+ Make table mapping for length of lat, lon degree
    + http://www.ncgia.ucsb.edu/education/curricula/giscc/units/u014/tables/table01.html
    + http://www.ncgia.ucsb.edu/education/curricula/giscc/units/u014/tables/table02.html

__determineTimeout.py__
Used to determine Happn's position change timeout. Determined to be 20 minutes.