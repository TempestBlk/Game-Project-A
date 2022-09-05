class Menu():
    def display_menu(self, title, options):
        print(f"\n[ {title} ]")
        valid_input = []
        counter = 1
        for opt in options:
            print(f"{counter}: {opt}")
            valid_input.append(str(counter))
            counter += 1
        user_input = None
        while user_input not in valid_input:
            user_input = str(input("> ")).lower().strip(" ")
        return user_input
