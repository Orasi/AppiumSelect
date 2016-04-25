import re


class Caps(object):
    pass

def propertyFromString(property, title):
    try:
        return re.search(property + '=.*?[}|,]', title).group().split('=')[1].replace('}','').replace(',','')
    except:
        return ''
