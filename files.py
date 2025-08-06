def read_and_modify_file():
   
    filename = input("Enter the name of the file to read: ")

    try:
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(" File read successfully!")

        modified_content = content.upper()

        new_filename = "modified_file.txt"


        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)
            print(f" Modified content saved to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except IOError:
        print("❌ Error reading or writing the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


read_and_modify_file()
