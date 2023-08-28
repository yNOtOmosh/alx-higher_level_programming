
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    try:
        for j in range(x):
            if isinstance(my_list[j], int):
                print("{:d}".format(my_list[j]), end='')
                printed_integers += 1
    except (ValueError, TypeError):
        pass
    finally:
        print()

    return (printed_integers)
