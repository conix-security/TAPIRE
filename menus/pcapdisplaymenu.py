import io

import click
from netzob.all import *
from scapy.all import *

import utilitaries.globalvars
from menus.mainmenu import main_menu
from utilitaries.window import tkinter_window

def pcap_exchange_menu(symbols):

    click.echo(click.style("Display pcap exchange :\n", fg="blue"))
    click.echo(click.style("[1]", fg = "green") + click.style(": Display as raw\n", fg = "blue"))
    click.echo(click.style("[2]", fg = "green") + click.style(": Display as utf-8 decoded\n", fg = "blue"))
    click.echo(click.style("[3]", fg = "green")+  click.style(": Display as ISO-SOMETHING decoded\n", fg = "blue"))
    click.echo(click.style("[4]", fg = "green")+  click.style(": Display as ASCII decoded\n", fg = "blue"))
    click.echo(click.style("[B]", fg="green") + click.style(": Go Back to main menu\n", fg="blue"))
    selector = input(" >>>  ")
    pcap_exchange_menu_choice(selector,symbols)

def pcap_exchange_menu_choice(selector,symbols):

    if (selector == "1"):
        click.echo(click.style("DISPLAY AS RAW\n", fg="yellow"))
        display_raw_pcap(symbols)
    elif (selector == "2"):
        click.echo(click.style("DISPLAY AS ISO-8859-1\n", fg="yellow"))
        display_utf8_pcap(symbols)
    #elif (selector == "3"):
    #    click.echo(click.style("DISPLAY AS ISO\n", fg="yellow"))
    #elif (selector == "4"):
    #    click.echo(click.style("DISPLAY AS ASCII\n", fg="yellow"))
    elif (selector == "B"):
        main_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        pcap_exchange_menu(symbols)

def display_raw_pcap(symbols):

    pcap_list = []
    for PCAPFile in utilitaries.globalvars.PCAPFiles:
        pcap_list.append(rdpcap(PCAPFile))
    tempstdout_list = []
    for i, pcap in enumerate(pcap_list):
        old_stdout = sys.stdout
        tempstdout_list.append(io.StringIO())
        sys.stdout = tempstdout_list[i]
        pcap.hexdump()
        sys.stdout = old_stdout
    buffer = ""
    for i, tempstdout in enumerate(tempstdout_list):
        buffer += "<----------------------------------------PCAP "+ str(i)+" :-------------------------------------->\n" + tempstdout.getvalue() + "\n"
    # Print buffer in a pager
    click.echo_via_pager(buffer)
    # Print buffer in tkinter window
    tkinter_window(buffer)
    pcap_exchange_menu(symbols)

def display_utf8_pcap(symbols):

    pcap_list = []
    for PCAPFile in utilitaries.globalvars.PCAPFiles:
        pcap_list.append(rdpcap(PCAPFile))
    tempstdout_list = []
    for i, pcap in enumerate(pcap_list):
        old_stdout = sys.stdout
        tempstdout_list.append(io.StringIO())
        sys.stdout = tempstdout_list[i]
        for j in pcap:
            print(j)
        sys.stdout = old_stdout
    buffer = ""
    for i, tempstdout in enumerate(tempstdout_list):
        buffer += "<----------------------------------------PCAP "+ str(i)+" :-------------------------------------->\n" + tempstdout.getvalue() + "\n"
    # Print buffer in a pager
    click.echo_via_pager(buffer)
    # Print buffer in tkinter window
    tkinter_window(buffer)
    pcap_exchange_menu(symbols)