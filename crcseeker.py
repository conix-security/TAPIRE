import click

from netzob.all import *

import symbolselector

from manipulatemenu import manipulate_menu

#TODO Get Debug log output from Netgoblin CRCSEEKER
def crcSeeker_menu(symbol_selector,symbols):

    click.echo(click.style("Available Metadata:\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[Create Fields]", fg = "blue") + '\n')
    click.echo(click.style("[2] ", fg = "green") + click.style("[Don't create Fields]", fg = "blue") + '\n')
    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    crcSeeker_menu_choice(seeker_selector, symbols, symbol_selector)

def crcSeeker_menu_choice(seeker_selector,symbols,symbol_selector):

    symbol = symbolselector.selectsymbol(symbols, symbol_selector)
    seeker = CRCFinder()
    if (seeker_selector == "1"):
        seeker.findOnSymbol(symbol=symbol, create_fields=True)
        manipulate_menu(symbols)
    elif (seeker_selector == "2"):
        seeker.findOnSymbol(symbol=symbol, create_fields=False)
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        manipulate_menu(symbols)