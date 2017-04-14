import pickle
import sys

import IPython
import click
from netzob.all import *


def main_menu(symbols=None):

    if(symbols is None and len(sys.argv) >= 4):
        with open(sys.argv[3], 'rb') as file:
            symbols = pickle.load(file)
    click.echo(click.style(
               """" \n\n\n
                        _,.,.__,--.__,-----.
                      ,""   '))              `.
                    ,'   e                    ))
                   (  .='__,                  ,
                    `~`     `-\  /._____,/   /
                             | | )    (  (   ;
                             | | |    / / / /
                     vvVVvvVvVVVvvVVVvvVVvVvvvVvPhSv

    """,fg="magenta") + '\n')
    click.echo(click.style("Welcome to TAPIRE, please select a menu option\n", fg = "yellow"))
    click.echo(click.style("[1]", fg = "green")+ click.style(": Display pcap exchange\n", fg = "blue"))
    click.echo(click.style("[2]", fg = "green")+ click.style(": Manipulate\n", fg = "blue"))
    click.echo(click.style("[3]", fg = "green")+ click.style(": Save project\n", fg = "blue"))
    click.echo(click.style("[4]", fg = "green")+ click.style(": Open IPython shell\n",fg = "blue"))
    selector = input(" PLEASE INPUT SELECTION >>>  ")
    main_menu_choice(selector,symbols)

def main_menu_choice(selector,symbols):

    if (selector == "1"):
        click.echo(click.style("DISPLAY PCAP\n", fg="yellow"))
        pcap_exchange_menu(symbols)
    elif (selector == "2"):
        click.echo(click.style("MANIPULATE MENU\n", fg="yellow"))
        if symbols == None:
            messages = PCAPImporter.readFile(sys.argv[1]).values() + PCAPImporter.readFile(sys.argv[2]).values()
            manipulate_menu([Symbol(name='symbol_0',messages=messages)])
        else:
            manipulate_menu(symbols)
    elif(selector == "3"):
        click.echo(click.style("SAVE\n", fg="yellow"))
        save_object(symbols)
    elif(selector == "4"):
        click.echo(click.style("IPYTHON SHELL",fg="yellow"))
        IPython.embed()
        main_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        main_menu(symbols)

def save_object(obj):
    filename = input("PLEASE SELECT PROJECT NAME >>>")
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    main_menu(obj)

#IMPORTS AT BOTTOM BECAUSE TEMPORARY FIX TO CIRCULAR DEPENDENCY http://effbot.org/zone/import-confusion.htm

from menus.manipulatemenu import manipulate_menu
from menus.pcapdisplaymenu import pcap_exchange_menu