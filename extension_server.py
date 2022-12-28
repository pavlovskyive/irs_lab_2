# this imports the SimpleServer library
import SimpleServer
# This imports the functions you defined in searchengine.py
from searchengine import create_index, search, textfiles_in_dir
# has the json.dumps function. So useful
import json

"""
File: extension_server.py
---------------------
This starts a server! Go to http://localhost:8000 to enjoy it. Currently
the server only serves up the HTML. It does not search. Implement code in
the TODO parts of this file to make it work.
"""

# the directory of files to search over
DIRECTORY = 'bbcnews'
# perhaps you want to limit to only 10 responses per search..
MAX_RESPONSES_PER_REQUEST = 10
# stopwords file
STOPWORDS_FILE = 'stopwords.txt'

class SearchServer:
    def __init__(self):
        """
        load the data that we need to run the search engine. This happens
        once when the server is first created.
        """
        self.html = open('extension_client.html').read()
        self.stopwords = open(STOPWORDS_FILE).read().split()

        # index files in *DIRECTORY*
        files = textfiles_in_dir(DIRECTORY)
        index = {}          # index is empty to start
        file_titles = {}    # mapping of file names to article titles is empty to start
        create_index(files, index, file_titles, stopwords=self.stopwords, use_stemming=True)

        self.index = index
        self.file_titles = file_titles

    # this is the server request callback function. You can't change its name or params!!!
    def handle_request(self, request):
        """
        This function gets called every time someone makes a request to our
        server. To handle a search, look for the query parameter with key "query"
        """
        # it is helpful to print out each request you receive!
        print(request)

        # if the command is empty, return the html for the search page
        if request.command == '':
            return self.html

        # if the command is search, the client wants you to perform a search!
        if request.command == 'search':
            files = search(self.index, request.params['query'], stopwords=self.stopwords, use_stemming=True)
            files = files[:MAX_RESPONSES_PER_REQUEST]
            titles = list(map(lambda filename: {'title': self.file_titles[filename]}, files))
            json_string = json.dumps(titles) 
            return json_string


def main():
    # make an instance of your Server
    handler = SearchServer()
    # start the server to handle internet requests!
    SimpleServer.run_server(handler, 8000) # make the server

if __name__ == '__main__':
    main()