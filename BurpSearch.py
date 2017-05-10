import os
import sys
import re
def check_dir(d):
 #   print (d)
    os.chdir(d)
    for i in os.listdir(os.getcwd()):

        if(os.path.isdir(i)):
            check_dir(i)
            os.chdir("..")
        else:
            f=open(i)
            for j in f.readlines():
                if matches(j):
                    print ("\n\n\n-----------------------------")
                    print("\tMatch Found")
                    print ("-----------------------------")
                    print("File:\n\t"+os.getcwd()+"/"+i)
                    print ("Line:\n\t"+j)

def matches(qu):
    if(option=="-r"):
        return bool(re.match(q,qu))
    elif(option=="-s"):
        if(q in qu):
            print ("sdf")
            return True
        else:
            return False
    elif(option=="-h" or "--help"):
        print ("Usage: python [option] [query] [location]\nOPTIONS:\n-r: Use regular expression\n-s: Normal search")
    else:
        print ("Invalid option : use -h or --help for help")

try:
    cwd=sys.argv[3]
except:
    cwd=os.getcwd()
option=sys.argv[1]
q=sys.argv[2]
check_dir(cwd)