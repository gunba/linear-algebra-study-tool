Here's a GitHub README for the provided code in Markdown format:

---

# Linear Algebra Study Tool

This Python script generates prompts for an AI tutor based on specified difficulty levels. It filters a predefined list of linear algebra problem types and provides a problem scaled to the requested difficulty level. The generated prompt is copied to the clipboard for easy use.

## Features

- Generates problems from various mathematical categories.
- Scales problem difficulty to match the user's requested level.
- Copies the generated prompt to the clipboard.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gunba/linear-algebra-study-tool.git
   ```
2. Install the required Python packages:
   ```bash
   pip install pyperclip
   ```

## Usage

Run the script with the desired difficulty level as an argument:

```bash
python generate_prompt.py <difficulty_level>
```

### Example

```bash
python generate_prompt.py 50
```

This will generate a prompt for problems with a difficulty level up to 50/100.

## Code Overview

- `problems`: A predefined list of mathematical problems categorized by name, category, and difficulty.
- `generate_prompt(difficulty)`: Filters problems by the given difficulty level, selects a random problem, and generates a prompt for the AI tutor. The prompt is copied to the clipboard.
- Main script: Parses the command-line argument for difficulty level and generates the prompt.

## Dependencies

- `pyperclip`: A cross-platform Python module for clipboard operations. Install it using `pip install pyperclip`.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
