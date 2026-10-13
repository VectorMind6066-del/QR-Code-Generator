
import qrcode as q
import colorama
colorama.init(autoreset=True)



print("*"*120)
print()
text = colorama.Fore.CYAN + "$ Welcome To QR code Generator $"
print(text.center(120))
print()
print("*"*120)
print()


def QR_code():
   print("*You can add any text,URL or Data to generate QR -->")
   print()
   qr = q.make(input(colorama.Fore.GREEN + "[$] Enter the text or url here to generate QR code:"))
   name = input(colorama.Fore.GREEN + "[$] Enter the name how you want to save the QR:")
   qr.save(f"{name}.png")
   print()
   print(colorama.Fore.YELLOW + f"Your QR has successfully saved in your file as {name}.png")
   print("*"*100)
   print()
   return main()

def Advance_QR():
    print("*"*90)
    print("*  <--",colorama.Fore.RED + "[*]",colorama.Fore.BLUE + "Recommanded box_size and border for best QR ",colorama.Fore.RED +"[*]", "-->","                         *")
    print("*  1].10 x 5                        2].20 x 10","                                          *")
    print("*","                                                                                       *")
    print("*  <--",colorama.Fore.RED + "[*]",colorama.Fore.BLUE + "Recommanded fill color and back color for best QR ",colorama.Fore.RED +"[*]", "-->","                   *")
    print("*  1].pink x black                   2].purple x black","                                  *")
    print("*  3].blue x red                     4].green x white","                                   *")
    print("*  5].yellow x blue                  6].cyan x white","                                    *")
    print("*","                                                                                       *")
    print("*",  colorama.Fore.RED + "NOTE:","                                                                                 *")
    print("*  Box_size is the size of QR box while border is the size of inner QR pattern","          *")
    print("*  Fill color is the color for inner QR pattern while back color is the background color","*")
    print("*","                                                                                       *")
    print("*"*90)
    print()

    decorator = colorama.Fore.GREEN + "[$]"
    size = int(input(f"{decorator} Enter the box_size of QR code (should not > 100,or you will get an memory error):"))
    border = int(input(f"{decorator} Enter the border of QR code (should not > 50,or you will get an memory error):"))
    sos = q.QRCode(version=1,error_correction=q.constants.ERROR_CORRECT_H,box_size=size,border=border)
    print()
    print("*You can add any text,URL or Data to generate QR -->")
    sos.add_data(input(colorama.Fore.GREEN + "[$] Enter the text or url here to generate QR code:"))
    sos.make(fit=True)
    print()
    filll_color = input(colorama.Fore.GREEN + "[$] Enter the fill color for QR:")
    back_color = input(colorama.Fore.GREEN + "[$] Enter the back color for QR:")
    img = sos.make_image(fill_color=filll_color,back_color=back_color)
    name = input(colorama.Fore.GREEN + "[$] Enter the name how you want to save the QR:")
    img.save(f"{name}.png")
    print()
    print(colorama.Fore.YELLOW + f"Your QR has successfully saved in your file as {name}.png")
    print("*"*100)
    print()
    return main()




def main():
    while True:
        print(colorama.Fore.GREEN + "[*]","Which type of QR do you want -->")
        print("1.QR code [Black & White QR]")
        print("2.Advanced QR code [Colorful QR]")
        print("3.Exit")
        print()
        a = colorama.Fore.GREEN + "[$]"
        choice = int(input(f"{a}Enter the index of your choice:"))
        print()

        if choice == 1:
            QR_code()
            print("*"*80)
            print()

        elif choice == 2:
            Advance_QR()
            print("*"*80)
            print()


        elif choice == 3:
            print("Thank you for using QR code generator. Have a nice day!!")
            print()
            break
        

        else :
            print("Invalid choice!!. Please select a valid option.")
            print("*"*80)
            print()


if __name__ == "__main__":
    main()