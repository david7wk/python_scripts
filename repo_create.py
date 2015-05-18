import requests, json
import sys


if len(sys.argv) < 5:
    print "Usage: repo_delete.py username password repo_name description"
    sys.exit(1)
    
user = sys.argv[1]
password = sys.argv[2]
repo = sys.argv[3]
description = sys.argv[4]

url = 'https://api.github.com/user/repos'

repo_info = {}
repo_info['name'] = repo
repo_info['description'] = description

data = json.dumps(repo_info)

r = requests.post(url, data, auth=(user, password))

assert r.status_code == 201, 'Error: repo create failed'

print "Repository ",repo," successfully created."

