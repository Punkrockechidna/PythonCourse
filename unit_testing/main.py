def do_stuff(num):
    # int(num) and try block added after initial test to make better code/prevent errors/better test
    # added if to make sure a number is added
    try:
        if num:
            return int(num) + 5
        elif num == 0:
            return 'Please enter number that is not 0'
        else:
            return 'Please enter number'
    except ValueError as err:
        return err