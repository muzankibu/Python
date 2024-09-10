#from pickletools import string1


String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)
 
# Keyword Formatting
String1 = "{l} {f} {g}"+" is kind of cool!".format(g='Geeks', f='with', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)