y = ' '
z = '!'
x = f'смысл%s{y}%s{y}%sжизни' % (z, z, z)     # первых два способа f.'{}' и '%s' % z
x = ' '.join(x.split('{}'.format(y))[::-1])   # третий способ '{}'.format()
print(x)
