# Happn Userbase Enumeration tool

IN PROGRESS - Works, but not clean

### Theory

~~##### Radius Method~~

~~1. Get recs normally with large limit (get max recs)~~
~~2. Change radius settings and see if it will increase the total recs given~~
Unfortunately the radius setting cannot be changed.

##### Sybil/Cover Method
Should work, but timely. Using sybils will decrease time by factor of n sybils

1. Set bottom x,y coordinates
2. Get recs, move radius amount
3. Get recs again
4. Repeat 2 given under HTTP 429 rate limiting time

__enumUsers.py__ - Main script
_TODO_:
+ include progress
+ mapping
+ add to db
+ add x,y to db for later calculations of longest part of area or other metrics
+ Make table mapping for length of lat, lon degree
    + http://www.ncgia.ucsb.edu/education/curricula/giscc/units/u014/tables/table01.html
    + http://www.ncgia.ucsb.edu/education/curricula/giscc/units/u014/tables/table02.html

_Concerns_:
    OAuth tokens will time-out

__determineTimeout.py__ - Used to determine Happn's position change timeout. Determined to be 20 minutes.



__enumCalc.py__ - Determines the approx amount of time to cover some area. Does not yet support args