import io
import sys

import click
from netzob.all import *

from menus.manipulatemenu import manipulate_menu
from menus.splitmenu import split_menu
from menus.encodingmenu import encoding_menu
from utilities import symbolselector
from utilities.window import tkinter_window
from utilities.availablefielddisplayer import *
from utilities.nameUnique import make_unique_names

def field_manipulate_menu(symbols, symbol_selector):
    if symbol_selector == "*":
        field_manipulate_menu_wildcard_symbol(symbols, symbol_selector)
    symbol = symbolselector.selectsymbol(symbols, symbol_selector)
    click.echo(click.style(symbol_selector, fg="red") + click.style(" selected!\n", fg="blue"))
    click.echo(click.style("[Symbol description]", fg="green") + click.style(":", fg="blue") + click.style(
        symbol.description + "\n", fg="magenta"))
    make_unique_names(symbol.fields)
    field, field_selector,child = display_available_fields(symbol.fields)
    click.echo(click.style(field_selector,fg = "red") + click.style(" selected!\n", fg = "blue"))
    if child:
        print_menu_choices(symbols, symbol_selector, field_selector, field, field.parent.fields)
    else:
        print_menu_choices(symbols,symbol_selector,field_selector,field,symbol.fields)

def field_manipulate_menu_wildcard_symbol(symbols,symbol_selector):
    click.echo(click.style("ALL SYMBOLS SELECTED\n", fg="yellow"))
    field_selector = "*"
    while field_selector == "*":
        field_selector = input("PLEASE SELECT THE INDEX OF A FIELD >>>  ")
        if field_selector == "*":
            click.echo(click.style("[ERROR] :", fg="red") + click.style("SELECTOR CAN'T BE * !\n", fg="yellow"))
    click.echo(click.style("Field-" + field_selector, fg="red") + click.style(" selected!\n", fg = "blue"))
    print_menu_choices(symbols,symbol_selector,field_selector)

def print_menu_choices(symbols,symbol_selector,field_selector,field=None,fields=None):
    if symbol_selector != "*":
        if field_selector != "*":
            click.echo(click.style("[Field description]", fg = "green") + click.style(":" ,fg = "blue") + click.style( field.description +"\n", fg = "magenta"))
            click.echo(click.style("Manipulate fields:\n", fg = "blue"))
            click.echo(click.style("[1]", fg = "green") + click.style(": Display field\n", fg = "blue"))
            click.echo(click.style("[2]", fg= "green") + click.style(": Rename field\n", fg= "blue"))
            click.echo(click.style("[3]", fg= "green") + click.style(": Edit field description\n", fg="blue"))
            click.echo(click.style("[4]", fg = "green")+ click.style(": Field merger\n", fg = "blue"))
            click.echo(click.style("[5]", fg="green") + click.style(": Encode field\n", fg="blue"))
            click.echo(click.style("[6]", fg="green") + click.style(": Split fields\n", fg="blue"))
            click.echo(click.style("[B]", fg= "green") + click.style(": Back to above menu\n", fg= "blue"))
        else:
            click.echo(click.style("Manipulate fields:\n", fg="blue"))
            click.echo(click.style("[1]", fg="green") + click.style(": Display fields\n", fg="blue"))
            click.echo(click.style("[2]", fg="green") + click.style(": Encode fields\n", fg="blue"))
            click.echo(click.style("[B]", fg="green") + click.style(": Back to above menu\n", fg="blue"))
    else:
        click.echo(click.style("Manipulate fields:\n", fg="blue"))
        click.echo(click.style("[1]", fg="green") + click.style(": Rename fields\n", fg="blue"))
        click.echo(click.style("[2]", fg="green") + click.style(": Edit field description\n", fg="blue"))
        click.echo(click.style("[3]", fg="green") + click.style(": Encode fields\n", fg="blue"))
        click.echo(click.style("[4]", fg="green") + click.style(": Split fields\n", fg="blue"))
        click.echo(click.style("[B]", fg="green") + click.style(": Back to above menu\n", fg="blue"))
    print("\n")
    selector = input("PLEASE SELECT A MENU CHOICE >>>  ")
    print("\n")
    field_manipulate_menu_choice(selector,field_selector,fields,symbols,symbol_selector)

