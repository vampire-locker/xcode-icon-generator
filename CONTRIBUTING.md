# Contributing to Batch Resize Icon for Xcode

First off, thank you for considering contributing to this project! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: How to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**:
  - Python version
  - Pillow version
  - Operating system
- **Screenshots**: If applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:

- **Clear title**: Summarize the enhancement
- **Detailed description**: Explain the feature and why it would be useful
- **Use cases**: Provide examples of how it would be used

### Pull Requests

1. **Fork** the repository
2. **Create a branch** for your feature (`git checkout -b feature/AmazingFeature`)
3. **Make your changes**
4. **Test your changes** thoroughly
5. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
6. **Push** to the branch (`git push origin feature/AmazingFeature`)
7. **Open a Pull Request**

#### Pull Request Guidelines

- Keep changes focused - one feature/fix per PR
- Follow the existing code style (PEP 8)
- Add comments for complex logic
- Update documentation if needed
- Test your changes with various input images

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/your-username/BatchResizePicForXcode.git
cd BatchResizePicForXcode
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Make your changes and test:
```bash
python batch_resize_icon.py test_icon.png -v
```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints where appropriate
- Write clear, descriptive variable and function names
- Add docstrings for classes and functions

## Testing

Before submitting a PR, please test with:

- Valid 1024×1024 PNG images
- Non-1024 sized images with `--auto-scale`
- Images without transparency
- JPG/JPEG formats
- Invalid inputs (wrong size, wrong format, etc.)

## Questions?

Feel free to create an issue for any questions or discussions.

Thank you for contributing! 🙏
