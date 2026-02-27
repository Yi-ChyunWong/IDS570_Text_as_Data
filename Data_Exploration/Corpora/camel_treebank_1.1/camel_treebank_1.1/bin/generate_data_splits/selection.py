
def print_options(subcorpora):
    for i, subcorpus in enumerate(subcorpora, 1):
        print(f'{i}: {subcorpus}')
    
def get_choices(subcorpora, extra_options):
    print('Please select the desired subocrpus to be split:')
    print_options(subcorpora + extra_options)
    while True:
        try:
            choice = int(input())
            if choice in range(1, len(subcorpora) + 3):
                break
            print('invalid choice! Please select a choice from the options below')
            print_options(subcorpora + extra_options)
        except ValueError as ve:
            print(ve)
            print('Please select a choice from the options below')
            print_options(subcorpora + extra_options)
    if choice < len(subcorpora) + 1:
        choices = [subcorpora[choice - 1]]
        save_each = True
        save_all = False
    elif choice == 14:
        choices = subcorpora
        save_each = False
        save_all = True
    elif choice == 15:
        choices = subcorpora
        save_each = True
        save_all = True

    return choices, save_each, save_all