import click
import io

from netzob.all import *
from scapy.all import *

from mainmenu import main_menu

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
        click.echo(click.style("DISPLAY AS UTF-8\n", fg="yellow"))
        display_utf8_pcap(symbols)
    elif (selector == "3"):
        click.echo(click.style("DISPLAY AS ISO\n", fg="yellow"))
    elif (selector == "4"):
        click.echo(click.style("DISPLAY AS ASCII\n", fg="yellow"))
    elif (selector == "B"):
        main_menu(symbols)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        pcap_exchange_menu(symbols)

def display_raw_pcap(symbols):

    pcapFile1 = sys.argv[1]
    pcap1 = rdpcap(pcapFile1)
    pcapFile2 = sys.argv[2]
    pcap2 = rdpcap(pcapFile2)
    #Retrieve hexdump from scapy print function and redirect it to a buffer
    old_stdout = sys.stdout
    sys.stdout = tempstdout1 = io.StringIO()
    pcap1.hexdump()
    sys.stdout=old_stdout
    sys.stdout = tempstdout2 = io.StringIO()
    pcap2.hexdump()
    sys.stdout = old_stdout
    #Print buffer in a pager
    click.echo_via_pager(click.style("<----------------------------------------PCAP 1:-------------------------------------->\n", fg = "red") + "\n" + tempstdout1.getvalue() +"\n" + click.style("<----------------------------------------PCAP 2:-------------------------------------->\n", fg = "red") +"\n" + tempstdout2.getvalue())
    pcap_exchange_menu(symbols)

def display_utf8_pcap(symbols):

    pcapFile1 = sys.argv[1]
    pcapFile2 = sys.argv[2]
    pcap1 = PCAPImporter.readFile(pcapFile1).values()
    pcap2 = PCAPImporter.readFile(pcapFile2).values()
    old_stdout = sys.stdout
    sys.stdout = buffer1 = io.StringIO()
    for i in pcap1:
        print(i)
    sys.stdout = old_stdout
    sys.stdout = buffer2 = io.StringIO()
    for j in pcap2:
        print(j)
    sys.stdout = old_stdout
    click.echo_via_pager(click.style("<----------------------------------------PCAP 1:-------------------------------------->\n", fg = "red") + "\n"+ buffer1.getvalue() + "\n" + click.style("<----------------------------------------PCAP 2:-------------------------------------->\n", fg = "red") + "\n" + buffer2.getvalue())
    pcap_exchange_menu(symbols)
