from twilio.rest import Client #Allows twilio API usage
#credentials.py contains my private credentials and my phone numbers for
#twilio. This file is not included for privacy reasons.
from credentials import account_sid, auth_token, my_cell, my_twilio
from entrez import entrezSearch
#initialise twilio client with credentials
client = Client(account_sid, auth_token)
#create output now
myMsg = ''
for i in range(len(entrezSearch())): #first iterate through each article
    article = entrezSearch()[i]
    for i in range(len(article)): #then iterate through each category
        artStr = '\n' #this includes title, journal, authors, etc.
        artStr += '{0}\n'.format(article[i]) #some nice string formatting
    myMsg += artStr
#Sends this as a message to an active phone number
message = client.messages.create(to = my_cell, from_ = my_twilio, body = myMsg)