# Pi Memorizer

Pi Memorizer is a fun and educational Python application that allows you to test your memory by entering the digits of the mathematical constant π (pi) up to a thousand decimal places.

## Features

- Enter the digits of π to test your memory.
- The application checks your input and provides real-time feedback.
- Keep track of the number of digits entered correctly.
- Option to clear your progress at any time and reset the digit count. (recommended for memorization)
- The application automatically saves your progress when you exit.

## Getting Started

1. Make sure you have Python installed on your computer.
2. Clone or download this repository to your local machine.
3. Run the `pi.py` script to launch the Pi Memorizer application.

## How to Play

- Enter the digits of π in the input field (can input multiple at once).
- The application will display real-time feedback on the correctness of your input.
- The digit count displayed on the counter label increases with each correct entry.
- You can use the "Clear Progress" checkbox to reset progress on each failed digit.
- When you exit the application, your progress will be automatically saved for the next session.

## Customization

- You can customize the color scheme of the application by modifying the `bg_color`, `text_color`, and `button_color` variables in the code.
- The minimum size of the application window can be adjusted by modifying the `self.master.minsize` method call.

## Dependencies

- This application is built using the Tkinter library, which is included with Python.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author

- Ian Sabolik

Enjoy testing your memory and learning more digits of π with Pi Memorizer!
