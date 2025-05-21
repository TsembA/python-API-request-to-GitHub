import requests

username = "TsembA"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)
repos = response.json()

print(f"🔍 Found {len(repos)} repositories for user: {username}\n")

for repo in repos:
    print(f"📦 Project Name: {repo['name']}")
    print(f"🔗 Project URL: {repo['html_url']}\n")
