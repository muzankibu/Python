txt = "My name is Showrav"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print(txt.encode())

txt = "Hello, welcome to my world."

x = txt.endswith('rld.',23,27)
print(x)