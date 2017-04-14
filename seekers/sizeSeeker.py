import click
from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from utilitaries import symbolselector


#TODO Get Debug log output from Netgoblin sizeSeeker
def sizeSeeker_menu(symbol_selector,symbols):

    click.echo(click.style("Create Fields?\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[Create Fields]", fg = "blue") + '\n')
    click.echo(click.style("[2] ", fg = "green") + click.style("[Don't create Fields]", fg = "blue") + '\n')
    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    click.echo(click.style("Base Index search :\n", fg="blue"))
    base = True
    while base:
        base_index = input(" PLEASE SELECT A BASE INDEX >>>   ")
        try:
            base_index = int(base_index)
            base = False
        except:
            base = True
    sizeSeeker_menu_choice(seeker_selector, symbols, symbol_selector,base_index)

def sizeSeeker_menu_choice(seeker_selector,symbols,symbol_selector,base_index):

    symbol = symbolselector.selectsymbol(symbols, symbol_selector)
    seeker = SizeFinder()
    if (seeker_selector == "1"):
        seeker.findOnSymbol(symbol=symbol,create_fields=True,baseIndex=base_index)
        manipulate_menu(symbols)
    elif (seeker_selector == "2"):
        seeker.findOnSymbol(symbol=symbol, create_fields=False,baseIndex=base_index)
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        manipulate_menu(symbols)
