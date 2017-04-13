import click
import sys
import io

import symbolselector

from mainmenu import main_menu

def manipulate_menu(symbols):

    click.echo(click.style("Available symbols:\n", fg="blue"))
    if len(symbols) > 1:
        old_stdout = sys.stdout
        sys.stdout = tempstdout = io.StringIO()
        print(symbols)
        sys.stdout = old_stdout
        click.echo(click.style(tempstdout.getvalue() + "\n", fg="red"))
        print("\n")
        symbol_selector = input(" PLEASE SELECT A SYMBOL >>>   ")
        print("\n")
        if symbol_selector != "*":
            symbol = symbolselector.selectsymbol(symbols,symbol_selector)
    else:
        click.echo(click.style("[symbol_0]" + "\n", fg = "red"))
        symbol_selector = "symbol_0"
        symbol = symbolselector.selectsymbol(symbols,symbol_selector)
    click.echo(click.style(symbol_selector,fg = "red") + click.style(" selected!\n", fg = "blue"))
    if symbol_selector != "*":
        click.echo(click.style("[Symbol description]", fg = "green") + click.style(":" ,fg = "blue") + click.style( symbol.description +"\n", fg = "magenta"))
        click.echo(click.style("Manipulate symbols:\n", fg = "blue"))
        click.echo(click.style("[1]", fg = "green") + click.style(": Display symbols\n", fg = "blue"))
        click.echo(click.style("[2]", fg = "green")+ click.style(": Clusterize\n", fg = "blue"))
        click.echo(click.style("[3]", fg = "green")+ click.style(": Split\n", fg = "blue"))
        click.echo(click.style("[4]", fg="green") + click.style(": Rename symbol\n", fg="blue"))
        click.echo(click.style("[5]", fg="green") + click.style(": Edit symbol description\n", fg="blue"))
        click.echo(click.style("[6]", fg="green") + click.style(": Generate packet according to symbol", fg="blue") +click.style("[WARNING]: STRESSFUL\n", fg="yellow"))
        click.echo(click.style("[7]", fg="green") + click.style(": Manipulate Fields\n", fg="blue"))
        click.echo(click.style("[8]", fg="green") + click.style(": Encode symbol\n", fg="blue"))
        click.echo(click.style("[9]", fg="green") + click.style(": Search for data relations (CRC, IP etc.)\n", fg="blue"))
        click.echo(click.style("[R]", fg="green") + click.style(": RelationFinder", fg="blue") + click.style("[WARNING]: LONG PROCESS...\n", fg="yellow"))
        click.echo(click.style("[B]", fg="green") + click.style(": Back to main menu\n", fg="blue"))
    else:
        click.echo(click.style("Manipulate symbols:\n", fg="blue"))
        click.echo(click.style("[1]", fg="green") + click.style(": Display symbols\n", fg="blue"))
        click.echo(click.style("[2]", fg="green") + click.style(": Clusterize\n", fg="blue"))
        click.echo(click.style("[3]", fg="green") + click.style(": Split\n", fg="blue"))
        click.echo(click.style("[4]", fg="green") + click.style(": Encode symbols\n", fg="blue"))
        click.echo(click.style("[5]", fg="green") + click.style(": Manipulate fields\n", fg="blue"))
        click.echo(click.style("[R]", fg="green") + click.style(": RelationFinder", fg="blue") + click.style("[WARNING]: LONG PROCESS...\n", fg="yellow"))
        click.echo(click.style("[B]", fg="green") + click.style(": Back to main menu\n", fg="blue"))
    print("\n")
    selector = input("PLEASE SELECT A MENU CHOICE >>>  ")
    print("\n")
    manipulate_menu_choice(selector,symbol_selector,symbols)

