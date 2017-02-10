import click
from termcolor import colored
from api import req

@click.command()
def cli():
    posts = req.top_posts();
    click.echo(colored('Welcome to the Reddit CLI\n', 'blue'))
    for i in range(len(posts)):
        click.echo(str(i + 1) + ". " + colored(posts[i]['data']['title'] + "\n", 'green'))
