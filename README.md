# Word Guess Desktop

A simple word guessing game for desktop, with multi-language support.

## Features

*   Simple and intuitive UI.
*   Multi-language support (English, Arabic, German, French).
*   Easily customizable word lists.

## How to Play

1.  Run the game.
2.  A secret word is chosen from the word list.
3.  Guess letters one by one.
4.  If you guess a correct letter, it will be revealed.
5.  If you guess a wrong letter, you will lose a try.
6.  You win if you guess the word before you run out of tries.
7.  You lose if you run out of tries before you guess the word.

## Development

### Prerequisites

*   Python 3.x
*   Tkinter

### Running the game

```bash
python src/main.py
```

### Word Lists

The word lists are located in the `words/` directory. Each file is a plain text file with one word per line, encoded in UTF-8.

*   `words/en.txt`: English
*   `words/ar.txt`: Arabic
*   `words/de.txt`: German
*   `words/fr.txt`: French

**Note on Arabic Support:** For correct rendering of Arabic text, it is recommended to use a font that supports Arabic script (e.g., Amiri, Noto Naskh Arabic).

## Packaging

This project can be packaged into a standalone executable using PyInstaller.

### Installation

```bash
pip install pyinstaller
```

### Building the executable

```bash
pyinstaller --onefile --windowed src/main.py
```

The executable will be created in the `dist/` directory.

## Future Ideas

*   Scoring system
*   Hints
*   Online leaderboards
*   More UI complexity (e.g., settings screen)