def field_manipulate_menu_choice(selector,field_selector,fields,symbols,symbol_selector):
    if symbol_selector != "*":
        if field_selector != "*":
            if (selector == "1"):
                click.echo(click.style("DISPLAY FIELD\n", fg= "yellow"))
                display_field(fields,field_selector,symbols,symbol_selector)
            elif (selector == "2"):
                click.echo(click.style("RENAME FIELD\n", fg= "yellow"))
                rename_field(fields, field_selector, symbols, symbol_selector)
            elif (selector == "3"):
                click.echo(click.style("EDIT FIELD DESCRIPTION\n", fg= "yellow"))
                edit_field_description(fields, field_selector, symbols, symbol_selector)
            elif (selector == "4"):
                click.echo(click.style("FIELD MERGER\n", fg= "yellow"))
                field_merger(fields,field_selector,symbols,symbol_selector)
            elif (selector == "5"):
                click.echo(click.style("ENCODING MENU\n", fg="yellow"))
                encoding_menu(fields, field_selector,symbols)
            elif (selector == "6"):
                click.echo(click.style("FIELD SPLIT MENU\n", fg="yellow"))
                split_menu(field_selector,fields,parent=symbols)
                manipulate_menu(symbols)
            elif (selector == "B"):
                click.echo(click.style("BACK TO MANIPULATE MENU\n", fg= "yellow"))
                manipulate_menu(symbols)
            else:
                click.echo(click.style("[ERROR] :", fg="red") + click.style("WRONG SELECTION\n", fg="yellow"))
                field_manipulate_menu(symbols,symbol_selector)
        else:
            if (selector == "1"):
                click.echo(click.style("DISPLAY FIELD\n", fg="yellow"))
                display_field(fields, field_selector, symbols, symbol_selector)
            elif (selector == "2"):
                click.echo(click.style("ENCODING MENU\n", fg="yellow"))
                encoding_menu(fields, field_selector,symbols)
            elif (selector == "B"):
                click.echo(click.style("BACK TO MANIPULATE MENU\n", fg= "yellow"))
                manipulate_menu(symbols)
            else:
                click.echo(click.style("[ERROR] :",fg="red")+ click.style("WRONG SELECTION\n", fg= "yellow"))
                field_manipulate_menu(symbols,symbol_selector)
    else:
        if (selector == "1"):
            click.echo(click.style("RENAME FIELD\n", fg="yellow"))
            rename_field(fields, field_selector, symbols, symbol_selector)
        elif (selector == "2"):
            click.echo(click.style("EDIT FIELD DESCRIPTION\n", fg="yellow"))
            edit_field_description(fields, field_selector, symbols, symbol_selector)
        elif (selector == "3"):
            click.echo(click.style("ENCODING MENU\n", fg="yellow"))
            encoding_menu(fields, field_selector,symbols)
        elif (selector == "4"):
            click.echo(click.style("FIELD SPLIT MENU\n", fg="yellow"))
            split_menu(symbol_selector,symbols,field_selector)
            manipulate_menu(symbols)
        elif (selector == "B"):
            click.echo(click.style("BACK TO MANIPULATE MENU\n", fg="yellow"))
            manipulate_menu(symbols)
        else:
            click.echo(click.style("[ERROR] :", fg="red") + click.style("WRONG SELECTION\n", fg="yellow"))
            field_manipulate_menu(symbols, symbol_selector)

def display_field(fields,field_selector,symbol,symbol_selector):
    old_stdout = sys.stdout
    sys.stdout = tempstdout = io.StringIO()
    if field_selector != "*":
        field = symbolselector.selectsymbol(fields, field_selector)
        print(field)
    else:
        for field in fields:
            print(field)
    sys.stdout = old_stdout
    click.echo_via_pager(tempstdout.getvalue())
    tkinter_window(tempstdout.getvalue())
    field_manipulate_menu(symbol, symbol_selector)

def rename_field(fields,field_selector,symbols,symbol_selector):
    print("\n")
    click.echo(click.style(field_selector, fg= "red") + click.style(" selected!\n", fg= "blue"))
    print("\n")
    new_name = input("PLEASE INPUT A NEW NAME >>>   ")
    print("\n")
    if symbol_selector != "*":
        field = symbolselector.selectsymbol(fields, field_selector)
        field.name = new_name
        click.echo(click.style(new_name, fg= "red") + click.style(" was saved!\n", fg= "blue"))
    else:
        for symbol in symbols:
            symbol.fields[int(field_selector)].name = new_name
    field_manipulate_menu(symbols, symbol_selector)

def edit_field_description(fields,field_selector,symbols,symbol_selector):
    print("\n")
    click.echo(click.style(field_selector, fg= "red") + click.style(" selected!\n", fg= "blue"))
    print("\n")
    if symbol_selector != "*":
        field = symbolselector.selectsymbol(fields, field_selector)
        click.echo(click.style("[Current symbol description]", fg= "green") + click.style(":", fg= "blue") + click.style(field.description + "\n", fg= "magenta"))
        print("\n")
    new_description = input("PLEASE INPUT A NEW DESCRIPTION >>>   ")
    print("\n")
    if symbol_selector != "*":
        field = symbolselector.selectsymbol(fields, field_selector)
        field.description = new_description
        click.echo(click.style(new_description, fg= "red") + click.style(" was saved!\n", fg= "blue"))
    else:
        for symbol in symbols:
            symbol.fields[int(field_selector)].name = new_description
    field_manipulate_menu(symbols, symbol_selector)

def field_merger(fields,field_selector,symbols,symbol_selector):
    field1 = symbolselector.selectsymbol(fields, field_selector)
    print("\n")
    click.echo(click.style(field_selector, fg="red") + click.style(" selected!\n", fg="blue"))
    print("\n")
    display_available_fields_only(fields,ommit= field1)
    field_merge_2 = input("PLEASE SELECT SECOND FIELD TO MERGE WITH >>> ")
    print("\n")
    #field1 = symbolselector.selectsymbol(fields, field_merge_1.name)
    field2 = symbolselector.selectsymbol(fields, field_merge_2)
    field_name = field1.name
    Format.mergeFields(field1,field2)
    field = symbolselector.selectsymbol(symbolselector.selectsymbol(symbols, symbol_selector).fields, "Merge")
    field.name = field_name
    field_manipulate_menu(symbols, symbol_selector)
