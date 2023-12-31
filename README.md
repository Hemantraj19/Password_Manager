# Password Manager Application

This is a simple password manager application built using Python and Tkinter. It allows users to generate secure passwords, save them along with website and email details, and retrieve passwords when needed.

## Features

- **Password Generation:** Click the "Generate Password" button to create a strong and random password.
- **Save Passwords:** Enter website, username, and password details and click the "Add" button to save them securely.
- **Search Passwords:** Use the "Search" button to find and display saved passwords for a specific website.
- **Data Storage:** Passwords are stored in a JSON file (`data.json`).
- **User Interface:** The application provides a user-friendly interface with entry fields, buttons, and a logo.

## How to Use

1. Run the script using a Python interpreter.
2. Enter the website, username, and password details.
3. Click the "Generate Password" button if you want the application to generate a password for you.
4. Click the "Add" button to save the entered details.
5. To retrieve a password, enter the website name and click the "Search" button.

## Dependencies

- `tkinter`: Python's standard GUI (Graphical User Interface) package.
- `pyperclip`: A clipboard copy and paste Python module.

## Files

- `main.py`: The main Python script containing the password manager application code.
- `logo.png`: The logo used in the application.
- `data.json`: JSON file to store saved passwords.

## Running the Application

Make sure you have Python installed on your system. Run the following command in the terminal or command prompt:

```bash
python main.py
