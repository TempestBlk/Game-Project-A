class Menu():
    def option_menu(title, option_list):
        print(f"\n[{title}]")
        valid_input = []
        option_dict = {}
        counter = 1
        for option in option_list:
            valid_input.append(str(counter))
            if hasattr(option, 'hp'): # if option has hp, probably entity
                name = option.get_name()
                print(f"{counter}: {name}")
                # command = ''.join([w[0] for w in name.split()]).lower()
                # option_dict[command] = counter
            elif isinstance(option, dict): # if option is dict, probably atk
                print(f"{counter}: {option['name']}")
                # command = ''.join([w[0] for w in option['name'].split()]).lower()
                # option_dict[command] = counter
            else:
                print(f"{counter}: {option}")
                # command = ''.join([w[0] for w in option.split()]).lower()
                # option_dict[command] = counter
            counter += 1
        user_input = None
        # for key in option_dict:
        #     valid_input.append(key)
        while user_input not in valid_input:
            user_input = input("> ").lower().strip(" ")
        # if re.search('[a-zA-Z]', user_input):
        #     user_input = option_dict[user_input]
        return int(user_input)
