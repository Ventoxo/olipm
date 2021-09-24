# -*- coding: utf-8 -*-
# Owner: User <djakovatwork@gmail.com>

'''
main idea:lists in python are ordered mutable collections of objects of arbitrary types with cool methods.
so, i need to check this idea.
'''

check_list = [5, '2', 4.8, [19, 20], (3, '4')]


def test_list_index_error():
    '''
    Description: list is the collection with indexed elements

    Steps:
    1. create list with 5 elements [0, 1, 2, 3, 4]
    2. try to get 6 element

    Expectations:
    raise IndexError
    '''

    list_ = [0, 1, 2, 3, 4]
    try:
        assert list_[5]
    except IndexError:
        pass


def test_list_change_element(check_list):
    '''
    Description: list is the mutable collection

    Steps:
    1. create list with 5 elements [0, '1', 2.1, [0,1], (1,'2')]
    2. try to change every element on elements from check_list

    Expectations:
    list with elements = elements from check_list
    '''

    list_ = [0, '1', 2.1, [0, 1], (1, '2')]
    list_[0] = check_list[0]
    list_[1] = check_list[1]
    list_[2] = check_list[2]
    list_[3] = check_list[3]
    list_[4] = check_list[4]
    for el in list_:
        assert el in check_list
    assert list_ == check_list


def test_check_methods():
    '''
        Description: list has a lot of methods, test checks 3 of them, my choice based on use statistic

        Steps:
        1. create list with 5 elements [0, 1, 2, 3, 4]
        2. try to append element {5}
        3. try to pop
        4. try to sort list with reverse=True

        Expectations:
        1. after append list will be [0, 1, 2, 3, 4, 5]
        2. after pop list will be [0, 1, 2, 3, 4]
        3. after sort list will be [4, 3, 2, 1, 0]
    '''
    list_ = [0, 1, 2, 3, 4]

    list_.append(5)
    assert list_[-1] == 5

    assert list_.pop() == 5
    assert list_ == [0, 1, 2, 3, 4]

    list_.sort(reverse=True)
    assert list_ == [4, 3, 2, 1, 0]


'''
main idea: int in python - numeric type. we can do smt operations with it
so, i need to check this idea.
'''


def test_int_math():
    '''
            Description: we can math int object

            Steps:
            1. 3+3
            2. 3*3
            3. 3-3
            4. 3/3
            5. 6//3
              -10//3
            6. 6%3
               7%3
            7. 2 degree 3
            8. 7 negated
            9. -7 unnegated
            10. 2.7 convert to integer
            11. '3' convert to integer
            12. negative test: '2.7' convert to integer

            Expectations:
            1. 6
            2. 9
            3. 0
            4. 1
            5. 2
              -4
            6. 0
               2
            7. 8
            8. -7
            9. 7
            10. 2
            11. 3
            12. pass

        '''
    assert 3 + 3 == 6
    assert 3 * 3 == 9
    assert 3 - 3 == 0
    assert 3 / 3 == 1
    assert 6 // 3 == 2
    assert -10 // 3 == -4
    assert 6 % 3 == 0
    assert 7 % 3 == 1
    assert -7 % 3 == 2
    assert pow(2, 3) == 2 ** 3
    i = 7
    assert -i == -7
    assert +i == 7
    assert int(2.7) == 2
    assert int('3') == 3
    try:
        assert int('2.7')
    except ValueError:
        pass


def test_bitwise_int():
    '''
                Description: we can do bitwise operations with int

                Steps:
                1.  6 or 1
                    6 or 4
                2.  6 exclusive 4
                    6 exclusive 1
                3.  6 and 1
                    6 and 4
                4.  6 shifted left by 2
                5.  6 shifted right by 2
                    6 shifted right by 20
                6.  6 invert
                    -10 invert


                Expectations:
                1.  7
                    6
                2.  2
                    7
                3.  0
                    4
                4.  24
                5.  1
                    0
                6. -7
                    9

            '''
    assert 6 | 1 == 7
    assert 6 | 4 == 6
    assert 6 ^ 4 == 2
    assert 6 ^ 1 == 7
    assert 6 & 1 == 0
    assert 6 & 4 == 4
    assert 6 << 2 == 24
    assert 6 >> 2 == 1
    assert 6 >> 20 == 0
    assert ~6 == -7
    assert ~-10 == 9


integer = 6
def test_check_int(integer):
    '''
        Description: we need to know that is int

        Steps:
        1. check type of integer

        Expectations:
        type of integer == int
    '''
    assert type(integer) == int


