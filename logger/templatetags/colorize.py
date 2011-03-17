from django import template

register = template.Library()

def do_colorize(value):
    if not value:
        return "#000000"
    parts = [value[i::3] for i in range(3)] # break abcdef into ['ad','be','cf'] 
    output = "#"
    for value in parts:
        result = sum([ord(c) for c in value])*51%220
        output+= ("0%X" % result)[-2:]
    return output
register.filter("colorize", do_colorize)

