import io
import sys
import click

from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from utilitaries import symbolselector


def entropyfinder_menu(symbol_selector,symbols):
    click.echo(click.style("ANALYZING ENTROPY",fg="yellow"))
    find_entropy(symbol_selector,symbols)
    manipulate_menu(symbols)

def find_entropy(symbol_selector,symbols):

    rels = []
    if symbol_selector == "*":
        for symbol in symbols:
            byte_entropy = [byte_entropy for byte_entropy in EntropyMeasurement.measure_entropy(symbol.messages)]
            rels.append(byte_entropy)
        display_results(rels,symbols,symbol_selector)
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        byte_entropy = [byte_entropy for byte_entropy in EntropyMeasurement.measure_entropy(symbol.messages)]
        rels.append(byte_entropy)
        display_results(rels,symbols,symbol_selector)


def display_results(rels,symbols,symbol_selector):
    old_stdout = sys.stdout
    sys.stdout = tempstdout = io.StringIO()
    click.echo(click.style("[Relations found] : ", fg="red") + "\n")
    for i,bytes_entropy in enumerate(rels):
        if symbol_selector == "*":
                print(symbols[i].name)
                print(bytes_entropy)
        else:
            symbol  = symbolselector.selectsymbol(symbols,symbol_selector)
            print(symbol.name)
            print(bytes_entropy)
    sys.stdout = old_stdout
    if symbol_selector == "*":
        click.echo_via_pager(tempstdout.getvalue())
    else:
        click.echo(tempstdout.getvalue())