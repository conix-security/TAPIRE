from menus.mainmenu import main_menu

from netzob.all import *

def wireshark_exporter_menu(symbols):
    dest_file = input(" PLEASE SPECIFY DESTINATION FILE PATH ( .lua extension) >>>   ")
    port = input(" PLEASE SPECIFY SERVER PORT >>>   ")
    port = int(port)
    while True:
        print('\033[92m' + " [0]  " + '\033[0m' + '\033[94m' + "TCP Protocol" + '\033[0m' +'\n')
        print('\033[92m' + " [1]  " + '\033[0m' + '\033[94m' + "UDP Protocol" + '\033[0m' +'\n')
        select = input(" PLEASE SELECT EITHER >>>   ")

        if int(select) == 0:
            TCP = True
            break
        elif int(select) == 1:
            TCP = False
            break
    wireshark_exporter(symbols,dest_file,port,TCP)

def wireshark_exporter(symbols,dest_file,port,TCP):
    exporter  = WiresharkExporter()
    exporter.export_to_wireshark(symbols,dest_file,port,TCP)
    main_menu(symbols)