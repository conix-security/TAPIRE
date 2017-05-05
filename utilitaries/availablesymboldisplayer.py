import click
import sys
import io

from utilitaries import symbolselector

def display_available_symbols(symbols):
    symbol = None
    wrong_input = True
    names = []
    for symbol in symbols:
        names.append(symbol.name)
    while wrong_input:
        click.echo(click.style("Available symbols:\n", fg="blue"))
        printed = symbols
        if len(printed) > 1:
            old_stdout = sys.stdout
            sys.stdout = tempstdout = io.StringIO()
            print(printed)
            sys.stdout = old_stdout
            click.echo(click.style(tempstdout.getvalue() + "\n", fg="red"))
            print("\n")
            symbol_selector = input(" PLEASE SELECT A SYMBOL >>>   ")
            print("\n")
            if symbol_selector != "*":
                symbol = symbolselector.selectsymbol(printed, symbol_selector)
        else:
            click.echo(click.style("[symbol_0]" + "\n", fg="red"))
            symbol_selector = "symbol_0"
            symbol = symbolselector.selectsymbol(printed, symbol_selector)
        if symbol_selector in names or symbol_selector == "*":
            wrong_input = False
    return symbol, symbol_selector
