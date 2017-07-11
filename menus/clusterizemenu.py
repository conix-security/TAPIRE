import io
import sys

import click
from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from utilitaries import symbolselector, replace_symbols


def clusterize_menu(symbols,symbol_selector):

    click.echo(click.style("Clusterize :", fg="blue"))
    click.echo(click.style("[1]", fg="green") + click.style(": Cluster by size\n", fg="blue"))
    click.echo(click.style("[2]", fg="green") + click.style(": Cluster by alignment\n", fg="blue"))
    click.echo(click.style("[3]", fg="green") + click.style(": Cluster by applicative data\n", fg="blue"))
    if symbol_selector != "*":
        click.echo(click.style("[4]", fg="green") + click.style(": Cluster by CRC32 field\n", fg="blue"))
        click.echo(click.style("[5]", fg="green") + click.style(": Cluster by key field\n", fg="blue"))
    click.echo(click.style("[B]", fg="green") + click.style(": Back to manipulate menu\n", fg="blue"))
    print("\n")
    selector = input("PLEASE SELECT A MENU CHOICE >>>  ")
    print("\n")
    clusterize_menu_choice(selector, symbols, symbol_selector)

def clusterize_menu_choice(selector,symbols,symbol_selector):
    if (selector == "1"):
        click.echo(click.style("CLUSTER BY SIZE\n", fg="yellow"))
        clusterize_by_size(symbols, symbol_selector)
    elif (selector == "2"):
        click.echo(click.style("CLUSTER BY ALIGNMENT\n", fg="yellow"))
        clusterize_by_alignment(symbols,symbol_selector)
    elif (selector == "3"):
        click.echo(click.style("CLUSTER BY APPLICATIVE DATA\n", fg="yellow"))
        #clusterize_by_applicative(symbols,symbol_selector)
    elif (selector == "4" and symbol_selector != "*"):
        click.echo(click.style("CLUSTER BY CRC32\n", fg="yellow"))
        clusterize_by_CRC(symbols, symbol_selector)
    elif (selector == "5" and symbol_selector != "*"):
        click.echo(click.style("CLUSTER BY KEY FIELD\n", fg="yellow"))
        clusterize_by_key_field(symbols, symbol_selector)
    elif (selector == "B"):
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        clusterize_menu(symbols, symbol_selector)

# def clusterize_by_applicative(symbols, symbol_selector):
#     if symbol_selector == "*":
#         messages = []
#         for symbol in symbols:
#             messages += symbol.messages.list
#     else:
#         symbol = symbolselector.selectsymbol(symbols, symbol_selector)
#         messages = symbol.messages.list
#     new_symbols = Format.clusterByApplicativeData(messages,appDatas)
#     if not isinstance(new_symbols,list):
#         new_symbols = [new_symbols ]
#     if new_symbols[0].name == "Symbol":
#         index=0
#         for sym in new_symbols:
#             sym.name = "Symbol-" + str(index)
#             index += 1
#     manipulate_menu(new_symbols)

def clusterize_by_size(symbols,symbol_selector):
    if symbol_selector == "*":
        messages = []
        for symbol in symbols:
            messages += symbol.messages.list
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        messages = symbol.messages.list
    new_symbols = Format.clusterBySize(messages)
    manipulate_menu(new_symbols)

def clusterize_by_alignment(symbols,symbol_selector):
    if symbol_selector == "*":
        messages = []
        for symbol in symbols:
            messages += symbol.messages.list
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        messages = symbol.messages.list
    new_symbols = Format.clusterByAlignment(messages)
    if not isinstance(new_symbols,list):
        new_symbols = [new_symbols ]
    if new_symbols[0].name == "Symbol":
        index=0
        for sym in new_symbols:
            sym.name = "Symbol-" + str(index)
            index += 1
    manipulate_menu(new_symbols)

def clusterize_by_CRC(symbols,symbol_selector):
    if symbol_selector == "*":
        messages = []
        for symbol in symbols:
            messages += symbol.messages.list
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        messages = symbol.messages.list
    new_symbols = Format.clusterByCRC(messages)
    if symbol_selector != "*":
        replace_symbols.replace_symb(symbols, symbol, new_symbols)
    else:
        symbols = new_symbols
    manipulate_menu(symbols)

def clusterize_by_key_field(symbols,symbol_selector):
    if symbol_selector == "*":
        click.echo(click.style("[ERROR] ", fg="red") + click.style("Selector can't be * for key field clustering!",
                                                                   fg="blue") + '\n')
        manipulate_menu(symbols)
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        display_symbol(symbol)
        for index, field in enumerate(symbol.fields):
            click.echo(click.style("[" + str(index) + "] ", fg="green") + click.style("Field-", fg="blue") + str(index))
        field_index = input("Please Select a field to cluster >>> ")
        field = symbol.fields[int(field_index)]
    new_symbols = Format.clusterByKeyField(symbol, field)
    replace_symbols.replace_symb(symbols, symbol, new_symbols)
    manipulate_menu(symbols)

def display_symbol(symbol):
    old_stdout = sys.stdout
    sys.stdout = tempstdout = io.StringIO()
    click.echo(click.style("[Available fields for clustering]", fg="red") + "\n")
    click.echo(click.style("[", fg="red") + click.style(symbol.name) + click.style("]", fg="red"))
    print(symbol)
    sys.stdout = old_stdout
    click.echo_via_pager(tempstdout.getvalue())