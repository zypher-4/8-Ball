import random
import os.path

pred = []
user_dir = False


def import_default():
    with open('./Database/Predictions-Default.txt', encoding='utf-8') as pred_default:
        for temp_pred in pred_default:
            pred.append(temp_pred)


def import_user():
    global user_dir
    if os.path.exists('./Database/Predictions-User.txt'):
        with open('./Database/Predictions-User.txt', encoding='utf-8') as pred_default:
            for temp_pred in pred_default:
                pred.append(temp_pred)
        user_dir = True
        return
    else:
        user_dir = False
        return


def create_user():
    global user_dir
    if user_dir == False:
        temp = open('./Database/Predictions-User.txt', 'w', encoding='utf-8')
        temp.close()


def check_user():
    global user_dir
    if os.path.exists('./Database/Predictions-User.txt'):
        user_dir = True


def add_pred(user_pred):
    global user_dir
    if user_dir:
        with open('./Database/Predictions-User.txt', 'a', encoding='utf-8') as pred_default:
            pred_default.writelines(user_pred + '\n')
    else:
        create_user()
        with open('./Database/Predictions-User.txt', 'a', encoding='utf-8') as pred_default:
            pred_default.writelines(user_pred + '\n')


def make_pred(temp_pred=pred):
    return random.choice(temp_pred)


def print_pred(temp_pred=pred):
    for temp in temp_pred:
        print(temp)


import_default()
check_user()
if user_dir:
    import_user()
else:
    create_user()


if __name__ == '__main__':

    print('Welcome to this 8Ball Application.')

    print('Would you like to add your custom predictions now? (Y/N) ')

    user_input = input()
    while True:
        if user_input == 'y' or user_input == 'Y':
            user_pred = input('Enter the prediction you would like to add. ')
            add_pred(user_pred)
            user_input = input(
                'Would you like to add another prediction? (Y/N) ')
            if user_input == 'n' or user_input == 'N':
                break
        else:
            break
