#Happn API Python Module
A module for interacting with Happn's REST API.

##Installation

Download the source and run:
```
	python setup.py install
```

##What is included
```
	\happn 	- Source
	\docs	- Documentation of functions
	\bin	- Prebuilt scripts using python Happn API
	\examples - exmaple implementations	
```

##Getting Started
First you need a facebook token to create a Happn User-Object. You can get the one associated with your facebook account by clicking [here](https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token) and copying it from the address bar.

```python
import happn
import pprint #For dictionary printing

token = <your facebook token>

# Generate the Happn User object
myUser = happn.User(token)

# Get user info of a specific user
targetUserDict = myUser.get_user_info(<target user id>)
pprint.pprint(targetUserDict)

# Set user position
myUser = myUser.set_position(20.0477203,-156.5052441) #Hawaii lat/lon
```

####Using the Scripts

####Using the API

##ToDo
-Easier Setting Configuration
-Unimplemented API Calls
    -Liking a User
    -Charming a User
    -Send a message
    -Get conversations
    -Get messages
Add Scripts