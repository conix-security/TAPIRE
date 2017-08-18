import uuid

def make_unique_names(symbol_list):
    symbol_names = []
    for symbol in symbol_list:
        if symbol.name not in symbol_names:
            symbol_names.append(symbol.name)
        else:
            symbol.name = symbol.name + str(uuid.uuid4())
            symbol_names.append(symbol.name)