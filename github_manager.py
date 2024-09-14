import requests

API_URL = "https://api.github.com"


status_codes = {
    200: "OK",
    304: "Not modified",
    403: "Forbidden",
    503: "Service unavailable"
}


def get_user_events(username: str):
    pass


def get_user_repositories(username: str):
    BASE_URL = f"{API_URL}/users/{username}/repos"
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        repository = response.json()
        print(f"Status code {response.status_code} is {status_codes[response.status_code]}")
        display_user_repositories(repository, username)
    else:
        return print(f"Status code {response.status_code} is {status_codes[response.status_code]}")


def display_user_repositories(repo_list, username):
    get_user_repositories(username)
    if repo_list:
        print(f"Repositor{'ies' if len(repo_list) > 1 else 'y'} of {username}:")
        for repo in repo_list:
            print(f"{repo["name"]}")
    else:
        print(f"Failed to get repos.")
