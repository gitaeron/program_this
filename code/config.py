import os
import re

# 绝对不会有问题的路径!!!!
tmp = os.path.abspath(os.getcwd())
tmp = tmp.split("\\")

pro_path = ''

for i in range(len(tmp)):
    if tmp[i] != 'program_this':
        pro_path += tmp[i] + "\\"
    else:
        pro_path += tmp[i]
        break

PROJECT_PATH = os.path.abspath(pro_path)
# print(PROJECT_PATH)


# code 
CODE_PATH = PROJECT_PATH + "\\code"
CODE_PATH = os.path.abspath(CODE_PATH)

# dataset
DATASET_PATH = PROJECT_PATH + "\\datasets"
DATASET_PATH = os.path.abspath(DATASET_PATH)

# dataset.yaml path
DATASET_YAML_PATH = DATASET_PATH + "\\dataset.yaml"
DATASET_YAML_PATH = os.path.abspath(DATASET_YAML_PATH)

# model => may delete in future ?
MODEL_PATH = PROJECT_PATH + "\\model\\yolov8n.pt"
MODEL_PATH = os.path.abspath(MODEL_PATH)

BEST_MODEL_PATH = PROJECT_PATH + "\\model\\best.pt"
BEST_MODEL_PATH = os.path.abspath(BEST_MODEL_PATH)

BEST_2023_06_19_MODEL_PATH = PROJECT_PATH + "\\model\\2023-06-19-best.pt"
BEST_2023_06_19_MODEL_PATH = os.path.abspath(BEST_2023_06_19_MODEL_PATH)
# print(MODEL_PATH)

# save path after train
SAVE_NAME = 'save'
SAVE_PATH = CODE_PATH
SAVE_PATH = os.path.abspath(SAVE_PATH)

# video captured image save path
VIDEO_IMAGE_SAVE_PATH = DATASET_PATH + "\\predict\\video_captured_image.jpg"
VIDEO_IMAGE_SAVE_PATH = os.path.abspath(VIDEO_IMAGE_SAVE_PATH)
# print(VIDEO_IMAGE_SAVE_PATH)

# UI image path
UI_HOME_IMG_PATH = os.path.abspath(PROJECT_PATH + "\\rs\\home_img.png")
UI_TEST_IMG_PATH = os.path.abspath(PROJECT_PATH + "\\rs\\test_img.png")
UI_PREDICT_IMG_PATH = os.path.abspath(PROJECT_PATH + "\\rs\\predict_img.png")
# print(UI_HOME_IMG_PATH)
# print(UI_TEST_IMG_PATH)
# print(UI_PREDICT_IMG_PATH)

