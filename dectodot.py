import socket, struct
import ipaddress
from itertools import permutations


def checkValidIp( IPS ):
    word = ""
    setword = []
    strlength = len(IPS)
    print(len(IPS))
    p1 = IPS[0:3]
    p2 = IPS[3:6]
    p9 = p1+ "." + p2 + "."
    p3 = IPS[6:9]
    p4 = IPS[9:12]
    p5=p3+p4
    p7 =[]
    #Initialisation of Variables
    
    
    if p1 == p2:
        if(strlength == 12):
            for i,w in enumerate(IPS):
                if (i == 3) or (i == 6) or (i == 9):
                    word = word + "."       
                word = word + w
        
        if(strlength == 11):
            p5 = p3[1:3] + p4    
            #split one after because 1:111 cannot happen so should split it away
            
            for i,w in enumerate(p5):
                p7.append(p9 + p3[0:1] + p5[0:i+1] + "." + p5[i+1:(len(p5))])
                #appends the 123.123 to the first digit to the changing position of the . and its surrounding numbers
                if i > len(w) -1:
                    break
                #stops the dot from going too far
            return (p7)
        
        if(strlength == 10):
            
            for i,w in enumerate(p5):
                p7.append(p9 + p5[0:i+1] + "." + p5[i+1: (len(p5))])
                if i > len(w):
                    break
            return (p7)
        
        if(strlength == 9):
    
            for i,w in enumerate(p3):
                setter = (p9 + p3[0:i+1]  + "." + p3[i+1:(len(p3))])
                p7.append(setter[0:len(setter) - (i -1)])
                if i > len(w):
                    break
            return (p7)
        
        if(strlength == 8):
            for i,w in enumerate(p3):
                setter = (p9 + p3[0:i+1]  + "." + p3[i+1:(len(p3))])
                p7.append(setter[0:len(setter) - (i)])
                if i > len(w):
                    break
            return (p7)
        
        if(strlength == 7):
            for i,w in enumerate(p3):
                setter = (p9 + p3[0:i+1]  + "." + p3[i+1:(len(p3))])
                p7.append(setter[0:len(setter) - (i+1)])
                if i > len(w):
                    break
            return (p7)
    
    
    setword.append(word)
    return (setword)
    #returns the word

        
def main():
    #listword = checkValidIp("123123454")
    #print(listword)
    #checks output and calls function
    pass
    
main()
#calls main
        


        

