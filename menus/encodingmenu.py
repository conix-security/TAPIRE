import click
from netzob.all import *
from netzob.Common.Utils.TypedList import TypedList

from menus.manipulatemenu import manipulate_menu
from utilities import symbolselector


def encoding_menu(symbols,symbol_selector,syms = None):
    click.echo(click.style("Available encodings:\n", fg="blue"))
    click.echo(click.style("[1]", fg="green") + click.style(": ASCII\n", fg="blue"))
    click.echo(click.style("[2]", fg="green") + click.style(": Raw\n", fg="blue"))
    click.echo(click.style("[3]", fg="green") + click.style(": Bitarray\n", fg="blue"))
    click.echo(click.style("[4]", fg="green") + click.style(": Integer\n", fg="blue"))
    click.echo(click.style("[5]", fg="green") + click.style(": HexaString\n", fg="blue"))
    click.echo(click.style("[6]", fg="green") + click.style(": IPV4\n", fg="blue"))
    click.echo(click.style("[7]", fg="green") + click.style(": TimeStamp\n", fg="blue"))
    encoding_selector = input(" PLEASE SELECT AN ENCODING FUNCTION >>>   ")
    enconding_menu_choice(symbols,symbol_selector,encoding_selector,syms)

def enconding_menu_choice(symbols,symbol_selector,encoding_selector,syms):
    if(encoding_selector == "1"):
        encoding = TypeEncodingFunction(ASCII)
    elif(encoding_selector == "2"):
        encoding = TypeEncodingFunction(Raw)
    elif(encoding_selector == "3"):
        encoding = TypeEncodingFunction(BitArray)
    elif (encoding_selector == "4"):
        encoding = TypeEncodingFunction(Integer)
    elif (encoding_selector == "5"):
        encoding = TypeEncodingFunction(HexaString)
    elif (encoding_selector == "6"):
        encoding = TypeEncodingFunction(IPv4)
    elif (encoding_selector == "7"):
        encoding = TypeEncodingFunction(Timestamp)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        encoding_menu(symbols,symbol_selector)

    add_encoding_function(symbols,symbol_selector,encoding,syms)

def add_encoding_function(symbols, symbol_selector,encoding,syms):
    if isinstance(symbols, list) or isinstance(symbols, TypedList):
        if symbol_selector == "*":
            for symbol in symbols:
                symbol.addEncodingFunction(encoding)
        else:
            symbol = symbolselector.selectsymbol(symbols, symbol_selector)
            symbol.addEncodingFunction(encoding)
    else:
        symbols.addEncodingFunction(encoding)
    if syms is None:
        manipulate_menu(symbols)
    else:
        manipulate_menu(syms)