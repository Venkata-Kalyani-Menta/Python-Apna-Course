#To delete the files in python, we are using os module. So, if in your system, doesn't exist then you need to install module using pip command "pip3 install os"
import os 
os.remove("demo2.txt") #removes file "demo2.txt" if it exists otherwise it will shows FileNotFoundError