import os
import torch
import cv2
from torchvision import models, transforms

# Chuẩn bị model + preprocess (giống trên)
model = models.resnet18(pretrained=True).eval()
preprocess = transforms.Compose([...])

features_list = []
for fname in sorted(os.listdir("frames/")):
    img = cv2.imread(os.path.join("frames", fname))
    tensor = preprocess(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).unsqueeze(0)
    with torch.no_grad():
        x = model.conv1(tensor)
        # ... (như trên) ...
        feat = torch.flatten(model.avgpool(x), 1)
    features_list.append(feat.squeeze().numpy())

print(f"Đã trích xuất feature cho {len(features_list)} frame.")
