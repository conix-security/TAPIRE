import click
import binascii
import socket
import io
import sys
import collections

from netzob.all import *

import symbolselector

from manipulatemenu import manipulate_menu

def metaseeker_menu(symbol_selector,symbols):

    symbol = symbolselector.selectsymbol(symbols,symbol_selector)
    click.echo(click.style("Available Metadata:\n", fg="blue"))
    click.echo(click.style("[1] ", fg = "green") + click.style("[Address 1]", fg = "cyan") + click.style(" : ",fg = "blue") + click.style(symbol.messages[0].l3DestinationAddress + "\n", fg = "red"))
    click.echo(click.style("[2] ", fg = "green") + click.style("[Address 2]", fg = "cyan") + click.style(" : ",fg = "blue") + click.style(symbol.messages[0].l3SourceAddress + "\n", fg = "red"))
    #click.echo(click.style("[3] ", fg = "green") + click.style("[Port 1]", fg = "cyan") + click.style(" : ",fg = "blue") + click.style(metadata.port1 + "\n", fg = "red"))
    #click.echo(click.style("[4] ", fg = "green") + click.style("[Port 2]", fg = "cyan") + click.style(" : ",fg = "blue") + click.style(metadata.port2 + "\n", fg = "red"))
    seeker_selector = input(" PLEASE SELECT AN ELEMENT TO SEEK >>>   ")
    metaseeker_menu_choice(seeker_selector,symbols,symbol_selector)

def metaseeker_menu_choice(seeker_selector,symbols,symbol_selector):

    if (seeker_selector == "1"):
        ip = symbolselector.selectsymbol(symbols,symbol_selector).messages[0].l3DestinationAddress
        seek_ip(ip,symbols,symbol_selector)
    elif (seeker_selector == "2"):
        ip = symbolselector.selectsymbol(symbols,symbol_selector).messages[0].l3SourceAddress
        seek_ip(ip,symbols,symbol_selector)
    else:
        click.echo(click.style("ERROR : WRONG SELECTION\n", fg="yellow"))
        encoding_menu(symbols, symbol_selector)

def recursive_find(workstring, index_list, hexipstring):
    res_index = workstring.find(hexipstring)
    if res_index == -1:
        # NOTHING FOUND
        return index_list
    else:
        # One match, looking for next match
        # STORE INDEX IN LIST
        if index_list:
            # List not empty, already has and index
            index_list.append(index_list[-1] + res_index)
        else:
            index_list.append(res_index)
        # DIVIDE workstring and apply find again
        workstring = workstring[res_index + len(hexipstring):]
        # Call function again
        return recursive_find(workstring, index_list, hexipstring)

def core_find(message,hexipstring,index_list):
        # Define results structure
        results = collections.namedtuple('Results', ['full_be', 'one_less_be', 'two_less_be', 'full_le', 'one_less_le', 'two_less_le','total_length'])
        results.full_be = recursive_find(message, index_list, hexipstring)
        index_list = []
        results.one_less_be = recursive_find(message, index_list, hexipstring[1:])
        index_list = []
        results.two_less_be = recursive_find(message, index_list, hexipstring[2:])
        index_list = []
        # little endian search
        results.full_le = recursive_find(message, index_list, hexipstring[::-1])
        index_list = []
        results.one_less_le = recursive_find(message, index_list, hexipstring[1:][::-1])
        index_list = []
        results.two_less_le = recursive_find(message, index_list, hexipstring[2:][::-1])
        # Remove results from one byte less searches in two bytes less searches
        for value in results.one_less_be:
            if value + 1 in results.two_less_be :
                results.two_less_be.remove(value + 1)
            if value in results.two_less_be:
                results.two_less_be.remove(value)
        for value in results.one_less_le:
            if value + 1 in results.two_less_le :
                results.two_less_le.remove(value + 1)
            if value in results.two_less_le:
                results.two_less_le.remove(value)
        # Remove results from full bytes searches in one and two bytes less searches
        for value in results.full_be:
            if value + 1 in results.one_less_be :
                results.one_less_be.remove(value + 1)
                if value + 2 in results.two_less_be:
                    results.two_less_be.remove(value + 2)
            if value in results.one_less_be:
                results.one_less_be.remove(value)
                if value in results.two_less_be:
                    results.two_less_be.remove(value)
        for value in results.full_le:
            if value + 1 in results.one_less_le :
                results.one_less_le.remove(value + 1)
                if value + 2 in results.two_less_le:
                    results.two_less_le.remove(value + 2)
            if value in results.one_less_le:
                results.one_less_le.remove(value)
                if value in results.two_less_le:
                    results.two_less_le.remove(value)
        results.total_length = len(results.full_be) + len(results.full_le) + len(results.one_less_be) + len(results.two_less_be) + len(results.one_less_le) + len(results.two_less_le)
        return results

