# TODO реализовать функцию delete удаления элемента из списка по индексу
def delete(list_, index=None):
    #  Почему нельзя просто параметрах написать index=-1?
    if index is None:
        list_ = list_[:-1]
    else:
        list_ = list_[0:index] + list_[index+1:]
    return(list_)



print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
