import requests
import sys

if len(sys.argv) < 2:
    print "Usage: repo_listing.py username"
    sys.exit(1)
    
user = sys.argv[1]

url = 'https://api.github.com/users/' + user + '/repos'

r = requests.get(url)

assert r.status_code == 200


for repo in r.json():
    print('[{language}] {name} {description}'.format(language=repo['language'],
                            name=repo['name'],description=repo['description']))