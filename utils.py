import os
import cv2
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import shutil


def preprocess_frame(frame, roi):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi = get_bbox_within_image_bounds(roi, frame.shape[1], frame.shape[0])
    x1, y1 = roi[0]
    x2, y2 = roi[1]
    cropped_gray_frame = gray_frame[y1:y2, x1: x2]

    return cropped_gray_frame


def display_message(message, frame, point_to_display=(20, 50)):
    base_color_to_display = (255, 255, 255)
    front_color_to_display = (0, 120, 255)
    base_thickness = 2
    front_thickness = 1
    font_scale = 1
    cv2.putText(frame, message, point_to_display, cv2.FONT_HERSHEY_SIMPLEX, font_scale, base_color_to_display, base_thickness, 16)
    cv2.putText(frame, message, point_to_display, cv2.FONT_HERSHEY_SIMPLEX, font_scale, front_color_to_display, front_thickness, 16)

    return frame


def get_number_from_list(numbers_list):
    return ''.join(numbers_list)


def get_bbox_within_image_bounds(bbox, img_width, img_height):
    '''

    :param bbox: [(x1,y1), (x2, y2)]
    :param img_width:
    :param img_height:
    :return:
    '''
    p1 = bbox[0]
    p2 = bbox[1]
    new_p1 = get_point_within_image_bounds(p1, img_width, img_height)
    new_p2 = get_point_within_image_bounds(p2, img_width, img_height)

    return [new_p1, new_p2]


def get_point_within_image_bounds(point, img_width, img_height):
    x = max(point[0], 0)
    y = max(point[1], 0)

    x = min(x, img_width)
    y = min(y, img_height)

    return (x, y)


def detect_color_area(hsv_img, color='yellow'):

    """
    lower = np.array([hue_lower, saturation_lower, value_lower])
    upper = np.array([hue_upper, saturation_upper, value_upper])
    """
    if color == 'yellow':
        lower = np.array([15, 130, 120])
        upper = np.array([30, 255, 255])
    elif color == 'red':
        lower = np.array([0, 150, 100])
        upper = np.array([15, 255, 255])

    image_mask = cv2.inRange(hsv_img, lower, upper)
    kernel = np.ones((3, 3), np.uint8)
    image_mask = cv2.dilate(image_mask, kernel, 2)
    image_mask = cv2.GaussianBlur(image_mask, (3, 3), 0,0)
    image_mask = cv2.erode(image_mask, kernel, 2)
    color_area = cv2.countNonZero(image_mask)

    return color_area


def convert_mnist_csv_to_img(input_csv_file):

    df = pd.read_csv(input_csv_file)
    images = df.values[0:, 1:]
    img = images[1].reshape((28, 28))
    plt.imshow(img)
    plt.show()


def segregate_data(input_dir, output_dir):
    for root, dir, files in os.walk(input_dir):
        for filename in files:
            filename_split = filename.split('_')[1].split('.png')[0]
            output_folder = os.path.join(output_dir, filename_split)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            shutil.copy(os.path.join(root, filename), output_folder)


def divide_data(input_dir, output_dir, train_number):

    train_output_dir = output_dir+'//train'
    val_output_dir = output_dir + '//val'

    for root, dir, files in os.walk(input_dir):
        file_count = 0
        random.shuffle(files)
        for filename in files:
            if file_count < train_number:
                output_dir_cnn = train_output_dir
            else:
                output_dir_cnn = val_output_dir
            cnn_dir = os.path.join(output_dir_cnn, os.path.basename(root))

            if not os.path.exists(cnn_dir):
                os.makedirs(cnn_dir)

            shutil.copy(os.path.join(root, filename), cnn_dir)
            file_count += 1