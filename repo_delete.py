import requests
import sys

if len(sys.argv) < 4:
    print "Usage: repo_delete.py username password repo_name"
    sys.exit(1)
    
user = sys.argv[1]
password = sys.argv[2]
repo = sys.argv[3]

url = 'https://api.github.com/repos/' + user + '/' + repo


r = requests.delete(url, auth=(user, password))

assert r.status_code == 204, 'Error: repo not deleted'

