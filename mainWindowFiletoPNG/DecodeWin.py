import tkinter as tk
import numpy as np
import binascii
from PIL import Image
import os
import tkinter.filedialog

class Decode(tk.Toplevel):
     """ Aplication for decoding data in a picture"""
     def __init__(self,master):
         super().__init__(master)
         self.title("Decode")
         self.geometry("400x150+30+30")
         self.mainWin()
         self.protocol('WM_DELETE_WINDOW', master.close)

     def mainWin (self):
		#the main function
        tk.Button(self,text="Upload a PNG picture",command=self.upload_file,height = 1, width = 18).place(x=10,y=10)
        tk. Button(self, text="Save", command=self.save, height=1, width=18).place(x=10,y=35)
        tk.Button(self, text="Close", command=self.close, height=1, width=18).place(x=10, y=60)

     def close(self):
         Decode.destroy(self)

     def upload_file(self):

        file = tk.filedialog.askopenfilename()                                          #filedialog open
        srcImg = Image.open(file)                                                       #Try to open an image

        srcData = np.array(srcImg)                                                      #make the image into array

        while srcImg.format.upper() != 'PNG':                                           #Check, if we upload a PNG image.
            tk.Label(self, text="Warning: Use PNG only,please!").place(x=150,y=10)      #Loop will be stayed untill uploading a PNG image

            file = tk.filedialog.askopenfilename()
            self.srcImg = Image.open(file)

        tk.Label(self,text="1.Image read Successfully").place(x=150,y=10)

        srcData = srcData.flatten()                                                     #make the array into big one

        n = int((bin(srcData[0])[2:].zfill(8))[-3:], 2) + 1;                            #getting section with adding zeros

        hiddenDataSize = ''

        #WORK WITH DECODING DATA
        i = 1
        while len(hiddenDataSize) < 64:                                                 #64 becauseof bits
            binary = bin(srcData[i])[2:].zfill(8)
            hiddenDataSize += binary[-n:]
            i += 1

        self.hiddenData = ''
        if (len(hiddenDataSize)%64!=0):
            self.hiddenData = hiddenDataSize[-(len(hiddenDataSize)%64):]                #decoding the data (Working with the size)

        hiddenDataSize = int(hiddenDataSize[:64], 2)                                    #knowing the data size

        while len(self.hiddenData) < hiddenDataSize:                                    #len not size GO
            binary = bin(srcData[i])[2:].zfill(8)                                       #making a binary mode
            self.hiddenData += binary[-n:]
            i += 1

        self.hiddenData = self.hiddenData[:hiddenDataSize]                              #making section


     def save(self):
        #SAVE settings
        gf = "C:/Users/Nikita Gusev/Desktop/new"                                         #creating file with new name
        with  open(gf, "wb")  as f:
            i=0
            while i < len(self.hiddenData):                                               #i not len go on the data
                data = self.hiddenData[i:i+8]                                             #Going on the data
                data = '{0:02x}'.format(int(data, 2))
                byte = binascii.unhexlify(data)
                f.write(byte)                                                             # saving (writing) in a file
                i += 8

        tk.Label(self, text="2.The file was decoded successfully!").place(x=150,y=110)

