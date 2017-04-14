import click
from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from utilitaries import symbolselector, replace_symbols


#TODO Get Debug log output from Netgoblin CRCSEEKER
def crcSeeker_menu(symbol_selector,symbols):

    click.echo(click.style("Create Fields?\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[Create Fields]", fg = "blue") + '\n')
    click.echo(click.style("[2] ", fg = "green") + click.style("[Don't create Fields]", fg = "blue") + '\n')
    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    crcSeeker_menu_choice(seeker_selector, symbols, symbol_selector)

def crcSeeker_menu_choice(seeker_selector,symbols,symbol_selector):

    symbol = symbolselector.selectsymbol(symbols, symbol_selector)
    seeker = CRCFinder()
    if (seeker_selector == "1"):
        not_work = True
        #Sometimes clustering fails so we apply this quick workaround untill it succeeds
        while not_work:
            new_symbols = clusterize_by_CRC(symbol)
            for sym in new_symbols:
                if sym.name.find("No_CRC") == -1:
                    try:
                        seeker.findOnSymbol(symbol=sym,create_fields=True)
                        not_work = False
                    except:
                        not_work = True
        replace_symbols.replace_symb(symbols, symbol, new_symbols)
        manipulate_menu(symbols)
    elif (seeker_selector == "2"):
        seeker.findOnSymbol(symbol=symbol, create_fields=False)
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        manipulate_menu(symbols)

def clusterize_by_CRC(symbol):
    new_symbols = Format.clusterByCRC(symbol)
    return new_symbols
