import DecodeWin as d
import test1 as e
import tkinter as tk

class Application(tk.Tk):
    """ the main window """
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("300x110+300+100")


        tk.Button(self, text="Encode", command=self.file_encode,height = 2, width = 10).place(x=70,y=20)
        tk.Button(self, text="Decode", command=self.file_decode,height = 2, width = 10).place(x=150,y=20)
        tk.Button(self, text="CLOSE ALL", command=self.close,height = 2, width = 10).place(x=110,y=65)

        self._encode_window = None
        self._decode_window = None

    def file_encode(self):
        if self._encode_window is not None:
           return

        self._encode_window = e.ApplicationEncode(self)

    def file_decode(self):
        if self._decode_window is not None:
            return

        self._decode_window = d.Decode(self)

    def close(self):
        if self._encode_window is not None:
            self._encode_window .destroy()
            self._encode_window  = None

        if self._decode_window is not None:
            self._decode_window .destroy()
            self._decode_window  = None

        exit(-1)

if __name__ == '__main__':
    window = Application()
    window.mainloop()