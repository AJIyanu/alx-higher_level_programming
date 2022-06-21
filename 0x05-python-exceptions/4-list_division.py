#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    divide = []
    for x in range(list_length):
        try:
            divide.append(my_list_1[x] / my_list_2[x])
        except IndexError:
            print("out of range")
            divide.append(0)
        except TypeError:
            print("wrong type")
            divide.append(0)
        except ZeroDivisionError:
            print("division by 0")
            divide.append(0)
        finally:
            continue
    return (divide)
