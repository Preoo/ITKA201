"""
Implement binarytree walking operations, tree creation can be done by hand

>>> pre_order(construct_tree(), '')
'HCABEDFJLK'

>>> in_order(construct_tree(), '')
'ABCDEFHJKL'

>>> post_order(construct_tree(), '')
'BADFECKLJH'

"""

def construct_tree():
    return {
            'value': 'H',
            'left': {
                'value': 'C',
                'left': {
                    'value': 'A',
                    'right': {
                        'value': 'B'
                    }
                },
                'right': {
                    'value': 'E',
                    'left': {
                        'value': 'D'
                    },
                    'right': {
                        'value': 'F'
                    }
                }
            },
            'right': {
                'value': 'J',
                'right': {
                    'value' : 'L',
                    'left': {
                        'value': 'K'
                    }
                }
            }
        }

def pre_order(sub_tree:dict, print_values:str) -> str:
    if sub_tree:
        print_values += sub_tree['value']
        print_values = pre_order(sub_tree.get('left', None), print_values)
        print_values = pre_order(sub_tree.get('right', None), print_values)

    return print_values

def in_order(sub_tree:dict, print_values:str) -> str:
    if sub_tree:
        print_values = in_order(sub_tree.get('left', None), print_values)
        print_values += sub_tree['value']
        print_values = in_order(sub_tree.get('right', None), print_values)

    return print_values

def post_order(sub_tree:dict, print_values:str) -> str:
    if sub_tree:
        print_values = post_order(sub_tree.get('left', None), print_values)
        print_values = post_order(sub_tree.get('right', None), print_values)
        print_values += sub_tree['value']

    return print_values

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)