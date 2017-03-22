import click
import io
import sys


from netzob.all import *

import symbolselector

from manipulatemenu import manipulate_menu

def relationfinder_menu(symbol_selector,symbols):
    click.echo(click.style("LONG PROCESS...\n", fg="blue"))
    click.echo(click.style("[1] : ", fg="green") + click.style(" Finding relations ",fg="blue"))
    find_relations(symbol_selector,symbols)


def find_relations(symbol_selector,symbols):
    old_stdout = sys.stdout
    sys.stdout = tempstdout = io.StringIO()
    rels = []
    if isinstance(symbols, list):
        if symbol_selector == "*":
            for symbol in symbols:
                rels += RelationFinder.findOnSymbol(symbol)
        else:
            symbol = symbolselector.selectsymbol(symbols, symbol_selector)
            rels += RelationFinder.findOnSymbol(symbol)
    else:
        rels += RelationFinder.findOnSymbol(symbols)
    click.echo(click.style("[Relations found] : ", fg="red")+ "\n")
    for i in rels:
        for rel in i:
            print("  " + rel["relation_type"] + ", between '" + rel["x_attribute"] + "' of:")
            print("    " + str('-'.join([f.name for f in rel["x_fields"]])))
            p = [v.getValues()[:] for v in rel["x_fields"]]
            print("    " + str(p))
            print("  " + "and '" + rel["y_attribute"] + "' of:")
            print("    " + str('-'.join([f.name for f in rel["y_fields"]])))
            p = [v.getValues()[:] for v in rel["y_fields"]]
            print("    " + str(p))
    sys.stdout = old_stdout
    click.echo_via_pager(tempstdout.getvalue())
    manipulate_menu(symbols)