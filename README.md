
# GitHub CLI Tool

This command-line tool allows you to fetch and display GitHub user events and repositories using the GitHub API.

## Features

- **Fetch Repositories**: Retrieve and display all public repositories of a GitHub user.
- **Fetch Events**: Retrieve and display recent public events performed by a GitHub user, such as pushes and repository creations.

## Requirements

- Python 3.x
- [Click](https://click.palletsprojects.com/en/8.0.x/) - for building the command-line interface
- [Requests](https://docs.python-requests.org/en/latest/) - for making HTTP requests to the GitHub API

## Setup

1. Clone the repository.
   
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Generate a [GitHub Personal Access Token (PAT)](https://github.com/settings/tokens) and store it in a file named `github_token.txt` in the root directory of the project.

## Usage

Run the command with either the `--repo` or `--events` option:

### Get Repositories

```bash
python github_cli.py <username> --repo
```

Example:
```bash
python github_cli.py octocat --repo
```

### Get Events

```bash
python github_cli.py <username> --events
```

Example:
```bash
python github_cli.py octocat --events
```

### Command Help

```
python github_cli.py --help
```
```
Usage: github_cli.py [OPTIONS] USERNAME

  Command-line tool for displaying GitHub user events and repositories

Options:
  -r, --repo    get user's repositories
  -e, --events  get user's events
  --help        Show this message and exit.
```

## Example Output

### Repositories

```
Repositories of octocat:
- Hello-World
- Spoon-Knife
- octocat.github.io

Number of repos: 3
```

### Events

```
Events of octocat:
- Pushed 2 commits to Hello-World at 2023-09-15T10:00:00Z
- Hello-World repository has been created at 2023-09-01T15:00:00Z
```

## License

This project is licensed under the MIT License.


## Project URL
[https://roadmap.sh/projects/Github-User-Activity](https://roadmap.sh/projects/Github-User-Activity)
