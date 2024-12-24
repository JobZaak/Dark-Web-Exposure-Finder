# Dark Web Exposure Finder

A Python-based GUI tool designed to help users check if their email address has been exposed in known data breaches. This tool uses a local breach dataset for analysis and provides results in a user-friendly interface.

---

## Features

- **Email Input**: Allows users to enter an email address for checking.
- **Hashing Mechanism**: Uses SHA1 hashing to protect email privacy during breach checks.
- **Breach Search**: Scans a local dataset of breaches to determine if the email is compromised.
- **User-Friendly Output**: Provides detailed information on breaches, including source and date.
- **Clear Results**: Offers an option to clear output for multiple checks.

---

## How It Works

1. **Input Email**: Enter the email address in the provided input field.
2. **Check Breach**:
   - Click the "Check Breach" button.
   - The tool hashes the email and searches for it in the local `breach_dataset.txt` file.
3. **View Results**: Displays breach status, source, and date if found.
4. **Clear Output**: Click the "Clear Output" button to reset the result area.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dark-web-exposure-finder.git
   ```
2. Navigate to the project directory:
   ```bash
   cd dark-web-exposure-finder
   ```
3. Ensure Python is installed on your system.
4. Install required libraries (if needed):
   ```bash
   pip install tkinter
   ```
5. Place your breach dataset file (`breach_dataset.txt`) in the project directory.
6. Run the tool:
   ```bash
   python dark_web_finder.py
   ```

---

## Dataset Format

The breach dataset (`breach_dataset.txt`) should follow this format:
```csv
hashed_email,source,date
```
Example:
```csv
d7a8fbb307d7809469ca9abcb0082e4f9f9966b6,example.com,2024-01-01
```

---

## Screenshots





## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

- Built with a focus on enhancing cybersecurity awareness.
- Special thanks to data breach intelligence contributors.
