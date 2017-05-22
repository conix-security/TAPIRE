import io

import click
from netzob.all import *
from scapy.all import *
from collections import OrderedDict

import utilitaries.globalvars
from menus.mainmenu import main_menu
from utilitaries.window import tkinter_window

def pcap_exchange_menu(symbols):

    click.echo(click.style("Display pcap exchange :\n", fg="blue"))
    click.echo(click.style("[1]", fg = "green") + click.style(": Display as raw\n", fg = "blue"))
    click.echo(click.style("[2]", fg = "green") + click.style(": Display as utf-8 decoded\n", fg = "blue"))
    click.echo(click.style("[3]", fg = "green")+  click.style(": Display with fields\n", fg = "blue"))
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
    elif (selector == "3"):
        click.echo(click.style("DISPLAY WITH FIELDS\n", fg="yellow"))
        display_messages_with_fields(symbols)
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
        pcap_list.append(PCAPImporter.readFile(PCAPFile).values())
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

def display_messages_with_fields(symbols):
    old_stdout = sys.stdout
    sys.stdout = tempstdout = io.StringIO()
    #List all sessions
    sessions = []
    splitMessageList = OrderedDict()
    for sym in symbols:
        for message in sym.messages:
            sessions.append(message.session)
    sessions = set(sessions)
    for session in sessions:
        click.echo(click.style(session.name, fg="red"))
        message_list = []
        for symbol in symbols:
            for message in symbol.messages:
                if message.session.id == session.id:
                    #Append the message to our message list
                    message_list.append(message)
            splitMessageList.update(symbol.getMessageCells())
        message_list.sort(key=lambda mess: mess.date)
        for message in message_list:
            for i,element in enumerate(splitMessageList[message]):
                print(" | ", end = " ")
                if i <= 2:
                    print('\033[92m' + " " + element + " " + '\033[0m',end = " ")
                else:
                    print(element, end = " ")
            print("\n")
    sys.stdout = old_stdout
    click.echo_via_pager(tempstdout.getvalue())
    tkinter_window(tempstdout.getvalue())
    pcap_exchange_menu(symbols)
