import os
from PIL import Image,ImageEnhance,ImageFilter

path = os.path.abspath("./photos")
pathOut = os.path.abspath("./photosedited")

# Create the output directory
os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))
    
    #Sharpener + Black and White
    edit = img.filter(ImageFilter.SHARPEN).convert("L")
    
    #Add Contrast
    factor = 1
    enhancer = ImageEnhance.Contrast(edit)
    edit= enhancer.enhance(factor)
    
    
    #Saving
    clean_name = os.path.splitext(filename)[0]
    output_path = os.path.join(pathOut, f"{clean_name}_edited.png")
    edit.save(output_path)