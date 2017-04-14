from collections import OrderedDict

def replace_symb(symbols,old_symbol,new_symbols):
    index = 0
    for i,symbol in enumerate(symbols):
        if symbol == old_symbol:
            index = i
            del symbols[i]
    if isinstance(new_symbols,list):
        for symbol in new_symbols:
            try:
                symbols.insert(index,symbol)
            except:
                symbols.append(symbol)
    elif isinstance(new_symbols,OrderedDict):
        for (name,symbol) in new_symbols.items():
            try:
                symbols.insert(index,symbol)
            except:
                symbols.append(symbol)
    else:
        pass
