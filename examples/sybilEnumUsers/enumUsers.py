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
import argparse
import pprint
from pymongo import MongoClient

def main(args):
	# Create user object with passed fbToken	
	user = happn.User(args.token)

	# Instantiate Logger	
	logging.basicConfig(filename='log.log', level=logging.INFO)
	logging.info('--------------------Logger Initiated--------------------')

	# Load facebook tokens from a file
	fbtokens = None
	try:
		with open(args.fbTokenFile) as f:
			fbtokens = f.read().splitlines()
	except IOError:
		logging.warning('Unable to locate file provided')
		return

	if fbtokens is None:
		logging.warning('Token file void of tokens')		
		return
	else:
		logging.info('%d Facebook tokens loaded from file',len(fbtokens))


	#Connect to database
	client = MongoClient('localhost', 27017)
	db = client.db
	users = db.userbase
	

	# Create a list of Sybils
	sybils = []
	for token in fbtokens:	
		try:		
			sybils.append(happn.User(token))			
		except NameError:
			logging.warning('Error creating sybil, moving on to next token (most likely invalid token)')
	if sybils == []:
		logging.warning('No Sybils to work with, exiting')
		return
	logging.info('Completed sybil generation')

	#Each sybil will be responsible for 



	# # Set user position
	try:
		user.set_position(42.3425227,-71.0885269)
	except happn.HTTP_MethodError as e:
		print 'Unable to change position due to HTTP method error: {}'.format(e.value)

	# Change match_dsistance setting radius to huge

	user.set_device()

	dist = 500
	payload = {"matching_distance": dist}
	user.set_settings(payload)
	user.update_activity()
	initialRecs = user.get_recommendations(limit=1000);
	print len(initialRecs)



if __name__ == '__main__':			
	# Generate argparse menu
	parser = argparse.ArgumentParser()
	
	parser.add_argument('--fbToken', required=True,
		dest='token', default=None,
		help='Facebook user token')

	parser.add_argument('--cLat', type=int,
		dest='lat', help='latitude')

	parser.add_argument('--cLon', type=int,
		dest='lon', help='longitude')

	args = parser.parse_args()	
	main(args)