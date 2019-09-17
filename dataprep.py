print("######Running dataprep.py######")
print("Importing Packages...##",end=" ")
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
print("IMPORT DONE.\n")

print("Setting Global Variables ... ##",end=' ')
data=pd.DataFrame()
flag=0;bots=0
names=[]
print("Done\n")

def NotFoundSoln(ftypes,title):
    print("\n\t\t!!! File not Found !!!")
    choose=str(input("\n\t\tOpen File Picker to Choose File to load?\nEnter [y/n]:   "))
    if choose=='y':
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        root=Tk()
        filename = askopenfilename(filetypes = ftypes,title = title)
        root.withdraw()
        print ("This is Chosen FilePath : ",filename)
        return filename
    elif choose=='n':
        print("\n\t\tThere is no File to Load !!! Cannot Proceed without Data file !!!")
        print("Try again to Load a data file")
        NotFoundSoln(ftypes,title)
    else:
        print("Wrong Choice...TRY AGAIN\n")
        NotFoundSoln(ftypes,title)


try:
    print("Importing Data from File...##",end=" ")
    data=pd.read_excel('houseData.xls',header=None)
    data.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
    flag=2
    print("Read DONE.\n")
except FileNotFoundError:
    ftypes = [('Excel FIle',"*.xls"),('CSV File',"*.csv")]
    ttl  = "Data File Picker"
    filename1=NotFoundSoln(ftypes,tt1)
    print("Reading Data from the chosen file ...##",end=' ')
    data=pd.read_excel(filename1,header=None)
    data.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
    flag=1
    print("Read DONE.\n")
        
finally:
    print("Data Ready to Process")



row,col=data.shape
print("Rows and Cols : ",row,col)


data=shuffle(data)

#print(data.head())

if flag==1:
    print("It seems that You have choosen a File to load instead of default file")
    def choser1():
        print("Do you want to save the current open file for later use?")
        choose=str(input("\n\t\tOpen File Picker to Choose file to open?\nEnter [y/n]:   "))
        if choose=='y':
            print("\nSaving Data to CSV file (flowdata.csv)...##",end=" ")
            data.to_csv('flowdata.csv')
            print("TO CSV DONE.")
print("\n\nEND\n")
