# Happn Userbase Enumeration tool

IN PROGRESS - NOT YET OPERATIONAL

### Theory

##### Radius Method
Unconfirmed to work

1. Get recs normally with large limit (get max recs)
2. Change radius settings and see if it will increase the total recs given

##### Sybil/Cover Method
Should work, but timely. Using sybils will decrease time by factor of n sybils

1. set bottom x,y coord
2. get recs, move radius amount
3. get recs again
4. repeat 2 given under HTTP 429 rate limiting time

__TODO__
for above must calc rate limit timeout time

__Possible Features___
Pre-time calculation