import click
from netzob.Common.Utils.TypedList import TypedList
from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from utilitaries import symbolselector, converter


def split_menu(symbol_selector, symbols,field_selector = None,parent = None):
    click.echo(click.style("[1]", fg="green") + click.style(": Split static\n", fg="blue"))
    click.echo(click.style("[2]", fg="green") + click.style(": Split aligned\n", fg="blue"))
    click.echo(click.style("[3]", fg="green") + click.style(": Split delimiter\n", fg="blue"))
    click.echo(click.style("[B]", fg="green") + click.style(": Go Back to main menu\n", fg="blue"))
    print("\n")
    selector = input("PLEASE SELECT A MENU CHOICE >>>  ")
    print("\n")
    split_menu_choice(selector, symbol_selector, symbols,field_selector,parent)


def split_menu_choice(selector, symbol_selector, symbols,field_selector,parent=None):
    if (selector == "1"):
        click.echo(click.style("SPLIT STATIC\n", fg="yellow"))
        split_static(symbols,  symbol_selector,field_selector)
    elif (selector == "2"):
        click.echo(click.style("SPLIT ALIGNED\n", fg="yellow"))
        split_aligned(symbols, symbol_selector,field_selector)
    elif (selector == "3"):
        click.echo(click.style("SPLIT DELIMITER\n", fg="yellow"))
        split_delimiter(symbols,symbol_selector,field_selector)
    elif (selector == "B"):
        if parent is not None:
            manipulate_menu(parent)
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        split_menu(symbol_selector, symbols,parent)
    return

def split_static(symbols,  symbol_selector,field_selector):
    if symbol_selector == "*":
        for symbol in symbols:
            if field_selector is not None:
                Format.splitStatic(symbol.fields[int(field_selector)])
            else:
                Format.splitStatic(symbol)
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        Format.splitStatic(symbol)
    if isinstance(symbols, TypedList):
        return
    manipulate_menu(symbols)

def split_aligned(symbols, symbol_selector,field_selector):
    if symbol_selector != "*":
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        Format.splitAligned(symbol)
    else:
        for symbol in symbols:
            if field_selector is not None:
                Format.splitAligned(symbol.fields[int(field_selector)],doInternalSlick=True)
            else:
                Format.splitAligned(symbol)
    if isinstance(symbols,TypedList):
        return
    manipulate_menu(symbols)

def split_delimiter(symbols,  symbol_selector,field_selector):
    click.echo(click.style("[1] ", fg="green") + click.style("[Ascii]", fg="blue") + '\n')
    click.echo(click.style("[2] ", fg="green") + click.style("[Raw]", fg="blue") + '\n')
    click.echo(click.style("[3] ", fg="green") + click.style("[HexaString]", fg="blue") + '\n')
    click.echo(click.style("[4] ", fg="green") + click.style("[BitArray]", fg="blue") + '\n')
    click.echo(click.style("[5] ", fg="green") + click.style("[Integer]", fg="blue") + '\n')
    click.echo(click.style("[6] ", fg="green") + click.style("[IPV4]", fg="blue") + '\n')
    click.echo(click.style("[7] ", fg="green") + click.style("[TimeStamp]", fg="blue") + '\n')
    delimiter_Type = input("Please select a type of data for the split delimiter >>>   ")
    if delimiter_Type == "1":
        delimiter_Type = "ASCII"
    elif delimiter_Type == "2":
        delimiter_Type = "Raw"
    elif delimiter_Type == "3":
        delimiter_Type = "Hexadecimal"
    elif delimiter_Type == "4":
        delimiter_Type = "BitArray"
    elif delimiter_Type == "5":
        delimiter_Type = "Integer"
    elif delimiter_Type == "6":
        delimiter_Type = "IPV4"
    elif delimiter_Type == "7":
        delimiter_Type = "TimeStamp"
    else:
        click.echo(click.style("[ERROR] ", fg="red") + click.style("Wrong selection",
                                                                   fg="blue") + '\n')
        split_menu(symbol_selector,symbols)
    delimiter_string = input("Please specify a delimiter >>> ")
    if delimiter_Type == "ASCII":
        delimiter = ASCII(delimiter_string)
    elif delimiter_Type == "Raw":
        delimiter =Raw(converter.input_to_raw(delimiter_string))
    elif delimiter_Type == "Hexadecimal":
        pass
    else:
        click.echo(click.style("[ERROR] ", fg="red") + click.style("Wrong selection",
                                                                   fg="blue") + '\n')
        split_menu(symbol_selector, symbols)
    if symbol_selector == "*":
        for symbol in symbols:
            if field_selector is not None:
                Format.splitDelimiter(symbol.fields[int(field_selector)],delimiter)
            else:
                Format.splitDelimiter(symbol,delimiter)
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        Format.splitDelimiter(symbol,delimiter)
    if isinstance(symbols, TypedList):
        return
    manipulate_menu(symbols)