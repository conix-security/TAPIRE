from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from utilitaries.all import *

def identifyHash(symbol_selector,symbols):
    symbol = symbolselector(symbols,symbol_selector)
    identifyer = HashIdentifyer()
    identifyer.identify(symbol)
    manipulate_menu(symbols)

