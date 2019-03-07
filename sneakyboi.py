import math
import numpy
msg = input("What message would you like to send :")
shift = int(input("What size shift would you like to make? (positive numbers only):"))

def shrink():
    global shift
    if shift > 36:
        shift = shift%36
            
shrink()

for char in msg:
    if char in " ,?.!/;:":
        msg = msg.replace(char,'')
msg = msg.lower()

msgl = list(msg)

#This is my list of the alphabet
abc = []
for letter in range(97,123):
    #add a-z to the list "abc = []"
    abc.append(chr(letter))

#add numbers to the list "abc"
for x in range(0,10):
    abc.append(str(x))
#repeat the list so that now it's 72 characters long
    #a-z, 0-9, a-z, 0-9
for letter in range(97,123):
    abc.append(chr(letter))
for x in range(0,10):
    abc.append(str(x))
    
convert = {"a":abc[shift],
           "b":abc[1+shift],
           "c":abc[2+shift],
           "d":abc[3+shift],
           "e":abc[4+shift],
           "f":abc[5+shift],
           "g":abc[6+shift],
           "h":abc[7+shift],
           "i":abc[8+shift],
           "j":abc[9+shift],
           "k":abc[10+shift],
           "l":abc[11+shift],
           "m":abc[12+shift],
           "n":abc[13+shift],
           "o":abc[14+shift],
           "p":abc[15+shift],
           "q":abc[16+shift],
           "r":abc[17+shift],
           "s":abc[18+shift],
           "t":abc[19+shift],
           "u":abc[20+shift],
           "v":abc[21+shift],
           "w":abc[22+shift],
           "x":abc[23+shift],
           "y":abc[24+shift],
           "z":abc[25+shift],
           "0":abc[26+shift],
           "1":abc[27+shift],
           "2":abc[28+shift],
           "3":abc[29+shift],
           "4":abc[30+shift],
           "5":abc[31+shift],
           "6":abc[32+shift],
           "7":abc[33+shift],
           "8":abc[34+shift],
           "9":abc[35+shift],
           }

result = [convert.get(n, n) for n in msg]
end = "".join(result)
print(end)

mrse = input("Would you like to switch to morse code? y/n:")

mconvert = {"a":"•– ",
           "b":"–••• ",
           "c":"–•–• ",
           "d":"–•• ",
           "e":"• ",
           "f":"••–• ",
           "g":"––• ",
           "h":"•••• ",
           "i":"•• ",
           "j":"•––– ",
           "k":"–•– ",
           "l":"•–•• ",
           "m":"–– ",
           "n":"–• ",
           "o":"––– ",
           "p":"•––• ",
           "q":"––•– ",
           "r":"•–• ",
           "s":"••• ",
           "t":"– ",
           "u":"••– ",
           "v":"•••– ",
           "w":"•–– ",
           "x":"–••– ",
           "y":"–•–– ",
           "z":"––•• ",
           "0":"––––– ",
           "1":"•–––– ",
           "2":"••––– ",
           "3":"•••–– ",
           "4":"••••– ",
           "5":"••••• ",
           "6":"–•••• ",
           "7":"––••• ",
           "8":"–––•• ",
           "9":"––––• ",
           }
if mrse == "y":
    mend = [mconvert.get(n, n) for n in end]
    mend = "".join(mend)
    print(mend)
