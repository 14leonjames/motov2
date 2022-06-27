import easyocr
import os


reader = easyocr.Reader(['en'])

# result = reader.readtext("crop/crop.jpg",paragraph="False")
result = reader.readtext("cd2.jpg",paragraph="True")
print(result[0][1])




