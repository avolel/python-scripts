from barcode import UPCA
from barcode.writer import ImageWriter 

number = '134730321732'
mycode = UPCA(number, writer=ImageWriter())
mycode.save("sample_code")