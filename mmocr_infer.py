from mmocr.apis import MMOCRInferencer
import cv2

infer = MMOCRInferencer(det='DBNetpp')

img_path = '/storage/intern_hcm/longph/datasets/cavet/image/img_front/133.jpg'

result = infer(img_path, return_vis=True)

# Lưu kết quả hình ảnh
output_image_path = 'img0_saved.jpg'
cv2.imwrite(output_image_path, cv2.cvtColor(result['visualization'][0], cv2.COLOR_RGB2BGR))

print(f"Kết quả hình ảnh đã được lưu")