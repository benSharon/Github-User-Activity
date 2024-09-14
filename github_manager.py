import os
import requests

API_URL = "https://api.github.com"
TOKEN_FILE = "github_token.txt"


def authenticate():
    # read token from github_token file
    with open(TOKEN_FILE, "r") as file:
        TOKEN = file.read()

    if not TOKEN:
        raise ValueError("Github PAT (personal access token) is missing.")
    return {
        "Authorization": f"token {TOKEN}"
    }


def get_user_events(username: str):
    BASE_URL = f"{API_URL}/users/{username}/events"
    pass


def get_user_repositories(username: str):
    BASE_URL = f"{API_URL}/users/{username}/repos"
    headers = authenticate()
    response_repos = requests.get(BASE_URL, headers=headers)

    if response_repos.status_code == 200:
        repository = response_repos.json()
        print(f"Status code {response_repos.status_code}: {response_repos.reason}")
        display_user_repositories(repository, username)
    else:
        return print(f"Status code {response_repos.status_code} is {response_repos.reason}")


def display_user_repositories(repo_list, username):
    if repo_list:
        print(f"Repositor{'ies' if len(repo_list) > 1 else 'y'} of {username}:")
        for repo in repo_list:
            print(f"{repo["name"]}")
    else:
        print(f"Failed to get repos.")
