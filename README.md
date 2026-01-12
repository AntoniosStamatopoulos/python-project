# Word Guessing Game (Python)

A command-line word guessing game inspired by Wordle, implemented in Python.
The game randomly selects a 5-letter word and allows the player to guess it within a limited number of attempts.

Two difficulty modes are available: Normal and Hard.

---

## Game Modes

### Normal Mode
- The player has 6 attempts to guess the word.
- Feedback is provided for each guess:
  - `O` indicates a correct letter in the correct position
  - `X` indicates a correct letter in the wrong position
  - `-` indicates a letter not present in the word
- Displays:
  - letters already used
  - letters not present in the secret word
  - remaining available letters

### Hard Mode
- Same rules as Normal Mode, with additional constraints.
- The player cannot reuse letters that are known not to exist in the secret word.
- Invalid guesses are detected and reported.

---

## Features
- Random word selection from a word list
- Input validation (word length, invalid letters)
- Multiple difficulty modes
- Clear visual feedback for guesses
- Greek alphabet support (uppercase letters)

---

## Project Structure

