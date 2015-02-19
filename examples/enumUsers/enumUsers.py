#!/usr/bin/env python

""" enumUsers.py 

	Enumerates all of the users in a given area.

	IN PROGRESS - NOT YET OPERATIONAL	
"""
# Set position of a given user
# :param fbToken Facebook token
# :param lat Latitude to place user at
# :param lon Longitude to place user at

__author__      = "Rick Housley"
import happn

def main():
	# Create user object with passed fbToken	
	user = happn.User(args.token)

	# Set user device (uses my phone config :TODO offload to settings)
	user.setDevice()

	# Set user position
	try:
		user.set_position(args.lat, args.lon)
	except HTTP_MethodError:
		print 'Unable to change position due to HTTP method error: %s', HTTP_MethodError.value

	# Change setting radius to huge

	# Get recomendations, store to a database or dictionary?


	# For confirmation that his will work (radius method)
	#	1. Get recs normally with large limit (get max recs)
	#	2. Change radius settings and see if it will increase the total recs given

	# Sybil / movement method
	#	1. set bottom x,y coord
	#	2. get recs, move radius amount
	#	3. get recs again
	#	4. repeat 2 given under HTTP 429 rate limiting time

		# for above must calc rate limit timeout time

	# add feature of time calculation, using sybils will decrease time by factor of n sybils




if __name__ == '__main__':			
	# Generate argparse menu
	parser = argparse.ArgumentParser()
	
	parser.add_argument('--fbToken', required=True,
		dest='fbToken', default=None,
		help='Facebook user token')

	parser.add_argument('--cLat', type=int, required=True,
		dest='lat', help='latitude')

	parser.add_argument('--cLon', type=int, required=True,
		dest='lon', help='longitude')

	args = parser.parse_args()	
	main(args)