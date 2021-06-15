import click


@click.command()
@click.option("--string", default="", help="Enter anything in quotes.")
@click.argument("filename", type=click.File("w"), default="-", required=False)
def cli(string, filename):
    """
    Creates a specified file and save your data there.
    """
    data = filename.write(string)
    click.echo(file=filename)
    return click.echo("Your data is saved successfully.") if data else ""


if __name__ == "__main__":
    cli()
