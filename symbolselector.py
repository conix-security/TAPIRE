def selectsymbol(symbols,symbol_selector):
    for sym in symbols:
        if sym.name == symbol_selector:
            return sym