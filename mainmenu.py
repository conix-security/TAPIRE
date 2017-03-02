import click
import sys

from netzob.all import *




def main_menu(symbols=None):

    click.echo(click.style("Welcome to scadalyser, please select what you would like to do?", fg = "blue"))
    click.echo(click.style("[1]", fg = "green")+ click.style(": Display pcap exchange\n", fg = "blue"))
    click.echo(click.style("[2]", fg = "green")+ click.style(": Manipulate\n", fg = "blue"))
    selector = input(" >>>  ")
    main_menu_choice(selector,symbols)

def main_menu_choice(selector,symbols):

    if (selector == "1"):
        click.echo(click.style("DISPLAY PCAP\n", fg="yellow"))
        pcap_exchange_menu(symbols)
    elif (selector == "2"):
        click.echo(click.style("MANIPULATE MENU\n", fg="yellow"))
        messages=PCAPImporter.readFile(sys.argv[1]).values() + PCAPImporter.readFile(sys.argv[2]).values()
        if symbols == None:
            manipulate_menu(Symbol(messages=messages))
        else:
            manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        main_menu()

#IMPORTS AT BOTTOM BECAUSE TEMPORARY FIX TO CIRCULAR DEPENDENCY http://effbot.org/zone/import-confusion.htm

from manipulatemenu import manipulate_menu
from pcapdisplaymenu import pcap_exchange_menu