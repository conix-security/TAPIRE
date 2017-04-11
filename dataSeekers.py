import click

from manipulatemenu import manipulate_menu
from seeker import metaseeker_menu
from crcseeker import crcSeeker_menu
from headerSeeker import headerSeeker_menu

#TODO Get Debug log output from Netgoblin CRCSEEKER
def dataSeeker_menu(symbol_selector,symbols):

    click.echo(click.style("Available Metadata:\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[IP Seeker]", fg = "blue") + '\n')
    click.echo(click.style("[2] ", fg = "green") + click.style("[CRC32 Seeker]", fg = "blue") + '\n')
    click.echo(click.style("[3] ", fg = "green") + click.style("[Header Seeker]", fg = "blue") + '\n')
    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    dataSeeker_menu_choice(seeker_selector, symbols, symbol_selector)

def dataSeeker_menu_choice(seeker_selector,symbols,symbol_selector):

    if (seeker_selector == "1"):
        click.echo(click.style("SEARCH FOR IPS\n", fg="yellow"))
        metaseeker_menu(symbol_selector, symbols)
    elif (seeker_selector == "2"):
        click.echo(click.style("SEARCH FOR CRC32\n", fg="yellow"))
        crcSeeker_menu(symbol_selector, symbols)
    elif (seeker_selector == "3"):
        click.echo(click.style("SEARCH FOR HEADER AND DATA FIELDS\n", fg="yellow"))
        headerSeeker_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        manipulate_menu(symbols)