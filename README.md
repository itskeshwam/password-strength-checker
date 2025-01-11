# Password Strength Checker

A Python-based GUI application that provides real-time password strength analysis with visual feedback.

## Features

- Real-time password strength evaluation
- Visual strength indicator with progress bar
- Detailed feedback and suggestions for improvement
- Multiple strength criteria analysis
- Color-coded strength levels
- User-friendly interface

## Requirements

- Python 3.x
- tkinter (usually comes bundled with Python)

## Installation

1. Ensure Python 3.x is installed on your system
2. Download the `password_checker.py` file
3. No additional package installation is required as the application uses built-in Python libraries

```bash
# Clone the repository (if using git)
git clone https://github.com/itskeshwam/password-strength-checker
# Navigate to the project directory
cd password-strength-checker

# Run the application
python password_checker.py
```

## Usage

1. Run the script using Python:
```bash
python password_checker.py
```

2. The application window will appear with:
   - Password input field
   - Strength indicator
   - Progress bar
   - Feedback section

3. Type your password in the input field and receive real-time feedback on:
   - Overall strength rating (Weak to Perfect)
   - Specific improvements needed
   - Progress towards a strong password

## Password Strength Criteria

The application evaluates passwords based on:

1. **Length**: Minimum 8 characters
2. **Character Variety**:
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Special characters
3. **Common Patterns**: Checks for and warns against:
   - Sequential characters
   - Repeated characters
   - Common passwords
   - Keyboard patterns
4. **Entropy**: Additional score for high entropy passwords

## Strength Levels

- **Weak** (0-40%): Red - Basic password needing significant improvement
- **Moderate** (41-60%): Orange - Better but needs improvement
- **Strong** (61-80%): Blue - Good password meeting basic requirements
- **Very Strong** (81-90%): Green - Excellent password
- **Perfect** (91-100%): Dark Green - Exceptional password meeting all criteria

## Contributing

Feel free to fork this project and submit pull requests for any improvements you'd like to add. Some areas for potential enhancement:

- Additional password strength criteria
- Enhanced UI design
- More detailed feedback
- Password generation suggestions
- Support for different languages
- Configuration options for criteria weights

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please:
1. Open an issue in the GitHub repository
2. Contact the maintainer
3. Submit a pull request with proposed changes

## Author

Keshwam Pandey

## Version History

- 1.0.0 (2025-01-11)
  - Initial release
  - Basic password strength checking
  - Real-time feedback system
  - GUI interface
