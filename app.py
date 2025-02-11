import requests
import json
from pprint import pprint
import webbrowser
url = 'https://api.github.com/users/crhodes76/repos'

print('Making a request to:', url)
response = requests.get(url)

print('Getting response status code:', response.status_code)
data = response.json()

print('The URL', response.url)
the_url = response.url
print('Opening the URL in a web browser')
webbrowser.open(the_url)

raw_data = response.text
print('Raw data from the response:')
print(raw_data)

print('Dictionary data from json.loads:')
dictionary_data = json.loads(raw_data)
print(dictionary_data)

# Generate a new list of repository names
print('generating a list of repository names')
repo_names = [repo['name'] for repo in data]
print('repository names:')
for name in repo_names:
    print(name)
