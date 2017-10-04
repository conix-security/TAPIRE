import re

from menus.mainmenu import main_menu

from netzob.all import *

def kaitai_exporter_menu(symbols):
    rule = re.compile(r'^[a-z][a-z0-9_]*$')
    while True:
        meta_name = input(" PLEASE SPECIFY PARSER NAME >>>   ")
        extension = input(" PLEASE SPECIFY FILE EXTENSION >>>   ")

        if rule.match(meta_name) and rule.match(extension):
            break
        else:
            print('\033[91m' + " Error:  " + '\033[0m' + '\033[91m' + "Inputs must match ^[a-z][a-z0-9_]*$ " + '\033[0m' +'\n')
    kaitai_export(meta_name,extension,symbols)

def kaitai_export(meta_name,extension,symbols):
    exporter  = KaitaiExporter()
    exporter.export_to_kaitai(meta_name,extension,symbols)
    print("Export done!\n")
    main_menu(symbols)