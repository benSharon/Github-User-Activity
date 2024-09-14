import requests

API_URL = "https://api.github.com"
TOKEN_FILE = "github_token.txt"


def authenticate():
    # read token from github_token file
    with open(TOKEN_FILE, "r") as file:
        GITHUB_TOKEN = file.read()

    if not GITHUB_TOKEN:
        raise ValueError("Github PAT (personal access token) is missing.")
    return {"Authorization": f"token {GITHUB_TOKEN}"}


def get_user_events(username: str):
    BASE_URL = f"{API_URL}/users/{username}/events"
    headers = authenticate()
    response_events = requests.get(BASE_URL, headers=headers)

    if response_events.status_code == 200:
        events = response_events.json()
        print(
            f"\nStatus code {response_events.status_code}: {response_events.reason}\n"
        )
        display_user_events(events, username)
    else:
        return print(
            f"\nStatus code {response_events.status_code} is {response_events.reason}\n"
        )


def get_user_repositories(username: str):
    BASE_URL = f"{API_URL}/users/{username}/repos"
    headers = authenticate()
    response_repos = requests.get(BASE_URL, headers=headers)

    if response_repos.status_code == 200:
        repository = response_repos.json()
        print(f"\nStatus code {response_repos.status_code}: {response_repos.reason}\n")
        display_user_repositories(repository, username)
    else:
        return print(
            f"\nStatus code {response_repos.status_code} is {response_repos.reason}\n"
        )


def display_user_repositories(repo_list, username):
    if not repo_list:
        raise ValueError("Could not get repos\n")

    print(f"Repositor{'ies' if len(repo_list) > 1 else 'y'} of {username}:")
    for repo in repo_list:
        print(f"- {repo["name"]}")
    print(f"\nNumber of repos: {len(repo_list)}\n")


def display_user_events(events_list, username):
    if not events_list:
        raise ValueError("Could not get events\n")
    else:
        print(f"Event{'s' if len(events_list) > 1 else ''} of {username}:")

        for event in events_list:
            if event["type"] == "PushEvent":
                commit_count = event["payload"]["size"]
                print(
                    f"- Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {event['repo']['name']} at"
                    f" {event['created_at']}"
                )

            if event["type"] == "CreateEvent":
                if event["payload"]["ref_type"] == "repository":
                    print(
                        f"- {event['repo']['name']} {event['payload']['ref_type']} has been created at {event['created_at']}"
                    )
                else:
                    print(
                        f"- {event['payload']['ref_type']} created in {event['repo']['name']} at {event['created_at']}"
                    )
        print()
