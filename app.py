import requests
import json
from pprint import pprint

url = 'https://api.github.com/users/crhodes76/repos'
print('Making a request to:', url)
response = requests.get(url)
print('Getting response:', response)
data = response.json()
# Extract and print the name attribute from each repository
#for repo in data:
#    print(repo['name'])

# Generate a new list of repository names
print('generating a list of repository names')
repo_names = [repo['name'] for repo in data]
print('repository names:')
for name in repo_names:
    print(name)
