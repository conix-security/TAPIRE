#!/usr/bin/env python3.5
import logging
import sys
import click
import argparse

import utilitaries.globalvars
from menus.mainmenu import main_menu



def usage():
    click.echo("\n")
    click.echo(click.style("Usage:\n\n", fg="blue") + click.style(sys.argv[0], fg = "red") + click.style(" < pcap File 1 > ", fg = "red") + click.style("< pcap File 2 >",fg ="red")
               + click.style("< Optional : saved project >\n\n", fg = "magenta")
               + click.style("Runs TAPIRE on two pcap files \n", fg = "yellow"))

    exit(1)

def get_args():
    parser = argparse.ArgumentParser(description="Tool for Assisting Protocol Inference and Reverse Engineering")
    group1 = parser.add_mutually_exclusive_group(required=True)
    group2 = parser.add_mutually_exclusive_group()
    group3 = parser.add_mutually_exclusive_group()
    group4 = parser.add_mutually_exclusive_group()
    group1.add_argument("-a", "-analyse", help="Analyses the provided pcaps (minimum 2)", nargs='+',default=None)
    group1.add_argument("-l","-load", help="Loads the provided project")
    group2.add_argument("-n","--network", help="Network mode for pcap(ng) analysis", action="store_true", default=False)
    group3.add_argument("-g","--gui", help="Activates GUI display", action="store_true", default=False)
    group4.add_argument("-v", "--verbose", help="Activates logging messages (Critical, Error, Warning, Info, Debug)", choices=['C','E','W','I','D'])
    parser.add_argument('--version', action='version', version='%(prog)s Version 0.5')
    args = parser.parse_args()

    #SET GUI
    if args.gui:
        utilitaries.globalvars.GUI = args.gui
    #SET NETWORKING
    if args.network:
        utilitaries.globalvars.NETWORK = args.network
    if args.verbose is not None:
        if args.verbose == "D":
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        elif args.verbose == "C":
            logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)
        elif args.verbose == "E":
            logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
        elif args.verbose == "W":
            logging.basicConfig(stream=sys.stdout, level=logging.WARNING)
        elif args.verbose == "I":
            logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    if args.a is not None and len(args.a) < 2:
        parser.error("Analyse mode needs at least two pcap files!")
    return args


def main():
    args = get_args()
    #if len(sys.argv) < 2:
    #    usage()
        #print('toto')
    main_menu(args=args)

if __name__ == '__main__':
    main()