def seek_ip(ip, symbols,symbol_selector):

    #Convert IP to hex value:
    hexipstring = binascii.hexlify(socket.inet_aton(ip))
    hexipstring =  binascii.unhexlify(hexipstring)
    index_list = []
    symbol = symbolselector.selectsymbol(symbols,symbol_selector)
    for message in symbol.messages:
        results = core_find(message.data,hexipstring,index_list)
        ####TODO Attempt to refine search and create new fields
        #Change stdout to get message print in buffer
        old_stdout = sys.stdout
        sys.stdout = buffer1 = io.StringIO()
        print(message)
        sys.stdout = old_stdout
        #Print results using click
        click.echo(click.style("Results for ", fg="blue") + click.style("[Message] : \n", fg = "green") + buffer1.getvalue() + "\n")
        click.echo(click.style("[Number of results found] : ", fg="green") + click.style(str(results.total_length) + "\n" ,fg ="red") )
        click.echo(click.style("Result indexes in message: \n ", fg="blue"))
        click.echo(click.style("[Whole IP Big Endian] : ", fg="green") + click.style( str(results.full_be) ,fg ="red") +"\n" )
        click.echo(click.style("[Three last terms of IP Big Endian] : ", fg="green") + click.style(str(results.one_less_be) ,fg ="red") + "\n" )
        click.echo(click.style("[Two last terms of IP Big Endian] : ", fg="green") + click.style(str(results.two_less_be),fg ="red")  + "\n" )
        click.echo(click.style("[Whole IP Little Endian] : ", fg="green") + click.style(str(results.full_le),fg ="red") + "\n"  )
        click.echo(click.style("[Three last terms of IP Little Endian] : ", fg="green") + click.style(str(results.one_less_le) ,fg ="red")  + "\n" )
        click.echo(click.style("[Two last terms of IP Little Endian] : ", fg="green") + click.style(str(results.two_less_le),fg ="red")  + "\n" )
        print('\n')
        click.echo(click.style("Attempting to create new fields", fg = 'yellow'))
        if symbol.fields:
            click.echo(click.style("Refining search to fields...", fg = 'yellow'))
            for field in symbol.fields:
                subfield_index_list = []
                field_values = field.getValues()
                number_of_values = len(set(field_values))
                # Get field length
                max_length = max([len(i) for i in field_values])
                if number_of_values > 1:
                    # More than one value => MUST CREATE ALT FIELD
                    # TODO
                    pass
                else:
                    mess = field_values[0]
                    field_result = core_find(mess,hexipstring,index_list)
                    if field_result:
                    # Searchstring not always split in between fields => Need to create subfields
                        click.echo(click.style("Searchstring inside fields, creating subfields...", fg='yellow'))
                        # Create field dict which contains fields and index
                        fields_dict = dict()
                        # Check if values in messages are different for need to create an alternative field or a simple raw field (above 1 if several values):
                        if number_of_values > 1:
                            #More than one value => MUST CREATE ALT FIELD
                            #TODO
                            pass
                        else:
                            #Can create simple static subfield
                            for i in field_result.full_be:
                                fields_dict[i] = Field(name = 'FullIpBe'+ str(i),domain = Raw(hexipstring))
                                subfield_index_list.append(i)
                                subfield_index_list.append(i + 4)
                            for i in field_result.one_less_be:
                                fields_dict[i] = Field(name='ThreeTIpBe' + str(i), domain=Raw(hexipstring[1:]))
                                subfield_index_list.append(i)
                                subfield_index_list.append(i + 3)
                            for i in field_result.two_less_be:
                                fields_dict[i] = Field(name='TwoTIpBe' + str(i), domain=Raw(hexipstring[2:]))
                                subfield_index_list.append(i)
                                subfield_index_list.append(i + 2)
                            for i in field_result.full_le:
                                fields_dict[i]= Field(name='FullIpLe' + str(i), domain=Raw(hexipstring[::-1]))
                                subfield_index_list.append(i)
                                subfield_index_list.append(i + 4)
                            for i in field_result.one_less_le:
                                fields_dict[i] = Field(name='ThreeTIpLe' + str(i), domain=Raw(hexipstring[1:][::-1]))
                                subfield_index_list.append(i)
                                subfield_index_list.append(i + 3)
                            for i in field_result.two_less_le:
                                fields_dict[i] = Field(name='TwoTIpLe' + str(i), domain=Raw(hexipstring[2:][::-1]))
                                subfield_index_list.append(i)
                                subfield_index_list.append(i + 2)
                            #Sort list in order
                            subfield_index_list.append(max_length)
                            subfield_index_list.insert(0,0)
                            #Remove duplicates (there shouldn't be any!)
                            subfield_index_list = list(set(subfield_index_list))
                            subfield_index_list = sorted(subfield_index_list, key=int)
                            #Create static field for every two elements of the subfield index_list as they represent beginning and end
                            for i,x in enumerate(subfield_index_list):
                                #Check if index is pair
                                if(i%2 == 0):
                                #Create static field and store it's beginning index in the structure
                                    try:
                                        fields_dict[x] = Field(name='Field' + str(i), domain = Raw(field_values[0][subfield_index_list[i]:subfield_index_list[i+1]]))
                                    except:
                                        fields_dict[x] = Field(name='Field' + str(i), domain=Raw(field_values[0][subfield_index_list[i]:]))
                                else:
                                # Don't do shit
                                    pass
                            #Create a list of all subfields in order
                            od = collections.OrderedDict(sorted(fields_dict.items()))
                            field_list = list(od.values())
                        field.fields = field_list
                    else:
                        #Searchstring always split in between other fields => Delete fields and create new ones Or just return indexes, and let user redefine fields manually
                            click.echo(click.style("Searchstring in between fields...", fg='yellow'))
                            click.echo(click.style("[1] : ", fg="green") + click.style("Delete all fields and replace by IPFIELDS"+ "\n", fg="blue"))
                            click.echo(click.style("[2] : ", fg="green") + click.style("Just print the index in the message"+ "\n", fg="blue"))
                            selector = input(" PLEASE SELECT AN ELEMENT TO SEEK >>>   ")
                            if selector == "1":
                                #TODO
                                pass
                            elif selector == "2":
                                manipulate_menu(symbols)
                            else:
                                click.echo(click.style("WRONG INPUT! QUITTING ", fg="red"))
    manipulate_menu(symbols)