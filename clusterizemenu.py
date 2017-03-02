import sys
import click

from netzob.all import *
from netzob.Inference.Vocabulary.FormatOperations.ClusterBySize import ClusterBySize
from netzob.Inference.Vocabulary.FormatOperations.ClusterByAlignment import ClusterByAlignment

from manipulatemenu import manipulate_menu

def clusterize_menu(symbols):

    click.echo(click.style("Clusterize :", fg="blue"))
    if(isinstance(symbols,list)):
        click.echo(click.style("[1]", fg="green") + click.style(": Cluster by alignment\n", fg="blue"))
        click.echo(click.style("[2]", fg="green") + click.style(": Cluster by applicative data\n", fg="blue"))
        click.echo(click.style("[3]", fg="green") + click.style(": Cluster by key field\n", fg="blue"))
        click.echo(click.style("[B]", fg="green") + click.style(": Back to manipulate menu\n", fg="blue"))
        print("\n")
        selector = input("PLEASE SELECT A MENU CHOICE >>>  ")
        print("\n")
        clusterize_menu_choice(selector,symbols)
    else:
        click.echo(click.style("[1]", fg="green") + click.style(": Cluster by size\n", fg="blue"))
        click.echo(click.style("[2]", fg="green") + click.style(": Cluster by alignment\n", fg="blue"))
        click.echo(click.style("[3]", fg="green") + click.style(": Cluster by applicative data\n", fg="blue"))
        click.echo(click.style("[4]", fg="green") + click.style(": Cluster by key field\n", fg="blue"))
        click.echo(click.style("[B]", fg="green") + click.style(": Back to manipulate menu\n", fg="blue"))
        print("\n")
        selector = input("PLEASE SELECT A MENU CHOICE >>>  ")
        print("\n")
        clusterize_menu_choice(selector,symbols)

def clusterize_menu_choice(selector,symbols):

    if(isinstance(symbols,list)):
        if (selector == "1"):
            click.echo(click.style("CLUSTER BY ALIGNMENT\n", fg="yellow"))
        elif (selector == "2"):
            click.echo(click.style("CLUSTER BY APPLICATIVE DATA\n", fg="yellow"))
        elif( selector =="3"):
            click.echo(click.style("CLUSTER BY KEY FIELD\n", fg="yellow"))
        elif(selector == "B"):
            manipulate_menu(symbols)
        else:
            click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
            clusterize_menu(symbols)
    else:
        if (selector == "1" ):
            click.echo(click.style("CLUSTER BY SIZE\n", fg="yellow"))
            clusterize_by_size()
        elif (selector == "2"):
            click.echo(click.style("CLUSTER BY ALIGNMENT\n", fg="yellow"))
            clusterize_by_alignment()
        elif (selector == "3"):
            click.echo(click.style("CLUSTER BY APPLICATIVE DATA\n", fg="yellow"))
        elif( selector =="4"):
            click.echo(click.style("CLUSTER BY KEY FIELD\n", fg="yellow"))
        elif(selector == "B"):
            manipulate_menu(symbols)
        else:
            click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
            clusterize_menu(symbols)


def clusterize_by_size():
    messages = PCAPImporter.readFile(sys.argv[1]).values() + PCAPImporter.readFile(sys.argv[2]).values()
    clusterer = ClusterBySize()
    new_symbols = clusterer.cluster(messages)
    manipulate_menu(new_symbols)

def clusterize_by_alignment():
    messages = PCAPImporter.readFile(sys.argv[1]).values() + PCAPImporter.readFile(sys.argv[2]).values()
    clusterer = ClusterByAlignment()
    new_symbols = clusterer.cluster(messages)
    if isinstance(new_symbols,list):
        if new_symbols[0].name == "Symbol":
            index=0
            for sym in new_symbols:
                sym.name = "Symbol-" + str(index)
                index += 1
    manipulate_menu(new_symbols)