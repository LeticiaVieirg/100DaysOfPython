#Mutable strings are less efficient than non-multable strings
import UserString

string=UserString.MultableString('Leticia')
string[0]='H'

print(string)
