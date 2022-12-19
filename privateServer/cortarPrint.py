from PIL import Image

def cortarprint():
  fullImg = Image.open('screenshots/bot.png')
  cropImg = fullImg.crop((780, 300, 850, 350)) 
  cropImg.save('screenshots/antibot.png')