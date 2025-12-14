# YOLOv8 Pothole Detection – Training

This folder contains the configuration and instructions used to fine-tune the YOLOv8s model on a pothole-detection dataset using Nebius Cloud GPUs.

## Training Command

The model was trained for 100 epochs using the Ultralytics CLI:

```bash
yolo detect train \
    model=yolov8s.pt \
    data=data.yaml \
    epochs=100 \
    imgsz=640 \
    batch=8
```

## Dataset
The `data.yaml` is the file format that `yolo` can read, the dataset that was used to train this model can be found in huggingface:

[Pothole dataset](https://huggingface.co/datasets/Ryukijano/Pothole-detection-Yolov8)

## Model

The model was also uploaded to huggingface which can be found here:

[Yolov8 pothole detection model](https://huggingface.co/peterhdd/pothole-detection-yolov8)

# Sample Predictions

Here are some predictions from the model after it was generated:

![dataset prediction](image.png)