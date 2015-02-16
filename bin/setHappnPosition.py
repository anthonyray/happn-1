#!/usr/bin/env python

""" setHappnPosition.py """
# Set position of a given user
# :param fbToken Facebook token
# :param lat Latitude to place user at
# :param lon Longitude to place user at

__author__      = "Rick Housley"
import happn

def main():
	# Create user object
	user = happn.User(args.token)

	# Set user device (uses my phone config :TODO offload to settings)
	user.setDevice()

	# Set user position
	try:
		user.set_position(args.lat, args.lon)
	except HTTP_MethodError:
		print 'Unable to change position due to HTTP method error: %s', HTTP_MethodError.value

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