#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sendSMS(): 

	# enter all the details 
	# get app_key and app_secret by registering 
	# a app on sinchSMS 
	number = '+911234567890'
	app_secret = 'jE8s23CZz0+qweBvSAm5Bw=='
	app_key = '142deeeb-62a5-4786-b7f0-0c723f61dde1'

	# enter the message to be sent 
	message = 'Emergency ! M is in Danger !'

	client = SinchSMS(app_key, app_secret) 
	print("Sending '%s' to %s" % (message, number)) 

	response = client.send_message(number, message) 
	message_id = response['messageId'] 
	response = client.check_status(message_id) 

	# keep trying unless the status retured is Successful 
	while response['status'] != 'Successful': 
		print(response['status']) 
		time.sleep(1) 
		response = client.check_status(message_id) 

	print(response['status'])

