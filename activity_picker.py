# import special libraries already built in python
import random

# list of options to select from
possible_activities = ['a', 'b', 'c', 'd', 'e', 'f']

# choice of what we are going to do
choice = possible_activities[random.randint(0, 5)]

# display the resuts to the ends user
print("Possible activities are: " + str(possible_activities))
print("What we are going to do: " + choice)
