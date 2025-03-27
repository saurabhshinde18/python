import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("\nFile Content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except IOError:
        print(f"Error: Could not read the file at '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"\nSuccessfully wrote to '{file_path}'.")
    except IOError:
        print(f"Error: Could not write to the file at '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
            print(f"\nSuccessfully appended to '{file_path}'.")
    except IOError:
        print(f"Error: Could not append to the file at '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def check_if_file_exists(file_path):
    if os.path.exists(file_path):
        print(f"\nThe file '{file_path}' exists.")
    else:
        print(f"\nThe file '{file_path}' does not exist.")

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"\nSuccessfully deleted the file at '{file_path}'.")
        else:
            print(f"\nError: The file at '{file_path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to delete '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    file_path = "example.txt"
    
    while True:
        print("\nFile Handling Menu:")
        print("1. Read from file")
        print("2. Write to file")
        print("3. Append to file")
        print("4. Check if file exists")
        print("5. Delete file")
        print("6. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            read_file(file_path)
        elif choice == '2':
            content = input("Enter content to write to the file: ")
            write_to_file(file_path, content)
        elif choice == '3':
            content = input("Enter content to append to the file: ")
            append_to_file(file_path, content)
        elif choice == '4':
            check_if_file_exists(file_path)
        elif choice == '5':
            delete_file(file_path)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
