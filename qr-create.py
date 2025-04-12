import qrcode
import sys, getopt
import argparse
import traceback

def Main(argv):
    try:
        argParser = argparse.ArgumentParser()
        argParser.add_argument("-d","--DATA", type=str, help="Data you want to add to QR Code")
        argParser.add_argument("-n","--NAME", type=str, help="Name of QR Code image file")
        argParser.parse_args()
        opts, args = getopt.getopt(argv,"d:n:")
        qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

        for opt, arg in opts:
            if opt == '-d':                
                qr.add_data(arg)
                qr.make(fit = True)
            if opt == '-n':
                img = qr.make_image(fill_color = 'black', back_color = 'white')
                img.save(f'{arg}.png')
    except Exception as e:
        traceback.print_exc()
        sys.exit(2)

if(__name__ == "__main__"):
    Main(sys.argv[1:])