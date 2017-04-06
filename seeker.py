import click

from netzob.all import *

import symbolselector

from manipulatemenu import manipulate_menu

#TODO Get Debug log output from Netgoblin IPSEEKER
def metaseeker_menu(symbol_selector,symbols):

    click.echo(click.style("Available Metadata:\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[Create Fields]", fg = "cyan") + '\n')
    click.echo(click.style("[2] ", fg = "green") + click.style("[Don't create Fields]", fg = "cyan") + '\n')
    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    metaseeker_menu_choice(seeker_selector, symbols, symbol_selector)

def metaseeker_menu_choice(seeker_selector,symbols,symbol_selector):

    symbol = symbolselector.selectsymbol(symbols, symbol_selector)
    seeker = IPSeeker()
    click.echo(click.style("[1] ", fg="green") + click.style("[Search for two term IPs]", fg="cyan") + '\n')
    click.echo(click.style("[2] ", fg="green") + click.style("[Don't search for two term IPs]", fg="cyan") + '\n')
    two_t = input(" PLEASE SELECT A CHOICE >>>   ")
    if (seeker_selector == "1"):
        if two_t:
            try:
                seeker.executeOnSymbol(symbol=symbol, create_fields=True,two_terms=True)
            except:
                pass
        else:
            try:
                seeker.executeOnSymbol(symbol=symbol, create_fields=True, two_terms=False)
            except:
                pass
        manipulate_menu(symbols)
    elif (seeker_selector == "2"):
        if two_t:
            try:
                seeker.executeOnSymbol(symbol=symbol, create_fields=False, two_terms=True)
            except:
                pass
        else:
            try:
                seeker.executeOnSymbol(symbol=symbol, create_fields=False, two_terms=False)
            except:
                pass
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        manipulate_menu(symbols)