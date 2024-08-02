import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from vietocr.vietocr.tool.predictor import Predictor
from vietocr.vietocr.tool.config import Cfg

# Load and modify configuration
config = Cfg.load_config_from_name('vgg_transformer')
config['cnn']['pretrained'] = False
config['device'] = 'cuda:0'

detector = Predictor(config)

img_path = '/storage/intern_hcm/longph/number.png'
img = Image.open(img_path)

detected_text = detector.predict(img)
print(f'Detected Text: {detected_text}')

draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
text_position = (10, 10)  # Position of the text on the image
text_color = (255, 0, 0)  # Color of the text (red)

draw.text(text_position, detected_text, fill=text_color, font=font)

annotated_img_path = '/storage/intern_hcm/longph/006_annotated.png'
img.save(annotated_img_path)