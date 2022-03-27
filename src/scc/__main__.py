import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    SCC (Software Catalog Creator)\n
    Automatically generates a searchable portal for every repsitory of an organization/s or user/s, which is easy to host.\n

    Usage:

    1. (repos) Fetch all repos from the desired organization/s\n
    2. (extract) Extract all metadata for every repo\n
    3. (portal) Generate a searchable portal for all the retreived data\n

    """
    pass 

@cli.command()
@click.option('--input','-i', required=True, help="Organization or user name", metavar='<name-or-path>')
@click.option('--output','-o', default="repos.csv", show_default=True, help="Output csv file", metavar='<path>')
@click.option('--org', 'repo_type', flag_value='orgs', default=True, show_default=True, help="Extracting from a organization")
@click.option('--user', 'repo_type', flag_value='users', default=False, show_default=True, help="Extracting from a user")
def repos(input, output, repo_type):
    """Retreive all organization/s or user/s repositories"""
    from scc.commands import fetch_repositories
    fetch_repositories.fetch(input, output, repo_type)

@cli.command()
@click.option('--input','-i', required=True, help="Pointers to the repositories in csv format", metavar='<csv-repos>')
@click.option('--output','-o', default="repos-metadata", help="Dir where repositories metadata will be saved", metavar='<path>')
def extract(input, output):
    """Fetch and save metadata from introduced repos"""
    from scc.commands import extract_metadata
    extract_metadata.fetch(input, output)

@cli.command()
@click.option('--input','-i', required=True, help="Dir respositories metadata in json format", metavar='<dir-json-metadata>')
@click.option('--output','-o', default="portal", show_default=True, help="Dir where Software Catalog Portal will be saved")
def portal(input, output):
    """Build a portal with a minimalistic desing"""
    from scc.commands.portal import portal
    portal.generate(input, output)

@cli.command()
@click.option('--input','-i', required=True, help="Respository URL", metavar='<url>')
@click.option('--output','-o', default="card.html", show_default=True, help="Output file where the html will be saved", metavar='<path>')
def card(input, output):
    """Create a stand-alone card ready to be embedded in a website"""
    from scc.commands import single_card
    single_card.create(input, output)
