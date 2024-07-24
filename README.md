# WordSearchMaster
An interactive word search game developed in Python using the Tkinter library. This project illustrates random matrix generation and the Knuth-Morris-Pratt (KMP) string matching algorithm. Ideal for learning Python GUI integration and search algorithm implementation in an engaging way.

## Features

- Generates a 10x10 matrix of random uppercase letters.
- Allows users to search for words horizontally, vertically, and diagonally.
- Highlights the found words within the matrix.
- Utilizes the Knuth-Morris-Pratt (KMP) algorithm for efficient string matching.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## How to Run

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/WordSearchMaster.git
    ```
2. Navigate to the project directory:
    ```sh
    cd WordSearchMaster
    ```
3. Run the game:
    ```sh
    python word_search_master.py
    ```

## Code Overview

- `WordFinderGame`: The main class that initializes the game, populates the matrix, and handles user interactions.
- `populate_matrix`: Populates the matrix with random uppercase letters.
- `create_widgets`: Creates the Tkinter widgets (canvas and search button).
- `draw_matrix`: Draws the letter matrix on the canvas.
- `start_search`: Prompts the user to enter a word and searches for it in the matrix.
- `search_word`: Searches for the word horizontally, vertically, and diagonally using the KMP algorithm.
- `kmp_search`: Implements the Knuth-Morris-Pratt string matching algorithm.
- `highlight_found_cells`: Highlights the cells of the found word in the matrix.
- `clear_highlights`: Clears any previous highlights from the matrix.

## Future Enhancements

- Add support for searching words in reverse directions.
- Enhance the user interface with improved graphics.
- Incorporate a scoring system to track user performance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
