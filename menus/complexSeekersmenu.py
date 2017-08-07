import click

from menus.manipulatemenu import manipulate_menu
from seekers.complexSeeker.all import *

def complexSeeker_menu(symbol_selector,symbols):


    print('\033[34m' + "Available relation seekers:" + '\033[0m' + '\n')
    print('\033[32m' + "[1]  " + '\033[0m' + '\033[34m' + "[Seek for an IP field]" + '\033[0m' + '\n')
    print('\033[32m' + "[2]  " + '\033[0m' + '\033[34m' + "[Seek for CRC32 relation]" + '\033[0m' + '\n')
    print('\033[32m' + "[3]  " + '\033[0m' + '\033[34m' + "[Separate header fields and data fields]" + '\033[0m' + '\n')
    print('\033[32m' + "[4]  " + '\033[0m' + '\033[34m' + "[Seek a size relation between two fields]" + '\033[0m' + '\n')
    print('\033[32m' + "[B]  " + '\033[0m' + '\033[34m' + "[Go back to previous menu]" + '\033[0m' + '\n')

    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    complexSeeker_menu_choice(seeker_selector, symbols, symbol_selector)

def complexSeeker_menu_choice(seeker_selector,symbols,symbol_selector):

    if (seeker_selector == "1"):
        click.echo(click.style("SEARCH FOR IPS\n", fg="yellow"))
        metaseeker_menu(symbol_selector, symbols)
    elif (seeker_selector == "2"):
        click.echo(click.style("SEARCH FOR CRC32\n", fg="yellow"))
        crcSeeker_menu(symbol_selector, symbols)
    elif (seeker_selector == "3"):
        click.echo(click.style("SEARCH FOR HEADER AND DATA FIELDS\n", fg="yellow"))
        headerSeeker_menu(symbols)
    elif (seeker_selector == "4"):
        click.echo(click.style("SEARCH FOR SIZE\n", fg="yellow"))
        sizeSeeker_menu(symbol_selector,symbols)
    elif (seeker_selector == "B"):
        click.echo(click.style("BACK TO PREVIOUS MENU\n", fg="yellow"))
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        complexSeeker_menu(symbol_selector,symbols)