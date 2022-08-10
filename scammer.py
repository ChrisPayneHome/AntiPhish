import requests
import os
import random
import string 
import json
import time


random.seed = (os.urandom(1026))

url = #chosen url target

email_end = ('@yahoo.com', '@outlook.com', '@gmail.com', '@harvard.edu', '@email.com', '@oxford.ac.uk', '@yale.edu', '@outlook.co.uk', '@mit.edu', '@Hotmail.com', '@zoho.com', '@mail.com')

names = json.loads(open('JSON/names.json').read())
words = json.loads(open('JSON/words.json').read())

for name in names:
	
	name_extra = ''.join(random.choice(string.digits))

	email = name.lower() + name_extra + random.choice(email_end)
	password = random.choice(words) + str(random.randint(1950, 2021))
	
	try:
		requests.post(url, allow_redirects = False, data = {
			#Form data for post request
		})

		print('Sending email: %s and password: %s' % (email, password))

	except Exception:
		print('Encountered error, beginning again')
		time.sleep(2)

	



