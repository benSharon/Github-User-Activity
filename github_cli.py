import click

from github_manager import get_user_events, get_user_repositories


@click.command()
@click.argument("username")  # Required argument for the GitHub username
@click.option("-r", "--repo", is_flag=True, help="get user's repositories")
@click.option("-e", "--events", is_flag=True, help="get user's events")
def cli(username, repo, events):
    """
    Command-line tool for displaying GitHub user events and repositories
    """
    try:
        if repo:
            get_user_repositories(username)
        elif events:
            get_user_events(username)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    cli()
