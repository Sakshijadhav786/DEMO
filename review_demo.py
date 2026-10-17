from pathlib import Path
from typing import List, Tuple


def calculate_student_marks(filepath: str) -> Tuple[int, float]:
    """
    Reads marks from a file and calculates the total and average.

    Args:
        filepath: Path to the text file containing integer marks per line.

    Returns:
        A tuple containing (total_marks, average_marks).

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file contains non-integer data or is empty.
    """
    path = Path(filepath)

    if not path.is_file():
        raise FileNotFoundError(f"The file '{filepath}' was not found.")

    marks: List[int] = []

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            stripped_line = line.strip()
            
            # Skip empty lines
            if not stripped_line:
                continue
                
            try:
                marks.append(int(stripped_line))
            except ValueError as e:
                raise ValueError(f"Invalid data on line {line_number}: '{stripped_line}' is not an integer.") from e

    if not marks:
        raise ValueError("The file contains no valid marks to calculate.")

    total = sum(marks)
    average = total / len(marks)

    return total, average


def main() -> None:
    """Entry point for the script."""
    target_file = "marks.txt"
    
    try:
        total, average = calculate_student_marks(target_file)
        print(f"Total Marks:   {total}")
        print(f"Average Marks: {average:.2f}")
    except FileNotFoundError as e:
        print(f"File Error: {e}")
    except ValueError as e:
        print(f"Data Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()