#!/usr/bin/env python3.5
#import logging
import sys

import click

#PROJECT FILES
from mainmenu import main_menu

#logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)

def usage():
    click.echo("\n")
    click.echo(click.style("Usage:\n\n", fg="blue") + click.style(sys.argv[0], fg = "red") + click.style(" < pcap File 1 > ", fg = "red") + click.style("< pcap File 2 >",fg ="red")
               + click.style("< Optional : saved project >\n\n", fg = "magenta")
               + click.style("Runs TAPIRE on two pcap files \n", fg = "yellow"))

    exit(1)

def main():

    if len(sys.argv) < 3:
        usage()
    main_menu()

if __name__ == '__main__':
    main()
