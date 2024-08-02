import json
import os
from PIL import Image

json_dir = '/storage/intern_hcm/longph/test/label'
image_dir = '/storage/intern_hcm/longph/test/image'

image_save_dir = '/storage/intern_hcm/longph/test/rec_data/images'
label_save_dir = '/storage/intern_hcm/longph/test/rec_data/labels'

os.makedirs(image_save_dir, exist_ok=True)
os.makedirs(label_save_dir, exist_ok=True)

for json_filename in os.listdir(json_dir):
    if json_filename.endswith('.json'):
        json_file_path = os.path.join(json_dir, json_filename)
        
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        image_filename = data['imagePath'].split('/')[-1]
        image_file_path = os.path.join(image_dir, image_filename)
        
        image = Image.open(image_file_path)
        
        for i, shape in enumerate(data['shapes']):
            label = shape['description']
            points = shape['points']
            
            xmin, ymin = int(points[0][0]), int(points[0][1])
            xmax, ymax = int(points[1][0]), int(points[1][1])
            
            cropped_image = image.crop((xmin, ymin, xmax, ymax))
            
            cropped_image_filename = f'{json_filename[:-5]}_{i:04d}.jpg'
            label_filename = f'{json_filename[:-5]}_{i:04d}.txt'
            
            image_save_path = os.path.join(image_save_dir, cropped_image_filename)
            label_save_path = os.path.join(label_save_dir, label_filename)
            
            cropped_image.save(image_save_path)
            
            with open(label_save_path, 'w', encoding='utf-8') as label_file:
                label_file.write(label)

print("DONE")
