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
import time
import argparse
import pprint
import logging
from pymongo import MongoClient

def main(args):
	
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
	
	logging.info('%d Facebook tokens loaded from file',len(fbtokens))


	# Connect to database
	client = MongoClient('localhost', 27017)
	db = client.db
	db_users = db.userbase
	
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

	#Each sybil will be seperated by 500m (default radius) and proceed longitudinaly	
	lConvFactor_km 	= 110 		# Conversion fator to degrees lat/lon in km
	lConvFactor_m 	= 110000 	# Conversion fator to degrees lat/lon in m
	r_m = 500
	r_l = r_m / lConvFactor_m 	# Conversion to degrees lat/lon
	
	targetLat = args.width * lConvFactor_km
	targetLon = args.height * lConvFactor_km

	x=[args.lat]
	y=args.lon	
	for __ in range(1,len(sybils)):
		x.append(x[-1]+r_l)		

	while max(x) < targetLat:
		while y < targetLon:			
			idx = 0
			for user in sybils:
				print x[idx], y	
				print user
				print user.id
				# Add a timeout for a sybil?
				while True:
					try:
						user.update_activity()
						user.set_device()	
						time.sleep(10)				
						user.set_position(x[idx],y)
					except happn.HTTP_MethodError as e:	
						time.sleep(60)
						continue
					break

				idx+=1
				print 'finished setting pos of sybil {}'.format(idx)

				# Get Recs and save to database
				recs = user.get_recommendations(limit=1000)				
				logging.info('Got %d recs', len(recs))
				
				# Load database with new recs
				for doc in recs:
					db_users.insert(doc)

					y=y+r_l;

	x = map(lambda z:z+r_l, x)	# Add to r_l to all items in list


if __name__ == '__main__':			
	# Generate argparse menu
	parser = argparse.ArgumentParser()
	
	parser.add_argument('--fbTokenFile', required=True,
		dest='fbTokenFile', default=None,
		help='File loaded with Facebook tokens')

	parser.add_argument('--rLat', type=float, required=True,
		dest='lat', help='Right corner latitude (starting point)')

	parser.add_argument('--rLon', type=float, required=True,
		dest='lon', help='Right corner longitude (starting point)')

	parser.add_argument('--width', type=float, required=True,
		dest='width', help='Width to traverse in kilometers')

	parser.add_argument('--height', type=float, required=True,
		dest='height', help='height to traverse in kilometers')

	args = parser.parse_args()	
	main(args)