#Defining the function for search using the Entrez database with a
#short simple text interface and instructions.
def entrezSearch():
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
        try:
            search = Entrez.esearch(db = 'pubmed', term = queryIn)
            record = Entrez.read(search) #search is read in; default RetMax
            articlesList = [] #is 20. This means there will be max 20 
            for i in range(len(record['IdList'])): #articles given. 
                handle = Entrez.esummary(db = 'pubmed', id = record['IdList'][i])
                article = Entrez.read(handle) #Search and read by article id
                artVar = [] #Temporary list to store information of each
                if 'Title' in article[0]: #article. Here we go one by one
                    title = article[0]['Title'] #for the information and if
                    artVar.append(title) #it's available, it is added.
                if 'FullJournalName' in article[0]: #This is to avoid 
                    journal = article[0]['FullJournalName'] #potential key
                    artVar.append(journal) #errors with the dictionary.
                if 'PubDate' in article[0]:
                    pubDate = article[0]['PubDate']
                    artVar.append(pubDate)
                if 'AuthorList' in article[0]:
                    authorList = ', '.join(article[0]['AuthorList'])
                    artVar.append(authorList)
                if 'DOI' in article[0]:
                    DOI = article[0]['DOI']
                    artVar.append(DOI)
                articlesList.append(artVar)
            return articlesList #Articles are all accessible by index
        except u.URLError: #Handy exception for if there are no articles
            print('Your query matched no results. Let\'s try that again.')