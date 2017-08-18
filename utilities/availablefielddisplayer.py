import click

from utilities import symbolselector

def display_available_fields(fields):

    child = False
    recurse = True
    while recurse:
        names = []
        for field in fields:
            names.append(field.name)
        click.echo(click.style("Available fields:\n", fg="blue"))
        if len(fields) > 1:
            field_list = []
            for field in fields:
                field_list.append(field.name)
            click.echo(click.style(str(field_list)+ '\n',fg="red"))
            print("\n")
            field_selector = input(" PLEASE SELECT A FIELD >>>   ")
            print("\n")
            if field_selector != "*":
                field = symbolselector.selectsymbol(fields, field_selector)
        else:
            if fields[0].name ==  None :
                click.echo(click.style("Field-0" + "\n", fg = "red"))
                field_selector = "Field-0"
            else:
                click.echo(click.style(fields[0].name + "\n", fg="red"))
                field_selector = fields[0].name
            field = fields[0]
        #Check field_selector
        if field_selector not in names:
            if field_selector != "*":
              print("\033[1;31m" + "Error in selection " + '\033[0m')
              continue
        # Check if the field has children
        if len(field.fields) > 0:
            # If so, recurse in function
            fields = field.fields
            child = True
            continue
        else:
            recurse = False
    return field, field_selector,child


def display_available_fields_only(fields, ommit = None):

    child = False
    recurse = True
    while recurse:
        names = []
        for field in fields:
            names.append(field.name)
        click.echo(click.style("Available fields:\n", fg="blue"))
        if len(fields) > 1:
            field_list = []
            for field in fields:
                if ommit is not None:
                    if field.name != ommit.name:
                        field_list.append(field.name)
                else:
                    field_list.append(field.name)
            click.echo(click.style(str(field_list)+ '\n',fg="red"))
            print("\n")
            break
