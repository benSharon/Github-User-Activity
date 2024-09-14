import click

from github_manager import (
    get_user_events,
    get_user_repositories
)


@click.command()
@click.argument("username")  # Required argument for the GitHub username
@click.option("-r", "--repo", is_flag=True, help="get user's repositories")
@click.option("-e", "--events", is_flag=True, help="get user's events")
def cli(username, repo, events):
    """
    Command-line tool for displaying GitHub user events and repositories
    """
    if repo:
        click.echo(f"Displaying repositories for user {username}:")
        get_user_repositories(username)
    elif events:
        click.echo(f"Displaying events for user {username}:")
        get_user_events(username)


def main():
    cli()


if __name__ == "__main__":
    main()
