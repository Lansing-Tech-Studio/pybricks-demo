from menu import Menu, demo_function_1, demo_function_2, demo_function_3

if __name__ == "__main__":
    menu = Menu()
    
    menu.add_item(1, demo_function_1)
    menu.add_item(5, demo_function_2) 
    menu.add_item(10, demo_function_3)
    
    menu.run(auto_increment=True)
