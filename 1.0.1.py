import time,sys, openpyxl
from accessability import pwint as print, line_pwint as line_print, inpwut as input, check_type as types, print_dic_list as list_dic
# Load the Excel file
wb = openpyxl.load_workbook('/Users/newenoch/Documents/Visual Studio Code/Minecraft (Buttons)/Version 1/1.0/1.0.1/Mine_speed 1.0.1.xlsx')
sheet = wb.active  # Select the first sheet

# Create an empty dictionary to store the mine speeds
mine_speeds = {}

# Iterate over the rows in the sheet
for row in range(2, sheet.max_row + 1):  # Assuming the first row is a header
    block_type = sheet.cell(row=row, column=1).value
    default_speed = sheet.cell(row=row, column=4).value
    mine_speeds[block_type] = {}
    mine_speeds[block_type]['default'] = default_speed
    
    # Get the tool speeds for the block type
    for col in range(5, 13):  # Columns 5-12
        tool_type = sheet.cell(row=1, column=col).value
        speed = sheet.cell(row=row, column=col).value
        
        # If the speed is a dash, set it to the default speed
        if speed == '-':
            speed = default_speed
        
        mine_speeds[block_type][tool_type] = speed

mine_list = {0: "Back to previous menu"}
for row in range(2, sheet.max_row + 1):  # Assuming the first row is a header
    block_type = sheet.cell(row=row, column=1).value
    if block_type not in [None, ""]:
        mine_list[len(mine_list)] = block_type

inventory = {key: 0 for key in mine_list if key != 0}
#upgrades (with durability in 1.0.4)

def mine_choice(parent=None):
    print('\n\n\n\n\n\n\n\n\n-----------------    Mining menu    -----------------\n\n\n\n\n\n\n\n\n')
    while True:
        try:
            print('\n')
            list_dic(mine_list)
            choice = input("Choose which block to mine, or type 0 to go back to the previous menu:\n")
            choice = types(choice, int, "Invalid input! Please enter a valid number.\n")
            if choice == 0:
                if parent is not None:
                    parent()
                else:
                    break
            elif choice in mine_list:
                # Make a mining screen with moving dots
                dots = ['.', '..', '...']
                total_time = mine_speeds[mine_list[choice]]['default']
                delay = total_time / len(dots)
                length_of_mining_line = len(f"\rMining {mine_list[choice]} {dots[0]}")
                delay = delay / length_of_mining_line
                for dot in dots:
                    print(f"\rMining {mine_list[choice]} {dot}", delay)
                # Add the block to the inventory and announce successful mining
                inventory[choice] += 1
                print(f"\nYou have mined {mine_list[choice]}!")
            else:
                print("Invalid input!")
        except Exception as e:
            print(f"Invalid input, {e}! at line {sys.exc_info()[-1].tb_lineno}")

def show_inventory():
    print("\nYour current inventory is:\n")
    for key, value in inventory.items():
        if key != 0:
            block_type = mine_list[key]
            line_print(f"{block_type}: {value}")

def ui():
    print("Welcome to your world!")
    while True:
        try:
            main_choice = input("Choose your action:\n1. Mine\n2. Craft\n3. Show inventory\n4. Quit\n")
            main_choice = types(main_choice, int, 'Choose your action:\n1. Mine\n2. Craft\n3. Show inventory\n4. Quit\n')
            if main_choice == 1:
                mine_choice(ui)
            elif main_choice == 2:
                craft_choice(ui)
            elif main_choice == 3:
                show_inventory()
            elif main_choice == 4:
                sys.exit()
        except NameError:
            print("That's a function soon to be implemented!")
        except Exception:
            print("Invalid input! Enter the number!")
ui()

