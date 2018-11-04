#Importing necessary modules
from Bio import Entrez   #Biopython's Entrez allows database searching
from urllib import error as u   #For handling search errors
Entrez.email = 'jo3500li-s@student.lu.se' #my email
#Description for user; also so they know how to stop the loop
print('This program uses the Entrez databases using the popular Biopython module. \
\n Use the prompt to enter a PubMed search query that will search the PubMed database for articles. \
You can use the standard rules for PubMed searches with brackets and all searches are case-insensitive. \
\n Try it out by typing a protein such as "casein" or an author like "shields d". \
\n\n Oh, one more thing! You can always type either "Q" or "QUIT" to quit. \
\n This is also case-insensitive!')
#Main loop constantly taking input until they say q or quit (case insensitive)
while True: #in order to keep it running constantly
#Upper method on input so that user doesn't have to worry about case
    queryIn = str(input('Enter a PubMed Search Query: \n')).upper()
    if queryIn == 'Q' or queryIn == 'QUIT':
        print('Good bye!')
        break #Stops loop!
#If you quit on the first iteration the function will obviously return
#Nothing AKA None
    while True: #Publication date range; N just skips this
        timeReq = str(input('Would you like to specify a publication date? \n \
                        Type "Y" OR "N" \n')).upper()
        if timeReq == 'N':
            break
        elif timeReq == 'Y':
            timeStartIn = str(input('Enter the starting year: \n'))
            timeEndIn = str(input('Enter the end year: \n'))
            timeVar = '"' + timeStartIn + '"[PDAT] : "' + timeEndIn + '"[PDAT]'
            queryIn += timeVar
            break
        else: #To force them to give an answer in case they write
            print('Please type "Y" or "N"\n') #something like "octopus"
    while True: #RetMax specification; N just skips this
        RetReq = str(input('\nWould you like to specify a maximum number of articles that this program finds? \n Default is 20. \n Type "Y" OR "N" \n')).upper()
        if RetReq == 'N':
            RetMax = 20
            break
        elif RetReq == 'Y':
            RetMax = int(input('Enter the RetMax (maximum articles per search query): \n'))
            break
        else: #To force them to give an answer in case they write
            print('Please type "Y" or "N"\n') #something like "octopus"
    try:
        search = Entrez.esearch(db = 'pubmed', term = queryIn, retmax = RetMax)
        record = Entrez.read(search) #search is read in; default RetMax
        for i in range(len(record['IdList'])): #articles given. 
            handle = Entrez.esummary(db = 'pubmed', id = record['IdList'][i])
            article = Entrez.read(handle)
            title = article[0]['Title']
            journal = article[0]['FullJournalName']
            pubDate = article[0]['PubDate']
            authorList = ', '.join(article[0]['AuthorList'])
            DOI = article[0]['DOI']
            print('\nTitle : {0} \nJournal : {1} \nPublication Date : {2} \nAuthors : {3} \nDOI : {4} \n'.format(title, journal, pubDate, authorList, DOI))
    except IndexError: #Handy exception for if there are no articles
        print('Your query matched no results. Let\'s try that again.')
    except KeyError as e:
        cause = e.args[0]
        print('\nThe following information was missing from this article: {0}\n'.format(cause))
