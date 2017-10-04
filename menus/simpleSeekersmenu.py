import click

from menus.manipulatemenu import manipulate_menu
from seekers.simpleSeeker.all import *

def simpleSeeker_menu(symbol_selector,symbols):

    print('\033[34m' + "Available relation seekers:" + '\033[0m' + '\n')
    print('\033[32m' + "[1]  " + '\033[0m' + '\033[34m' + "[Print entropy of all fields]" + '\033[0m' + '\n')
    print('\033[32m' + "[2]  " + '\033[0m' + '\033[34m' + "[Print basic data relation between fields]" + '\033[0m' + '\n')
    print('\033[32m' + "[3]  " + '\033[0m' + '\033[34m' + "[Run through hash identifyer]" + '\033[0m' + '\n')
    print('\033[32m' + "[B]  " + '\033[0m' + '\033[34m' + "[Go back to previous menu]" + '\033[0m' + '\n')


    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    simpleSeeker_menu_choice(seeker_selector, symbols, symbol_selector)

def simpleSeeker_menu_choice(seeker_selector,symbols,symbol_selector):

    if (seeker_selector == "1"):
        click.echo(click.style("ANALYSE ENTROPY\n", fg="yellow"))
        entropyfinder_menu(symbol_selector, symbols)
    elif (seeker_selector == "2"):
        click.echo(click.style("RELATION FINDER\n", fg="yellow"))
        relationfinder_menu(symbol_selector, symbols)
    elif (seeker_selector == "3"):
        click.echo(click.style("RUN HASH IDENTIFYER\n", fg="yellow"))
        identifyHash(symbol_selector,symbols)
    elif (seeker_selector == "B"):
        click.echo(click.style("BACK TO PREVIOUS MENU\n", fg="yellow"))
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        simpleSeeker_menu(symbol_selector,symbols)