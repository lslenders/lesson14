# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:59:02 2016
Jason and Lieven
Team Puma
"""

#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, and outputs
#    them to a CSV file.
#-----------------------------------------------------------------------

from twitter import *
from twython import Twython
import sys
import csv
import os
latitude = 52.3667	# geographical centre of search
longitude = 4.9000	# geographical centre of search
max_range = 1 			# search range in kilometres
num_results = 100		# minimum results to obtain
outfile = "results.csv"

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
APP_KEY = 'CDTJv48Iw1DmipA6sKhOAy2mh'
APP_SECRET = '4S9ap1C29ijcdphNggwTn2jN4WrgWIopbMtG5H869qHB8a5eo3'
OAUTH_TOKEN = '2798921029-3KUlMoPN0J5YlF5WXIGvDb1yPAmqY5PmthgSqJ4'
OAUTH_TOKEN_SECRET = 'WOJeSSdEBjKX9v7XlvD2SSPKHBI622LXakkUlQhGR1ai5'

##initiating Twython object 
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#-----------------------------------------------------------------------
# open a file to write (mode "w"), and create a CSV writer object
#-----------------------------------------------------------------------
os.chdir('/home/user/Desktop/geoscripting/lesson14')
csvfile = file('results.csv', "w")
csvwriter = csv.writer(csvfile)


#-----------------------------------------------------------------------
# add headings to our CSV file
#-----------------------------------------------------------------------
row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)

#-----------------------------------------------------------------------
# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.
#-----------------------------------------------------------------------
result_count = 0
last_id = None
while result_count <  num_results:
	#-----------------------------------------------------------------------
	# perform a search based on latitude and longitude
	# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
	#-----------------------------------------------------------------------
	query = twitter.search(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)

	for result in query["statuses"]:
		#-----------------------------------------------------------------------
		# only process a result if it has a geolocation
		#-----------------------------------------------------------------------
		if result["geo"]:
			user = result["user"]["screen_name"]
			text = result["text"]
			text = text.encode('ascii', 'replace')
			latitude = result["geo"]["coordinates"][0]
			longitude = result["geo"]["coordinates"][1]

			# now write this row to our CSV file
			row = [ user, text, latitude, longitude ]
			csvwriter.writerow(row)
			result_count += 1
		last_id = result["id"]

	#-----------------------------------------------------------------------
	# let the user know where we're up to
	#-----------------------------------------------------------------------
	print "got %d results" % result_count

#-----------------------------------------------------------------------
# we're all finished, clean up and go home.
#-----------------------------------------------------------------------
csvfile.close()

print "written to %s" % outfile