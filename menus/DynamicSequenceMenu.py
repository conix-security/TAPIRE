import copy

from netzob.all import *

from menus.mainmenu import main_menu

from utilitaries import symbolselector
from utilitaries import converter

def dynamic_sequence_menu(symbols):

    symbol_sequence = []
    session_messages = []
    received_messages = []
    print('\033[34m' + "Please select symbols to create a symbol sequence:" + '\033[0m' + '\n')
    #Select symbols to be part of Session
    while True:
        print('\033[34m' + "Your sequence is:" + '\033[0m' + '\n')
        print('\033[31m' + str(symbol_sequence) + '\033[0m' + '\n')
        print('\033[34m' + "Available symbols:" + '\033[0m' + '\n')
        print('\033[31m' + str(symbols) + '\033[0m' + '\n')
        print('\033[34m' + "Press \"D\" when done" + '\033[0m' + '\n')

        selector = input(" >>>  ")
        if selector == "D" or selector == "d":
            break
        else:
            #Copy symbol and insert in the sequence
            passed_symbol = symbolselector.selectsymbol(symbols,selector)
            if passed_symbol is not None:
                symbol_sequence.append(copy.deepcopy(passed_symbol))
    #Select messages to be part of session
    print('\033[34m' + "Please select messages to be part of a message sequence:" + '\033[0m' + '\n')
    for sym in symbol_sequence:
        print('\033[34m' + sym.name + '\033[0m' + '\n')
        #Display messages in symbol
        for index,mess in enumerate(sym.messages):
            print('\033[32m' + "[" + str(index) + "]" + '\033[0m' + '\n')
            print(mess)
            print('\n')
        while True:
            selector = input(" >>> ")
            try:
                session_messages.append(sym.messages[int(selector)])
                break
            except:
                print('\033[31m' + 'Error:' +'\033[0m' + '\033[34m' + 'Wrong choice, please try again' + '\033[0m' + '\n')
                continue
    #Allow message modification:
    print('\033[34m' + "Would you like to modify a message?" + '\033[0m' + '\n')
    print('\033[32m' + '[Y]' + '\033[0m' + '\033[34m' + 'es or ' + '\033[0m'+ '\033[32m' + '[N]' + '\033[0m' + '\033[34m' + 'o' + '\033[0m' +'\n')
    while True:
        selector = input(" >>> ")
        if selector == 'Y' or selector == 'y' or selector == 'n' or selector == 'N':
            break
    if selector == 'Y' or selector == 'y':
        handle_modify_message(session_messages)
    while True:
        print('\033[34m' + "Please input destination IP" + '\033[0m' + '\n')
        dest_ip = input(' >>> ')
        print('\n')
        print('\033[34m' + "Please input destination Port" + '\033[0m' + '\n')
        print('\n')
        dest_port = int(input(' >>> '))
        print('\033[34m' + "Please specify " + '\033[0m' + '\033[32m' + '[TCP]' + '\033[0m' + ' or ' + '\033[32m' + '[UDP]' + '\033[0m' + '\n')
        protocol = input(' >>> ')
        if protocol == "UDP" or protocol == "Udp" or protocol == "udp":
            try:
                client = UDPClient(remoteIP=dest_ip, remotePort=dest_port)
                client.open()
                break
            except:
                print('\033[31m' + 'Error:' +'\033[0m' + '\033[34m' + 'Wrong choice, please try again' + '\033[0m' + '\n')
                continue
        elif protocol == "TCP" or protocol == "Tcp" or protocol == "tcp":
            try:
                client = TCPClient(remoteIP=dest_ip, remotePort=dest_port)
                client.open()
                break
            except:
                print('\033[31m' + 'Error:' +'\033[0m' + '\033[34m' + 'Wrong choice, please try again' + '\033[0m' + '\n')
                continue
        else:
            print('\033[31m' + 'Error:' + '\033[0m' + '\033[34m' + 'Wrong choice, please try again' + '\033[0m' + '\n')
            continue
    for index,mess in enumerate(session_messages):
        print('\033[34m' + symbol_sequence[index].name + '\033[0m' + '\n')
        print('\033[34m' + "Sent:" + '\033[0m' + '\n')
        sent = mess.data
        print(sent)
        print('\n')
        print('\033[34m' + "Received:" + '\033[0m' + '\n')
        received = client.sendReceive(mess.data)
        print(received)
        print('\n')
        received_messages.append(received)
    client.close()
    main_menu(symbols)

def modify_message(message):
    print('\033[34m' + "Old data:" + '\033[0m' + '\n')
    print(message.data)
    print('\n')
    new_data = input('Please specify new Raw data like so: \"\\\\xca\\\\xfe\\\\xba\\\\xbe\" \n >>> ')
    message.data = converter.input_to_raw(new_data)

def handle_modify_message(session_messages):
    while True:
        print('\033[34m' + "Please select a message to modify:" + '\033[0m' + '\n')
        for index, mess in enumerate(session_messages):
            print('\033[32m' + "[" + str(index) + "]" + '\033[0m' + '\n')
            print(mess)
            print('\n')
            print('\033[34m' + "Press D when done" + '\033[0m' + '\n')
            while True:
                try:
                    message_selector = input(" >>> ")
                    if message_selector == "D" or message_selector == "d":
                        return
                    else:
                        modify_message(session_messages[int(message_selector)])
                    break
                except:
                    print('\033[31m' + 'Error:' + '\033[0m' + '\033[34m' + 'Wrong choice, please try again' + '\033[0m' + '\n')
                    continue