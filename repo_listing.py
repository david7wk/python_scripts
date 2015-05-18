import requests
import sys

if len(sys.argv) < 2:
    print "Usage: repo_listing.py username"
    sys.exit(1)
    
user = sys.argv[1]

url = 'https://api.github.com/users/' + user + '/repos'

r = requests.get(url)

assert r.status_code == 200, 'Error: repo listing failed'

print
print('{0:10s} {1:20s} {2:25s}'.format('Language','Repo Name','Description'))
print('{0:10s} {1:20s} {2:25s}'.format(10*'-', 20*'-', 25*'-'))
for repo in r.json():
    print('{language:10s} {name:20s} {description:25s}'.format(language=repo['language'],
                            name=repo['name'],description=repo['description']))