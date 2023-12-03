import operator


def reverse_sort_dictionary(dict_reverse):
    old_dict = dict(sorted(dict_reverse.items(), reverse=True))

    return old_dict
