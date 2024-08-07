import os
import json

json_folder = '/storage/intern_hcm/longph/data/Labels/label_back'
image_folder = '/storage/intern_hcm/longph/data/Images/img_back'

for json_filename in os.listdir(json_folder):
    if json_filename.endswith('.json'):
        json_path = os.path.join(json_folder, json_filename)
        
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        image_filename = json_filename.replace('.json', '.jpg')
        new_image_path = os.path.join(image_folder, image_filename)
        
        data['imagePath'] = new_image_path
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

print("Done")
