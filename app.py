import requests
import json
from pprint import pprint

url = 'https://api.github.com/users/crhodes76/repos'
response = requests.get(url)
data = response.json()
# Extract and print the name attribute from each repository
#for repo in data:
#    print(repo['name'])

# Generate a new list of repository names
repo_names = [repo['name'] for repo in data]
for name in repo_names:
    print(name)
