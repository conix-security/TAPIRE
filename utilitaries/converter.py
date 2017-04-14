import codecs

def input_to_raw(string):
    string = codecs.decode(string, "unicode_escape")
    return string.encode('ISO-8859-1')