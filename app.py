import click
import requests

POST_URL = "http://localhost:8000/upload"
SITE_POST_LABEL = "notebook-data"


@click.command()
@click.argument(
    "notebook",
    required=False,
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        allow_dash=False,
    ),
)
def main(notebook):
    check_notebook(notebook)
    click.echo("\nWelcome to NbHub!")
    click.echo("Consider supporting us at: https://duarteocarmo.com\n")
    click.echo(f"You are about to publish {notebook}\n")
    click.confirm("Are you sure you want to publish it?", abort=True)
    if click.confirm("Do you wish to set a password?"):
        click.echo("")
        click.echo(
            f"Private notebooks are not available yet! 😬, check https://duarteocarmo.com for updates"
        )

    else:
        check_status()
        files = {SITE_POST_LABEL: open(notebook, "rb")}
        response = requests.post(POST_URL, files=files)
        if response.status_code == 200:
            link = response.json().get("path")
            click.echo("")
            click.echo("Published! ✨")
            click.echo(f"Visit your notebook at: {link}\n")

        else:
            click.echo("Sorry, something went wrong 😔")


def check_notebook(notebook):
    if not notebook:
        click.echo("No notebook provided, nothing to do 😇")
        click.Context.exit(0)


def check_status():
    click.echo("\nQuerying the interwebs.. 🌎")
    try:
        requests.get(POST_URL)
    except Exception:
        click.echo("Sorry.. Our service appears to be down atm.")
        click.Context.exit(0)


if __name__ == "__main__":
    main()
