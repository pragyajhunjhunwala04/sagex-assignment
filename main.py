import os
import processing
import chat

def list_csv_files():
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return files

def choose_from_list(options, prompt):
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    while True:
        choice = input(prompt)
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print("Invalid choice. Please try again.")

def main():
    csv_files = list_csv_files()
    if not csv_files:
        print("No CSV files found in the current directory.")
        return

    print("Available CSV files:")
    selected_csv = choose_from_list(csv_files, "Select a CSV file by number: ")

    new_column = input("Enter the name of the new column you would like to add: ").strip()
    if not new_column:
        print("Column name cannot be empty.")
        return

    print(f"You selected '{selected_csv}' and want to add a new column named '{new_column}'.")

    print("Please provide a transformation prompt for the new column:")
    transformation_prompt = chat.process_transformation_prompt(input("Transformation prompt: ").strip())
    
    df = processing.read_csv(selected_csv)
    df = processing.add_column_to_csv(df, new_column)
    df = processing.process_csv_with_gemini(df, new_column, transformation_prompt)

    print(f"Transformation successful! The new column '{new_column}' has been added to '{selected_csv}' according to your transformation prompt!")

if __name__ == "__main__":
    main()