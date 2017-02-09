import click
from termcolor import colored

@click.command()
def cli():
    """Example script."""
    click.echo(colored('', 'blue'))
