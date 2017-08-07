from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from utilitaries.all import *

def identifyHash(symbol_selector,symbols):
    identifyer = HashIdentifyer()
    if symbol_selector == "*":
        for symbol in symbols:
            click.echo(click.style("[Symbol] : " + symbol.name, fg="red") + "\n")
            identifyer.identify(symbol)

    else:
        symbol = symbolselector.selectsymbol(symbols,symbol_selector)
        click.echo(click.style("[Symbol] : " + symbol.name, fg="red") + "\n")
        identifyer.identify(symbol)
    manipulate_menu(symbols)

