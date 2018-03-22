# steganographyPy
---------------------------------------------------------------------------------------------------------------------------------

It was my first serious project that I wrote on Python `(3.6+)`  with using windows(`tkinter`), `pil` (image) and `np.array`. 

The main idea of project is uploading a picture with some file (`encoding`), then `decode` new picture and  the program create a new file , where you should change for the right format. I think , it is easy for using it because there are windows. 

**Note**: use only PNG picture , please. Notice about the size of a file ,which you want to upload a picture.

**Some explanations:**

We have 2 lower bytes in one rank of our image.
If we try to record in those 2 bytes our additional information, our eyes can't see
any changes. That's why we can "hide" some info there.

If we have an image with size 1280x720, it means, we have `921.600 cells`.
Also, we have RGB image , it mean that `921.600 * 3 =2.764.800` (`8bytes`) values.
If we use 2 lower bytes from every value (=`2.764.800`), we will get `2.764.800*2=5.529.600` (`5.53 mb`)

It means that we can hide some text or even a small file there.

You can see some windows:

![Alt text](https://github.com/nikitaxgusev/steganographyPy/blob/master/12.png?raw=true "Optional Title")

![Alt text](https://github.com/nikitaxgusev/steganographyPy/blob/master/13.png?raw=true "Optional Title")
