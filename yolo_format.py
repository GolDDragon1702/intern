import json
import os

json_dir = '/storage/intern_hcm/longph/test/label'
output_dir = '/storage/intern_hcm/longph/yolo/labels'

os.makedirs(output_dir, exist_ok=True)

# Mapping of labels to numbers
label_mapping = {
    "name": 0,
    "engine": 1,
    "address": 2,
    "chassis": 3,
    "brand": 4,
    "model": 5,
    "type": 6,
    "color": 7,
    "capacity": 8,
    "seat": 9,
    "origin": 10,
    "plate": 11,
    "first_date": 12,
    "number": 13
}

def convert_to_yolo_format(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    image_width = data['imageWidth']
    image_height = data['imageHeight']
    
    yolo_data = []
    
    for shape in data['shapes']:
        if shape['shape_type'] == 'rectangle':
            label = shape['label']
            label_num = label_mapping[label]
            
            x_min, y_min = shape['points'][0]
            x_max, y_max = shape['points'][1]
            
            # Calculate center_x, center_y, width, height
            center_x = (x_min + x_max) / 2.0 / image_width
            center_y = (y_min + y_max) / 2.0 / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height
            
            yolo_data.append(f"{label_num} {center_x} {center_y} {width} {height}")
    
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(json_file))[0] + '.txt')
    with open(output_file, 'w') as f:
        f.write('\n'.join(yolo_data))

for json_file in os.listdir(json_dir):
    if json_file.endswith('.json'):
        convert_to_yolo_format(os.path.join(json_dir, json_file))