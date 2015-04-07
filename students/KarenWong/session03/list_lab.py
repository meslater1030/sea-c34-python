#!/usr/bin/env python


def main():
    fruits_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print fruits_list
    add_fruit = raw_input(u'what fruit do you want to add to '
                          'the end of the list? ')
    fruits_list.append(add_fruit)
    print fruits_list

    user_has_answer = False
    while user_has_answer is False:
        ask_number = raw_input(u'Pick a number and I will display '
                               'the fruit that corresponds to that number ')
        ask_number_value = int(ask_number)
        if ask_number_value > 0 and ask_number_value <= len(fruits_list):
            print fruits_list[ask_number_value - 1]
            user_has_answer = True

    fruits_list = ['Kiwi'] + fruits_list
    print fruits_list
    fruits_list.insert(0, 'Pineapple')
    print fruits_list
    for fruit in fruits_list:
        if fruit.startswith('p') or fruit.startswith('P'):
            print fruit
# second series of the assignment
    print fruits_list
    fruits_list.pop(6)
    print fruits_list
    user_has_answer = False
    while user_has_answer is False:
        delete_fruit = raw_input(u'Please pick a fruit to delete!')
        if delete_fruit in fruits_list:
            fruits_list.remove(delete_fruit)
            print fruits_list
            user_has_answer = True
# third series of the assignment
    for fruit in fruits_list[:]:
        user_has_answer = False
        while user_has_answer is False:
            ask_preference = raw_input(u'Do you like ' + fruit.lower() + '? ')
            if ask_preference == "Yes" or ask_preference == "yes":
                user_has_answer = True
            elif ask_preference == "No" or ask_preference == "no":
                fruits_list.remove(fruit)
                user_has_answer = True
    print fruits_list
# fourth series of the assignment
    fruits_list_copy = fruits_list[:]
    for idx, fruit in enumerate(fruits_list):
        fruits_list_copy[idx] = fruit[::-1]
    fruits_list.pop()
    print fruits_list
    print fruits_list_copy
if __name__ == '__main__':
    main()
