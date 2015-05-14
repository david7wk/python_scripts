import requests

r = requests.get('https://api.github.com/users/david7wk/repos')

assert r.status_code == 200

for repo in r.json():
    print('[{language}] {name} {description}'.format(language=repo['language'],
                            name=repo['name'],description=repo['description']))