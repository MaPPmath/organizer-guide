import re
import codecs

plaintext = open("plaintext.txt","r").read()
plaintext = plaintext.upper()
plaintext = re.sub(r"[^A-Z\n]+"," ",plaintext)

#plaintext = codecs.encode(plaintext,'rot_13')

#def make_even(str):
#  if len(str) % 2 == 0:
#    return str
#  else:
#    return str[0:-1]
#

def trim_line(line):
  if line.endswith(" "):
    return trim_line(line[:-1])
  if line.startswith(" "):
    return trim_line(line[1:])
  else:
    return line

plaintext = "\n".join([trim_line(line) for line in plaintext.split("\n")])

display = plaintext.replace("\n","\n\n")
display = display.replace(" ","$\\cdot{}$")
print(display)

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]

for line in plaintext.split("\n"):
  for word in line.split(" "):
    for index,char in enumerate(list(word)):
      val = ord(char)-64# (ord(char)-65+primes[index])%26+1
      if val//9 == 0:
        first = "C"
      elif val//9 == 1:
        first = "T"
      else:
        first = "S"
      if val//3%3 == 0:
        second = "C"
      elif val//3%3 == 1:
        second = "T"
      else:
        second = "S"
      if val%3 == 0:
        third = "C"
      elif val%3 == 1:
        third = "T"
      else:
        third = "S"
      print('\\tikz{{\code{}{{\code{}{{\code{}{{}}}}}}}}'.format(first,second,third))
    print('\\hspace{1em}')
  print()
