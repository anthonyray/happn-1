"""enumCalc.py"""

width	= 10 	# in mi
height	= 10 	# in mi
nSybils	= 5
timeout = 20 # in minutes
radius	= .500 # km^2

s_mi = width*height
#s_mi = 303
s_km = s_mi * 2.58999

m_to_completion = ((s_km / radius) / nSybils) * timeout
h_to_completion = m_to_completion / 60
d_to_completion = h_to_completion / 24

print("{} mi^2 will take: {} minutes, {} hours, {} days to complete".format(s_mi, m_to_completion,h_to_completion,d_to_completion))