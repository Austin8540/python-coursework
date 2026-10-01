# Python Coursework

Python programs I wrote while learning the language, covering object-oriented design, input validation, and error handling. Each program runs from the command line with no outside libraries.

## Programs

### [Gradebook](gradebook/gradebook.py)
A command-line gradebook for managing a course. It stores students and grade items keyed by unique IDs, rejects duplicate student IDs and grade items, enforces valid grade ranges (0 to the item's total points), and keeps running when the user enters bad input.

**Concepts:** classes working together (`Student`, `GradeItem`, `Course`), dictionaries as lookup tables, data validation, exception handling

```
python gradebook/gradebook.py
```

### [Steps to Miles](steps-to-miles/steps_to_miles.py)
Converts a step count to miles walked. Rejects non-numeric input and negative values with clear error messages, using a custom exception class.

**Concepts:** custom exceptions, input validation, `if __name__ == "__main__"` structure

```
python steps-to-miles/steps_to_miles.py
```

### [Scrabble Score](scrabble-score/scrabble_score.py)
Calculates the Scrabble point value of any word the user enters, using a dictionary of letter values.

**Concepts:** dictionary lookups, generator expressions, input loops

```
python scrabble-score/scrabble_score.py
```

## Requirements
Python 3.8 or newer.
