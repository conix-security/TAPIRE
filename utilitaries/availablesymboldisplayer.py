import click
import sys
import io

from utilitaries import symbolselector

def display_available_symbols(symbols,removeSymbol=None):
    symbol = None
    click.echo(click.style("Available symbols:\n", fg="blue"))
    printed = symbols
    #if removeSymbol:
    #    printed.remove(removeSymbol)
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
    return symbol, symbol_selector
