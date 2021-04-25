from handGesture import *
from utils import *
import keras


def check_for_reset_stop(frame):
    # check for an object of particular color and size in the frame
    # if object is RED in color then user wants to stop the application, isStop = True
    # if object is YELLOW in color then user wants to reset the calculator, isReset = True
    isReset = False
    isStop = False

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellow_area = detect_color_area(hsv_image, 'yellow')
    red_area = detect_color_area(hsv_image, 'red')

    if yellow_area > red_area and yellow_area > 0.1*frame.shape[0]*frame.shape[1]:
        isReset = True
        print('Resetting Calculator')
    elif red_area > yellow_area and red_area > 0.1*frame.shape[0]*frame.shape[1]:
        isStop = True
        print('Stopping Application')

    return isReset, isStop


def run_calculator():
    window_name = 'Virtual Calculator'
    cv2.namedWindow(window_name, cv2.WINDOW_FREERATIO)
    roi = [(0, 0), (600, 600)]

    model_path = "./models/hand_gesture_model.h5"
    model = keras.models.load_model(model_path)
    previous_gesture = 'empty'
    threshold = 0.7
    number1_list = []
    number2_list = []
    isNumber1Received = False
    operator = ''
    isOperator1Received = False

    videoSource = 0
    cap = cv2.VideoCapture(videoSource)

    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                isReset, isStop = check_for_reset_stop(frame)
                if isStop:
                    break
                if isReset:
                    number1_list.clear()
                    number2_list.clear()
                    operator = ''

                cropped_gray_frame = preprocess_frame(frame, roi)

                cv2.rectangle(frame, roi[0], roi[1], (255, 255, 0), 2, 16)
                classified_gesture, score = recognize_hand_gesture(cropped_gray_frame, model)

                if score > threshold:
                    process_gestures_and_perform_calculations(frame, classified_gesture, number1_list, operator, number2_list, previous_gesture, isNumber1Received, isOperator1Received)

                cv2.imshow(window_name, frame)
                k = cv2.waitKey(1)
                if k == 27 or k == ord('q'):
                    break

            else:
                print("ERROR: Stopping the application since capture object cannot provide any frame")
    else:
        print("ERROR: Cannot open Video Source")


if __name__ == "__main__":
    run_calculator()

