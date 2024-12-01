import torch
# ultralytics
# detection_model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5/runs/train/yolov5s-custom-detection/weights/best.pt', force_reload=True)
# structure_model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5/runs/train/yolov5s-custom-structure/weights/best.pt', force_reload=True)

import cv2
imgsz = 640
checkpoint = r"J:/tr/tablePT/structure.pt"
# structure_model = torch.load(checkpoint)
structure_model = torch.hub.load(r"J:/tr/tablePT", 'custom', r"J:/tr/tablePT/structure.pt", source='local')

# model = torch.hub.load(path, 'resnet50', pretrained=True)
def table_structure(filename):
    image = cv2.imread(filename)
    pred = structure_model(image, size=imgsz)
    pred = pred.xywhn[0]
    result = pred.numpy()
    return result