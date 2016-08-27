# import special libraries already built in python
import random
import urllib2

# list of options to select from
url = "https://raw.githubusercontent.com/kaitlinhbui/cool/master/activities.list"
list_raw_text = urllib2.urlopen(url).read()

# print "DEBUG: " + str(list_raw_text.split())

possible_activities = list_raw_text.split()

# choice of what we are going to do
choice = random.choice(possible_activities)

# display the resuts to the ends user
print("Possible activities are: " + str(possible_activities))
print("What we are going to do: " + choice)
