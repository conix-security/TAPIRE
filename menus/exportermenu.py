import click

from exporter.all import *
from menus.mainmenu import main_menu


def exporter_menu(symbols):

    click.echo(click.style("Available relation seekers:\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[Export to wireshark]", fg = "blue") + '\n')
    click.echo(click.style("[2] ", fg = "green") + click.style("[Export to Kaitai]", fg = "blue") + '\n')
    click.echo(click.style("[B] ", fg = "green") + click.style("[Back]", fg = "blue") + '\n')
    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    exporter_menu_choice(seeker_selector,symbols)

def exporter_menu_choice(seeker_selector,symbols):

    if (seeker_selector == "1"):
        click.echo(click.style("EXPORT TO WIRESHARK\n", fg="yellow"))
        wireshark_exporter_menu(symbols)
    elif (seeker_selector == "2"):
        click.echo(click.style("EXPORT TO KAITAI\n", fg="yellow"))
        kaitai_exporter_menu(symbols)
    elif (seeker_selector == "B"):
        click.echo(click.style("BACK TO PREVIOUS MENU\n", fg="yellow"))
        main_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        main_menu(symbols)