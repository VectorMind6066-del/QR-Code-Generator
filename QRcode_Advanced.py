# import the 'qrcode' library in python to generate any QR code.

import qrcode as Q 

sos = Q.QRCode(version=1,error_correction=Q.constants.ERROR_CORRECT_H,box_size=100,border=50) 
# This commands reduces the size of QR code and makes it more clear and readable.also it reduces any errors in the QR.

sos.add_data("paste your content here")  
# All the data that you want to encode in the QR code can be passed here. It can be a url or any text.

sos.make(fit=True)    
# This command makes the QR code fit in the given size and reduces the size of QR code. 

img = sos.make_image(fill_color="purple",back_color="black")  
# This command helps to change the color of QR code. Here we have changed the color of QR code to purple and background to pink.

img.save("Qp.png")       
# This command saves the QR code in the same directory where your code is saved. You can also change the name of the file by changing the name in the brackets.
