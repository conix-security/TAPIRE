import io
import sys
import click

from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from utilities import symbolselector


def relationfinder_menu(symbol_selector,symbols):
    click.echo(click.style("FINDING RELATIONS ",fg="yellow"))
    find_relations(symbol_selector,symbols)
    manipulate_menu(symbols)

def find_relations(symbol_selector,symbols):

    rels = []
    if symbol_selector == "*":
        for symbol in symbols:
            rels = RelationFinder.findOnSymbol(symbol)
            click.echo(click.style("[Symbol] : " + symbol.name, fg="red") + "\n")
            display_results(rels,False)
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        rels += RelationFinder.findOnSymbol(symbol)
        display_results(rels)

def display_results(rels,pager=True):
    old_stdout = sys.stdout
    sys.stdout = tempstdout = io.StringIO()
    click.echo(click.style("[Relations found] : ", fg="red") + "\n")
    for rel in rels:
        print("  " + rel["relation_type"] + ", between '" + rel["x_attribute"] + "' of:")
        print("    " + str('-'.join([f.name for f in rel["x_fields"]])))
        p = [v.getValues()[:] for v in rel["x_fields"]]
        print("    " + str(p))
        print("  " + "and '" + rel["y_attribute"] + "' of:")
        print("    " + str('-'.join([f.name for f in rel["y_fields"]])))
        p = [v.getValues()[:] for v in rel["y_fields"]]
        print("    " + str(p))
    sys.stdout = old_stdout
    if pager:
        click.echo_via_pager(tempstdout.getvalue())
    else:
        click.echo(tempstdout.getvalue())
    #TODO Open IPYTHON shell to apply relation (add example code snippet)
    #click.echo(click.style("Apply relation?\n", fg="blue"))
    #click.echo(click.style("[1] ", fg = "green") + click.style("[Apply relation]", fg = "blue") + '\n')
    #click.echo(click.style("[2] ", fg = "green") + click.style("[Don't apply relation]", fg = "blue") + '\n')
