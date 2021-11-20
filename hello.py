import click

@click.command(help="This is just a hello app. It does nothing")
@click.option("--name", prompt="I need your name")
# @click.option("--color", prompt="I need your color", help="This is your color")
def hello(name):
    if name == "thor":
        click.echo(click.style(f"Welcome {name}, strongest avenger", fg="red"))
    elif name == "hulk":
        click.echo(click.style(f"Hello {name}", fg="green"))
    else:
        click.echo(click.style(f"Whatever {name}", fg="blue"))
 
if __name__ == "__main__":
    hello()