def manipulate_menu_choice(selector,symbol_selector,symbols):

    if symbol_selector == "*":
        if (selector == "1"):
            click.echo(click.style("DISPLAY SYMBOLS\n", fg="yellow"))
            display_symbols(symbol_selector, symbols)
        elif (selector == "2"):
            click.echo(click.style("CLUSTERIZE MENU\n", fg="yellow"))
            clusterize_menu(symbols,symbol_selector)
        elif (selector == "3"):
            click.echo(click.style("SPLIT MENU\n", fg="yellow"))
            split_menu(symbol_selector, symbols)
        elif (selector == "4"):
            click.echo(click.style("ENCODING MENU\n", fg="yellow"))
            encoding_menu(symbols, symbol_selector)
        elif (selector == "5"):
            click.echo(click.style("MANIPULATE FIELDS MENU\n", fg="yellow"))
            field_manipulate_menu(symbols, symbol_selector)
        elif(selector == "R"):
            click.echo(click.style("RELATION FINDER\n", fg="yellow"))
            relationfinder_menu(symbol_selector,symbols)
        elif (selector == "B"):
            click.echo(click.style("BACK TO MAIN MENU\n", fg="yellow"))
            main_menu(symbols)
        else:
            click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
            manipulate_menu(symbols)
    else:
        if (selector == "1"):
            click.echo(click.style("DISPLAY SYMBOLS\n", fg="yellow"))
            display_symbols(symbol_selector, symbols)
        elif (selector == "2"):
            click.echo(click.style("CLUSTERIZE MENU\n", fg="yellow"))
            clusterize_menu(symbols,symbol_selector)
        elif (selector == "3"):
            click.echo(click.style("SPLIT MENU\n", fg="yellow"))
            split_menu( symbol_selector, symbols)
        elif (selector == "4"):
            click.echo(click.style("RENAMING SYMBOL\n", fg="yellow"))
            rename_symbol(symbols, symbol_selector)
        elif (selector == "5"):
            click.echo(click.style("EDITING SYMBOL DESCRIPTION\n", fg="yellow"))
            edit_symbol_description(symbols, symbol_selector)
        elif (selector == "6"):
            click.echo(click.style("GENERATING PACKET ACCORDING TO SYMBOL\n", fg="yellow"))
            packet_generator(symbols,symbol_selector)
        elif (selector == "7"):
            click.echo(click.style("MANIPULATE FIELDS MENU\n", fg="yellow"))
            field_manipulate_menu(symbols, symbol_selector)
        elif (selector == "8"):
            click.echo(click.style("ENCODING MENU\n", fg="yellow"))
            encoding_menu(symbols, symbol_selector)
        elif (selector == "9"):
            click.echo(click.style("SEARCH FOR DATA RELATIONS\n", fg="yellow"))
            dataSeeker_menu(symbol_selector,symbols)
        elif(selector == "R"):
            click.echo(click.style("RELATION FINDER\n", fg="yellow"))
            relationfinder_menu(symbol_selector,symbols)
        elif (selector == "B"):
            click.echo(click.style("BACK TO MAIN MENU\n", fg="yellow"))
            main_menu(symbols)
        else:
            click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
            manipulate_menu(symbols)

def display_symbols(symbol_selector, symbols):

    old_stdout = sys.stdout
    sys.stdout = tempstdout = io.StringIO()
    if symbol_selector == "*":
        for symbol in symbols:
            click.echo(click.style("[", fg="red") + click.style(symbol.name) + click.style("]", fg="red"))
            print(symbol)
    else:
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        click.echo(click.style("[", fg="red") + click.style(symbol.name) + click.style("]", fg="red"))
        print(symbol)
    sys.stdout = old_stdout
    click.echo_via_pager(tempstdout.getvalue())
    manipulate_menu(symbols)

def rename_symbol(symbols,symbol_selector):

    print("\n")
    click.echo(click.style(symbol_selector, fg="red") + click.style(" selected!\n", fg="blue"))
    print("\n")
    new_name = input("PLEASE INPUT A NEW NAME >>>   ")
    print("\n")
    if isinstance(symbols, list):
        symbol = symbolselector.selectsymbol(symbols, symbol_selector)
        symbol.name = new_name
    click.echo(click.style(new_name, fg="red") + click.style(" was saved!\n", fg="blue"))
    manipulate_menu(symbols)

def edit_symbol_description(symbols,symbol_selector):
    print("\n")
    click.echo(click.style(symbol_selector, fg="red") + click.style(" selected!\n", fg="blue"))
    print("\n")
    if isinstance(symbols,list):
        symbol = symbolselector.selectsymbol(symbols,symbol_selector)
    else:
        symbol = symbols
    click.echo(click.style("[Current symbol description]", fg = "green") + click.style(":" ,fg = "blue") + click.style( symbol.description + "\n", fg = "magenta"))
    print("\n")
    symbol.description = input("PLEASE INPUT A NEW DESCRIPTION >>>   ")
    print("\n")
    click.echo(click.style(symbol.description, fg="red") + click.style(" was saved!\n", fg="blue"))
    manipulate_menu(symbols)

def packet_generator(symbols,symbol_selector):
    symbol = symbolselector.selectsymbol(symbols,symbol_selector)
    click.echo(click.style("[Generated message (Protocol layer)]\n",fg = "green"))
    click.echo(click.style(symbol.specialize(),fg = "red"))
    manipulate_menu(symbols)

#IMPORTS AT BOTTOM BECAUSE TEMPORARY FIX TO CIRCULAR DEPENDENCY http://effbot.org/zone/import-confusion.htm

from clusterizemenu import clusterize_menu
from splitmenu import split_menu
from fieldmanipulatemenu import field_manipulate_menu
from encodingmenu import encoding_menu
from Relation_finder import relationfinder_menu
from dataSeekers import dataSeeker_menu