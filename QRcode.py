# To make a QR code first of all we need to install the 'qrcode' library. RUN `pip install qrcode`(in windows) or `pip3 install qrcode`(in linux/ mac OS)
# Now import the library as follows
import qrcode as Q

# We will make here a simple black an white QR code.

sos = Q.make("This is the first QR that i have made using python.")  
# In the make function we can pass the data that we want to encode in the QR code.If we pass a url then it will redirect user to that url also any text can valid here to show it to user.
 
sos.save("QR.png")
  
# Now to save the image of QR we can pass the name by which we want to save it(here 'danger.png').
# 
#Now run the code and you will get the png file in the same directory where your code is saved.  
