import sys
import requests
from requests.api import get

# we create a function that calls API for details of the user

def findUserInfo(username):
    url="https:api.github.com/users/" + username
    html = requests.get(url)
    return html.json()

#a function to handle errors if datais not provided

def getField(key,dic):
    if dic[key] is None:
        return 'Not Available'
    return dic[key]

#calling of the functions

if __name__ == '__main__':
    username=input('Enter the Username: ')
    userDetails=findUserInfo(username)
    if 'message' in userDetails.keys():
        print('Username not found')
        sys.exit()
    else:
        print('**Name **\n'+ userDetails['name'], "\n")
        print('**About **\n')
        print('Bio: ', getField('bio', userDetails))
        print('Email', getField('email', userDetails))
        print('Location: ',getField('location', userDetails))
        print('**Profile Details**\n')
        print('Public Repositories: ', userDetails['public_repos'])
        print['Public Gists: ', userDetails['public_gists']]
        print('Followers: ',userDetails['followers'])
        print('Following: ', userDetails['following'])
        