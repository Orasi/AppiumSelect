import re


class Caps(object):
    pass

def propertyFromString(property, title):
    return re.search(property + '=.*?[}|,]', title).group().split('=')[1].replace('}','').replace(',','')
