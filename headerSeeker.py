import click
import codecs

from netzob.all import *

from manipulatemenu import manipulate_menu

#TODO Get Debug log output from Netgoblin headerSeeker

def headerSeeker_menu(symbols):

    click.echo(click.style("Available Methods:\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[Ratio based search]", fg = "blue") + '\n')
    click.echo(click.style("[2] ", fg = "green") + click.style("[Separator field based search]", fg = "blue") + '\n')
    click.echo(click.style("[3] ", fg = "green") + click.style("[Separator value based search]", fg = "blue") + '\n')
    seeker_selector = input(" PLEASE SELECT A CHOICE >>>   ")
    headerSeeker_menu_choice(seeker_selector, symbols)

def headerSeeker_menu_choice(seeker_selector, symbols):
    if (seeker_selector == "1"):
        click.echo(click.style("Ratio based search\n", fg="yellow"))
        seek_headers_ratio(symbols)
    elif (seeker_selector == "2"):
        click.echo(click.style("Field separator based search\n", fg="yellow"))
        seek_headers_field_sep(symbols)
    elif (seeker_selector == "3"):
        click.echo(click.style("SEARCH FOR HEADER AND DATA FIELDS\n", fg="yellow"))
        seek_headers_value_sep(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        manipulate_menu(symbols)

def seek_headers_ratio(symbols):
    ratio = 0
    while not 0 < ratio <1:
        ratio = input(" Please input a ratio >>>   ")
        ratio = float(ratio)
        if not 0 < ratio < 1:
            click.echo(click.style("[ERROR] ", fg="red") + click.style("Ratio must be between 0 and 1 (strictly)", fg="blue") + '\n')
    click.echo(click.style("Searching for Headers\n", fg="yellow"))
    seeker = headerDetector(ratio=True,ratioValue=ratio)
    found = seeker.findOnSymbols(symbols)
    if found:
        click.echo(click.style("Renaming headers\n", fg="yellow"))
    else:
        click.echo(click.style("Sorry, didn't find anything!\n", fg="yellow"))
    manipulate_menu(symbols)

def seek_headers_field_sep(symbols):
    click.echo(click.style("[1] ", fg="green") + click.style("[Size relation]", fg="blue") + '\n')
    click.echo(click.style("[2] ", fg="green") + click.style("[CRC32 relation]", fg="blue") + '\n')
    click.echo(click.style("[3] ", fg="green") + click.style("[IPchecksum relation]", fg="blue") + '\n')
    field_separator = input(" Please select a type of field relation for separation between header and data >>>   ")
    if field_separator == "1":
        field_separator = "Size"
    elif field_separator == "2":
        field_separator = "CRC32"
    elif field_separator == "3":
        field_separator = "InternetChecksum"
    else:
        click.echo(click.style("[ERROR] ", fg="red") + click.style("Wrong selection",
                                                                   fg="blue") + '\n')
        headerSeeker_menu(symbols)
    seeker = headerDetector(field=True,fieldType=field_separator)
    found = seeker.findOnSymbols(symbols)
    if found:
        click.echo(click.style("Renaming headers\n", fg="yellow"))
    else:
        click.echo(click.style("Sorry, didn't find anything!\n", fg="yellow"))
    manipulate_menu(symbols)


def seek_headers_value_sep(symbols):
    click.echo(click.style("[1] ", fg="green") + click.style("[Ascii]", fg="blue") + '\n')
    click.echo(click.style("[2] ", fg="green") + click.style("[Raw]", fg="blue") + '\n')
    click.echo(click.style("[3] ", fg="green") + click.style("[HexaString]", fg="blue") + '\n')
    click.echo(click.style("[4] ", fg="green") + click.style("[BitArray]", fg="blue") + '\n')
    click.echo(click.style("[5] ", fg="green") + click.style("[Integer]", fg="blue") + '\n')
    click.echo(click.style("[6] ", fg="green") + click.style("[IPV4]", fg="blue") + '\n')
    click.echo(click.style("[7] ", fg="green") + click.style("[TimeStamp]", fg="blue") + '\n')
    separator = input(" Please select a type of data for the separator between header and data >>>   ")
    if separator == "1":
        separator = "ASCII"
    elif separator == "2":
        separator = "RAW"
    elif separator == "3":
        separator = "Hexadecimal"
    elif separator == "4":
        separator = "BitArray"
    elif separator == "5":
        separator = "Integer"
    elif separator == "6":
        separator = "IPV4"
    elif separator == "7":
        separator = "TimeStamp"
    else:
        click.echo(click.style("[ERROR] ", fg="red") + click.style("Wrong selection",
                                                                   fg="blue") + '\n')
        headerSeeker_menu(symbols)
    value = input("Please specify the value of the separator>>> ")
    if separator == "ASCII":
        field = Field(domain = ASCII(value))
    elif separator == "Raw":
        field = Field(domain=Raw(input_to_raw(value)))
    elif separator == "Hexadecimal":
        pass
    else:
        click.echo(click.style("[ERROR] ", fg="red") + click.style("Wrong selection",
                                                                   fg="blue") + '\n')
        headerSeeker_menu(symbols)
    seeker = headerDetector(separator=True, separatorValue=field)
    found = seeker.findOnSymbols(symbols)
    if found:
        click.echo(click.style("Renaming headers\n", fg="yellow"))
    else:
        click.echo(click.style("Sorry, didn't find anything!\n", fg="yellow"))
    manipulate_menu(symbols)
    pass

def input_to_raw(string):
    string = codecs.decode(string, "unicode_escape")
    return string.encode('ISO-8859-1')