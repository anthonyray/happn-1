#!/usr/bin/env python

""" determineTimeout.py """
# Determine timeouts between position sets
# :param fbToken Facebook token

__author__      = "Rick Housley"


import happn
from datetime import datetime
import time
import argparse
import logging


def main(args):
	logger = logging.getLogger()
	logger.disabled = True


	# Create user object
	user = happn.User(args.token)

	# Set user position, start stopwatch
	user.set_device()
	try:
		user.set_position(42.3425227,-71.0885269)
	except happn.HTTP_MethodError as e:
		print 'Unable to change position due to HTTP method error: {}'.format(e.value)
		#return False
	start = datetime.now()	
	
	count = 0
	while True:
		# Set user position
		print "{} Attempts".format(count)
			
		try:
			user.set_position(20.3425227,-157.0885269)
		except happn.HTTP_MethodError as e:	
			time.sleep(60)
			count = count + 1
			continue
		break

	end = datetime.now()		

	print "Start Time: {}".format(start)
	print "End Time: {}".format(end)


if __name__ == '__main__':			
	# Generate argparse menu
	parser = argparse.ArgumentParser()
	
	parser.add_argument('--token', required=True,
		dest='token', default=None,
		help='Facebook user token')

	args = parser.parse_args()	
	main(args)