import click

from menus.manipulatemenu import manipulate_menu
from seekers.all import *

def dataSeeker_menu(symbol_selector,symbols):

    click.echo(click.style("Available relation seekers:\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[Print entropy of all fields]", fg = "blue") + click.style("(Recommended first)", fg = "magenta") + '\n')
    click.echo(click.style("[2] ", fg = "green") + click.style("[Seek for an IP field]", fg = "blue") + '\n')
    click.echo(click.style("[3] ", fg = "green") + click.style("[Seek for CRC32 relation]", fg = "blue") + '\n')
    click.echo(click.style("[4] ", fg = "green") + click.style("[Separate header fields and data fields]", fg = "blue") + '\n')
    click.echo(click.style("[5] ", fg="green") + click.style("[Seek a size relation between two fields]", fg="blue") + '\n')
    print('\033[92m' + " [6]  " + '\033[0m' + '\033[94m' + "[Run through hash identifyer]" + '\033[0m' + '\n')
    print('\033[92m' + " [B]  " + '\033[0m' + '\033[94m' + "[Go back to previous menu]" + '\033[0m' + '\n')


    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    dataSeeker_menu_choice(seeker_selector, symbols, symbol_selector)

def dataSeeker_menu_choice(seeker_selector,symbols,symbol_selector):

    if (seeker_selector == "1"):
        click.echo(click.style("ANALYSE ENTROPY\n", fg="yellow"))
        entropyfinder_menu(symbol_selector, symbols)
    elif (seeker_selector == "2"):
        click.echo(click.style("SEARCH FOR IPS\n", fg="yellow"))
        metaseeker_menu(symbol_selector, symbols)
    elif (seeker_selector == "3"):
        click.echo(click.style("SEARCH FOR CRC32\n", fg="yellow"))
        crcSeeker_menu(symbol_selector, symbols)
    elif (seeker_selector == "4"):
        click.echo(click.style("SEARCH FOR HEADER AND DATA FIELDS\n", fg="yellow"))
        headerSeeker_menu(symbols)
    elif (seeker_selector == "5"):
        click.echo(click.style("SEARCH FOR SIZE\n", fg="yellow"))
        sizeSeeker_menu(symbol_selector,symbols)
    elif (seeker_selector == "7"):
        click.echo(click.style("RUN HASH IDENTIFYER\n", fg="yellow"))
        identifyHash(symbol_selector,symbols)
    elif (seeker_selector == "B"):
        click.echo(click.style("BACK TO PREVIOUS MENU\n", fg="yellow"))
        manipulate_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        dataSeeker_menu(symbol_selector,symbols)