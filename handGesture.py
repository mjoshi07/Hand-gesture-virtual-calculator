from keras.preprocessing import image
from utils import *


hand_gesture_list = ['/', '+', '-', '0', '1', '2', '3', '4', '5', 'empty', 'x']


def perform_calculation(number1, number2, operator_character):

    output = 0

    if operator_character == '+':
        output = number1 + number2
    elif operator_character == '-':
        output = number1 - number2
    elif operator_character == 'x':
        output = number1 * number2
    elif operator_character == '/':
        output = number1 / number2

    return output


def is_classified_gesture_number(classified_gesture):
    if classified_gesture in hand_gesture_list[3:10]:
        return True
    else:
        return False


def process_gestures_and_perform_calculations(frame, classified_gesture, number1_list, operator, number2_list, previous_gesture, isNumber1Received, isOperator1Received):
    if is_classified_gesture_number(classified_gesture):
        if classified_gesture != 'empty':
            if not isNumber1Received:
                if len(number1_list) == 0 and previous_gesture == 'empty':
                    number1_list.append(classified_gesture)
                    display_message(classified_gesture, frame)
            else:
                if len(number2_list) == 0 and previous_gesture == 'empty':
                    number2_list.append(classified_gesture)
                    display_message(classified_gesture, frame)
            previous_gesture = classified_gesture
        else:
            previous_gesture = 'empty'
    elif not isOperator1Received:
        if len(number1_list):
            operator = classified_gesture
            isNumber1Received = True
            isOperator1Received = True
            previous_gesture = 'empty'
            message_to_display = 'operator: ' + operator
            display_message(message_to_display, frame)
    elif len(number2_list):
        number1 = int(get_number_from_list(number1_list))
        number2 = int(get_number_from_list(number2_list))
        output = perform_calculation(number1, number2, operator)
        message_to_display = "{} {} {} is equal to {}".format(number1, operator, number2, output)
        display_message(message_to_display, frame)
        number1_list.clear()
        number2_list.clear()
        operator = ''


def recognize_hand_gesture(gray_img, model):

    gray_img_resized = cv2.resize(gray_img, (100, 100))
    gray_img_normalized = gray_img_resized / 255
    x = image.img_to_array(gray_img_normalized)
    x = np.expand_dims(x, axis=0)
    prediction = model.predict(x)
    max_score_index = np.argmax(prediction[0])
    max_score = prediction[0][max_score_index]
    max_score_class = hand_gesture_list[max_score_index]

    return max_score_class, max_score


