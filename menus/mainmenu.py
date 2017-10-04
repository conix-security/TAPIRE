import pickle

import IPython
import click
from netzob.all import *
import utilities.globalvars

def main_menu(symbols=None,args=None):

    if(symbols is None and args.l is not None):
        with open(args.l, 'rb') as file:
            symbol_dict = pickle.load(file)
            symbols = symbol_dict['Symbol']
            utilities.globalvars.PCAPFiles = symbol_dict['messages']
    elif symbols is None and args.a is not None :
            messages = []
            if utilities.globalvars.NETWORK:
                for argument in args.a:
                    messages += PCAPImporter.readFile(argument).values()
                    utilities.globalvars.PCAPFiles += [argument]
            else:
                for argument in args.a:
                    messages += FileImporter.readFile(argument,delimitor=b'').values()
                    utilities.globalvars.PCAPFiles += [argument]
            symbols = [Symbol(name='symbol_0',messages=messages)]
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
    click.echo(click.style("[5]", fg="green") + click.style(": Export project parser\n", fg="blue"))
    click.echo(click.style("[6]", fg="green") + click.style(": Dynamic analysis\n", fg="blue"))
    click.echo(click.style("[E]", fg="green") + click.style(": Exit and close Tapire\n", fg="blue"))
    selector = input(" PLEASE INPUT SELECTION >>>  ")
    main_menu_choice(selector,symbols)

def main_menu_choice(selector,symbols):

    if (selector == "1"):
        click.echo(click.style("DISPLAY PCAP\n", fg="yellow"))
        pcap_exchange_menu(symbols)
    elif (selector == "2"):
        click.echo(click.style("MANIPULATE MENU\n", fg="yellow"))
        manipulate_menu(symbols)
    elif(selector == "3"):
        click.echo(click.style("SAVE\n", fg="yellow"))
        save_object(symbols)
    elif(selector == "4"):
        click.echo(click.style("IPYTHON SHELL",fg="yellow"))
        IPython.embed()
        main_menu(symbols)
    elif (selector == "5"):
        click.echo(click.style("EXPORT MENU", fg="yellow"))
        exporter_menu(symbols)
    elif (selector == "6"):
        click.echo(click.style("Dynamic Analysis MENU", fg="yellow"))
        dynamic_sequence_menu(symbols)
    elif (selector == "E"):
        click.echo(click.style("Bye! Thanks for using TAPIRE, feedback welcome! :)", fg="yellow"))
        exit()
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        main_menu(symbols)

def save_object(obj):
    filename = input("PLEASE SELECT PROJECT NAME >>>")
    if utilities.globalvars.PCAPFiles:
        symbol_dict = {
            'Symbol': obj,
            'messages': utilities.globalvars.PCAPFiles
        }
    with open("./projects/"+filename, 'wb') as output:
        pickle.dump(symbol_dict, output, pickle.HIGHEST_PROTOCOL)
    main_menu(obj)


#IMPORTS AT BOTTOM BECAUSE TEMPORARY FIX TO CIRCULAR DEPENDENCY http://effbot.org/zone/import-confusion.htm

from menus.manipulatemenu import manipulate_menu
from menus.pcapdisplaymenu import pcap_exchange_menu
from menus.exportermenu import exporter_menu
from menus.DynamicSequenceMenu import dynamic_sequence_menu