from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGBA', (400, 400), "white")
idraw = ImageDraw.Draw(img)
idraw.rectangle((100, 100, 300, 300), fill='grey', outline=(255, 255, 255))
idraw.ellipse((100, 100, 300, 300), fill='yellow', outline=(0, 0, 0))
idraw.ellipse((120, 100, 280, 300), fill='red', outline=(0, 0, 0))
idraw.ellipse((190, 150, 210, 250), fill='black', outline=(0, 0, 0))
text="Eye of mordor"
titleFont = ImageFont.truetype('KUNSTLER.TTF', 50)
idraw.text((120, 330), text, font = titleFont, fill="black")
img.save("LearnUp.png")