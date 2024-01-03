import os

str=os.path.basename("D:\Documents and Works\Python\OS Module\A\B\C\C1.txt") 
print(str) #print only the specific file name

print(os.path.dirname("D:\Documents and Works\Python\OS Module\A\B\C\C1.txt")) #print the whole path of the file

print(os.path.exists("D:\Documents and Works\Python\OS Module\A\B\C\C1.txt")) #check whether the file or folder exists or not

print(os.path.isdir("D:\Documents and Works\Python\OS Module\A\B\C\C1.txt")) #check whether the directory exists or not

print(os.path.isfile("D:\Documents and Works\Python\OS Module\A\B\C\C1.txt")) #check whether the file exists or not

#problematic
os.chdir('D:\Documents and Works\Python\OS Module\Test folder')
dir=os.getcwd()
print(dir) 
os.path.join(dir, 'Test.py')

print(os.path.split("D:\Documents and Works\Python\OS Module\A\A1.txt"))