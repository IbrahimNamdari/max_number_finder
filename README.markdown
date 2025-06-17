# Max Number Finder

A simple Python program that takes two numbers from the user and displays the larger one. This project is designed for users of all skill levels, showcases basic Python skills, with clean code, clear explanations, and error handling.

## Features

- Takes two numbers as input.
- Determines and displays the larger number.
- Checks that inputs are valid numbers (including decimals and negatives).
- After completion, allows the user to choose to compare another pair of numbers or exit.
- Handles errors so the program doesn’t crash if you make a mistake.
- Follows Python’s professional standards (PEP 8).
- Uses comments, explanations, and messages, which is standard for clean code.

## Requirements

- Python 3.6 or higher is required.
- An internet connection is needed to download the project from GitHub.
- For more details, see the `requirements.txt` file.

## How to Install

This section explains how to install and set up the Max Number Finder project on your computer, even if you are new to programming or using the command line. Follow these steps carefully:

### Prerequisites

- Python 3.6 or higher is required.
- An internet connection is needed to download the project from GitHub.

### Step-by-Step Installation

1. **Download the Project**:
   - **Option 1: Using Git (if installed)**:
     - Open a Command Prompt (Windows) or Terminal (Mac/Linux).
     - If you have Git installed (check by typing `git --version`), download the project by running:
       ```bash
       git clone https://github.com/IbrahimNamdari/max_number_finder.git
       ```
     - This creates a folder named `max_number_finder` on your computer.
   - **Option 2: Manual Download (no Git required)**:
     - Open a web browser and go to `https://github.com/IbrahimNamdari/max_number_finder`.
     - Click the green **Code** button, then select **Download ZIP**.
     - Save the ZIP file to a location on your computer (e.g., `E:\Python`).
     - Extract the ZIP file using your system’s built-in tools:
       - On Windows: Right-click the ZIP file, select **Extract All**, and choose a destination (e.g., `E:\Python`).
       - On Mac/Linux: Double-click the ZIP file or use the `unzip` command.
     - After extraction, you’ll have a folder named `max_number_finder-main` or similar.

2. **Navigate to the Project Folder**:
   - Open a Command Prompt (Windows) or Terminal (Mac/Linux).
   - Use the `cd` command to move to the project folder. For example, if you extracted the project to `E:\...\max_number_finder`, follow these steps:
     ```
     Microsoft Windows [Version ...]
     (c) Microsoft Corporation. All rights reserved.

     C:\Users\<your-username>>E:
     E:\>cd Python
     E:\Python>cd max_number_finder
     E:\...\max_number_finder>
     ```
     - **Explanation**:
       - `C:\Users\<your-username>>E:` switches to the E: drive.
       - `cd Python` enters the `Python` folder.
       - `cd max_number_finder` enters the project folder.
     - If you downloaded the ZIP, the folder might be named `max_number_finder-main`. Adjust the command accordingly (e.g., `cd max_number_finder-main`).
     - To verify you’re in the correct folder, type `dir` (Windows) or `ls` (Mac/Linux) and press Enter. You should see `main.py` listed.

3. **Run the Program**:
   - In the Command Prompt or Terminal, while inside the project folder (e.g., `E:\...\max_number_finder`), type:
     ```bash
     python main.py
     ```
     - On some systems (e.g., Mac/Linux), you may need to use:
       ```bash
       python3 main.py
       ```
   - The program will start and display: `Max Number Finder is RUNNING`.

### Troubleshooting Installation
- **If `python` or `python3` doesn’t work**:
  - Ensure Python is installed (check with `python --version`).
  - If you get "command not found," reinstall Python and ensure "Add Python to PATH" is checked during installation (Windows).
- **If the folder or file isn’t found**:
  - Double-check the folder name and path. Use `dir` (Windows) or `ls` (Mac/Linux) to list files and verify `main.py` exists.
- **If you get errors when running the program**:
  - Ensure you’re in the correct folder (containing `main.py`).
  - Contact the author (see Author section) with the error message for help.

## How to Run

This section explains how to use the Max Number Finder program after installation. The program is simple and interactive, designed for users of all skill levels.

### How to Use the Program

1. **Start the Program**:
   - Ensure you’re in the project folder (e.g., `E:\...\max_number_finder`) in your Command Prompt or Terminal.
   - Run the program by typing:
     ```bash
     python main.py
     ```
     - On Mac/Linux, you may need:
       ```bash
       python3 main.py
       ```
   - The program will start and display: `Max Number Finder is RUNNING`.

2. **Enter Two Numbers**:
   - When prompted, type the first number (e.g., `5`, `3.5`, `-2`) and press Enter.
   - Repeat for the second number.
   - Example:
     ```
     Enter the first number: 5
     Enter the second number: 3
     ```

3. **View the Result**:
   - The program displays the entered numbers and the larger one, all with two decimal places.

   - **Example output**:
     ```
     E:\...\max_number_finder>python main.py

     Max Number Finder is RUNNING
     Please Enter Two Numbers to Compare
     
     Enter the first number: 5
     Enter the second number: 3

     First Number: 5.00
     Second Number: 3.00
     Larger Number: 5.00
     
     E:\...\max_number_finder>
     ```
   - If you enter invalid input (e.g., letters), the program will display an error, such as:
     ```
     Error: Please enter a valid number.
     ```

4. **Run Again**:
   - To use the program again, repeat step 1 (run `python main.py`).
   - You can close the Command Prompt or Terminal when done.

### Usage Tips
- Enter numbers, including decimals (e.g., `2.5`) or negative numbers (e.g., `-10`).
- If you make a mistake, the program won’t crash and will ask for valid input.
- To continue comparing, enter `yes` or `y`. To stop, enter `no` or `n`, or press `Ctrl+C`, which will display: `Program terminated by user.`

### If You Get Errors

- If you enter letters (e.g., "abc"), it says: "Error: Please enter a valid number."
- If you enter an invalid choice for continuing, it says: "Error: Please enter 'yes(y)' or 'no(n)'."
- If you stop the program, it says: "Program terminated/stopped by user."

## License

This project is licensed under the MIT License. See `LICENSE.txt` for details.

## Author

- Ibrahim Namdari
  - LinkedIn: [Ibrahim Namdari](https://www.linkedin.com/in/ibrahim-namdari-7a0a7a208/)
  - GitHub: [IbrahimNamdari](https://github.com/IbrahimNamdari/)
  - Email: ibrahimnamdari1999@yahoo.com

## Questions?

If anything in the code or project is unclear, open an Issue on GitHub or email me!