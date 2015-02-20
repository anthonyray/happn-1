# Happn Userbase Enumeration tool

IN PROGRESS - NOT YET OPERATIONAL

### Theory

~~##### Radius Method

1. Get recs normally with large limit (get max recs)
2. Change radius settings and see if it will increase the total recs given~~
Unfortunately the radius setting cannot be changed.

##### Sybil/Cover Method
Should work, but timely. Using sybils will decrease time by factor of n sybils

1. set bottom x,y coord
2. get recs, move radius amount
3. get recs again
4. repeat 2 given under HTTP 429 rate limiting time

__enumUsers.py__ - Main script
_TODO_:
+ include progress
+ mapping
+ add to db
+ add x,y to db for later calcs of lonliest part of area or other metrics

_Concerns_:
    OAuth tokens will time-out

__determineTimeout.py__ - Used to determine Happn's position change timeout. Determined to be 20 minutes.



__enumCalc.py__ - Determines the approx amount of time to cover some area. Does not yet support args