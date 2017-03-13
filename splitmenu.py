
import click
import symbolselector

from netzob.all import *
from manipulatemenu import manipulate_menu

def split_menu( symbol_selector, symbols):
    click.echo(click.style("[1]", fg="green") + click.style(": Split static\n", fg="blue"))
    click.echo(click.style("[2]", fg="green") + click.style(": Split aligned\n", fg="blue"))
    click.echo(click.style("[3]", fg="green") + click.style(": Split delimiter\n", fg="blue"))
    click.echo(click.style("[B]", fg="green") + click.style(": Go Back to main menu\n", fg="blue"))
    print("\n")
    selector = input("PLEASE SELECT A MENU CHOICE >>>  ")
    print("\n")
    split_menu_choice(selector, symbol_selector, symbols)


def split_menu_choice(selector, symbol_selector, symbols):
    if (selector == "1"):
        click.echo(click.style("SPLIT STATIC\n", fg="yellow"))
        split_static(symbols,  symbol_selector)
    elif (selector == "2"):
        click.echo(click.style("SPLIT ALIGNED\n", fg="yellow"))
        split_aligned(symbols, symbol_selector)
    elif (selector == "3"):
        click.echo(click.style("SPLIT DELIMITER\n", fg="yellow"))
    elif (selector == "B"):
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        split_menu( symbol_selector, symbols)


def split_static(symbols,  symbol_selector):
    if (isinstance(symbols, list)):
        if symbol_selector == "*":
          for symbol in symbols:
              Format.splitStatic(symbol)
        else:
            symbol = symbolselector.selectsymbol(symbols, symbol_selector)
            Format.splitStatic(symbol)
    else:
        symbol = symbols
        Format.splitStatic(symbol)
    manipulate_menu(symbols)

def split_aligned(symbols, symbol_selector):
    if (isinstance(symbols, list)):
        if symbol_selector != "*":
            symbol = symbolselector.selectsymbol(symbols, symbol_selector)
            Format.splitAligned(symbol)
        else:
            for symbol in symbols:
                Format.splitAligned(symbol)
    else:
        symbol = symbols
        Format.splitAligned(symbol)
    manipulate_menu(symbols)
