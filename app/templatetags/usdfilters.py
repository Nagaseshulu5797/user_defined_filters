from django import template

register=template.Library()

@register.filter()
def swap(value):
    return value.swapcase()


@register.filter()
def counting(value,arg):
    c=0
    for x in range(len(value)):
        if arg==value[x:x+len(arg)]:
            c+=1
    return c


@register.filter(name='remove')
def remove(value,arg):
    return value.replace('arg','')


@register.filter(name='vowels')
def vowels(value):
    v='aeiouAEIOU'
    c=0
    for x in value:
        if x in v:
            c+=1
    return c

#register.filter('vowels',vowels)
#register.filter('counting',counting)
#register.filter('remove',remove)
#register.filter('swapping',swap)

