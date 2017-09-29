import tkinter as tk
from PIL import Image
import numpy as np
import binascii
import tkinter.filedialog


class ApplicationEncode(tk.Toplevel):
    """ Aplication for encoding data in a picture"""
    def __init__(self,master):
        super().__init__(master)
        self.hiddenData = ''
        self.title("Encode")
        self.main_win()
        self.geometry("400x120+30+30")
        self.protocol('WM_DELETE_WINDOW', master.close)

    def main_win(self):
        #for a window
        self.upl_btn=tk.Button(self, text="Upload a PNG picture", command=self.upload_file,height = 1, width = 18).place(x=10,y=10)
        self.upl_file_btn=tk.Button(self, text="Upload a file", command=self.uploadHidden_file,height = 1, width = 18).place(x=10,y=35)
        tk.Button(self, text="Encode", command=self.Encode_mech,height = 1, width = 18).place(x=10,y=60)
        tk.Button(self, text="Close", command=self.close,height = 1, width = 18).place(x=10, y=85)



        n = np.uint8(7)
        if n > 8 or n < 1:
            exit()

    def close(self):
        ApplicationEncode.destroy(self)

    def upload_file(self):

        file = tk.filedialog.askopenfilename()
        self.srcImg=Image.open(file)                                                           #Open an image for encondig

        while self.srcImg.format.upper() != 'PNG':                                             #Check for format of a picture(using format.upper())
            tk.Label(self, text="Warning: Use PNG only,please!").place(x=150,y=10)             # If not a PNG format , calling filedialog again
            file = tk.filedialog.askopenfilename()
            self.srcImg = Image.open(file)                                                     #Try open an image


        self.srcData = np.array(self.srcImg)                                                   #make our picture in array data

        tk.Label(self,text="1.Successfully uploaded a 'PNG' picture").place(x=150,y=10)

                                                                           #Value for hidding data(It's empty)???

        self.row = len(self.srcData)                                                           #Figuring out the size of array (size of a picture)
        self.col = len(self.srcData[0])
        self.height = len( self.srcData[0][0])                                                 #Because we use RGB (3)????
       # print(self.row,self.col,self.height)
        self.srcData =  self.srcData.flatten()                                                 #Make our array in big one(Before: it was of several arrays)


    def uploadHidden_file(self):
        file = tkinter.filedialog.askopenfilename()                                            #Open file for hidding
        with open(file, "rb") as f:                                                            #Open in 'rb' mode for reading it in way like: 010101010
            byte = f.read(1)                                                                   #if we miss opening in binary mode, we try to do it by our hands
            while byte:
                hexadecimal = binascii.hexlify(byte)
                decimal = int(hexadecimal, 16)
                binary = bin(decimal)[2:].zfill(8)
                self.hiddenData += binary
                byte = f.read(1)

        tk.Label(self, text="2.Successfully uploaded a file in the picture").place(x=150,y=35)

    def Encode_mech(self):

        hiddenDataSize = bin(len(self.hiddenData))[2:].zfill(64)                                #make our hidded size in binary mode from string , and make it for 64 bits
        noOfBitsUsed = bin(7 - 1)[2:].zfill(3)                                                  #The value, which is the LSB,is used for hidden data (it's 6)
        self.hiddenData = hiddenDataSize + self.hiddenData                                      #set hidden data value

        self.hiddenData += "0" * (7 - (len(self.hiddenData) % 7))                               #Adding LSB to hidden data

        if len(self.hiddenData) > 7 * (len( self.srcData) - 1):
            tk.Label(self, text="Warning:The size of a picture is too small for encoding").place(x=150,y=60)
            exit(-1)

        self.srcData[0] &= 248                                                                  #changing R of RGB
        self.srcData[0] |= np.uint8(int("00000" + noOfBitsUsed, 2))                             #Inputting LSB in R of RGB

        i = 1
        j = 0
        setToZero = np.uint8(255 << 7)                                                          #make a bit -> in 255 value (shift it)
        while i < len(self.srcData) and j < len(self.hiddenData):
            self.srcData[i] &= setToZero                                                        #Record a 128
            bits = np.uint8(int("0" * (8 - 7) + self.hiddenData[j:j + 7], 2))                   #getting bits
            self.srcData[i] |= bits                                                             #recording hidding info in array of a picture
            i += 1
            j += 7

        self.srcData = np.reshape(self.srcData, [self.row, self.col, self.height])              #reshape srcData


        self.img = Image.fromarray(self.srcData)                                                #convert from array in an image
        fp=open('C:/Users/Nikita Gusev/Desktop/new.png', 'wb')
        self.img.save(fp)                                                                       #save image
        tk.Label(self, text="3. Finished").place(x=150,y=60)

