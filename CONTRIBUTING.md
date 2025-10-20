# Contributing to Directed Quantum Measurement (DQM)

Thank you for your interest in contributing to the Directed Quantum Measurement project! This is an active research initiative exploring the boundaries of quantum measurement theory.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Development Setup](#development-setup)
4. [Submission Guidelines](#submission-guidelines)
5. [Style Guidelines](#style-guidelines)
6. [Research Contributions](#research-contributions)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful in all interactions.

### Expected Behavior

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive criticism
- Acknowledge contributions from others
- Engage in scientific discourse with open-mindedness

---

## How Can I Contribute?

### 1. Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and environment details
- Error messages (if any)

### 2. Suggesting Enhancements

We welcome suggestions for:
- New experimental implementations
- Theoretical extensions
- Documentation improvements
- Performance optimizations
- Educational materials

### 3. Code Contributions

Areas where contributions are particularly welcome:
- **Experimental Implementations**: New quantum circuits or measurement protocols
- **Theoretical Analysis**: Mathematical formulations and proofs
- **Hardware Optimization**: Improvements for specific quantum backends
- **Visualization Tools**: Better ways to display results
- **Documentation**: Tutorials, examples, and explanations
- **Testing**: Unit tests and validation experiments

### 4. Research Contributions

If you conduct experiments or develop theoretical extensions:
- Document your methodology clearly
- Include code and data when possible
- Reference the original DQM framework
- Submit findings via pull request or issue discussion

---

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/Directed-Quantum-Measurement-DQM.git
cd Directed-Quantum-Measurement-DQM
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

### 3. Set Up Environment

```bash
# Create virtual environment
python -m venv dqm-env

# Activate it
# Windows:
.\dqm-env\Scripts\Activate.ps1
# Linux/macOS:
source dqm-env/bin/activate

# Install dependencies
pip install -r requirements_dqm.txt
```

### 4. Make Your Changes

- Write clear, commented code
- Follow existing code style
- Add docstrings to functions
- Include examples where helpful

### 5. Test Your Changes

```bash
# Run your new code
python your_new_script.py

# Test with different parameters
# Verify on local simulator before IBM backends
```

---

## Submission Guidelines

### Pull Request Process

1. **Update Documentation**
   - Add your changes to README.md if relevant
   - Update SETUP.md if installation changes
   - Include docstrings in code

2. **Commit Messages**
   - Use clear, descriptive commit messages
   - Reference issues when applicable
   - Examples:
     - `Add new entanglement preservation experiment`
     - `Fix bug in directional_field calculation (#42)`
     - `Update README with new theoretical section`

3. **Pull Request Description**
   - Explain what changes you made and why
   - Reference any related issues
   - Include screenshots for visual changes
   - Describe how you tested the changes

4. **Code Review**
   - Be open to feedback
   - Respond to review comments
   - Make requested changes promptly

### What to Include

✅ **Do Include:**
- Clear code comments
- Docstrings for functions
- Example usage
- References to scientific literature (if applicable)
- Test results or output examples

❌ **Don't Include:**
- API tokens or credentials
- Personal configuration files
- Large binary files
- Unrelated changes

---

## Style Guidelines

### Python Code Style

Follow PEP 8 with these specifics:

```python
# Function naming: lowercase with underscores
def directional_field(theta, phi):
    """
    Calculate the directional quantum field value.
    
    Args:
        theta (float): Angular parameter in radians
        phi (float): Angular parameter in radians
    
    Returns:
        float: Bias value between 0 and 1
    """
    return 0.5 + 0.5 * sin(theta) * cos(phi)

# Constants: UPPERCASE
MAX_SHOTS = 1024
DEFAULT_THETA = pi / 3

# Class naming: CamelCase
class QuantumMeasurementSimulator:
    pass
```

### Documentation Style

- Use clear, concise language
- Include mathematical notation when needed (LaTeX/KaTeX)
- Provide examples for complex concepts
- Link to relevant papers or resources

### Commit Style

```
Type: Brief description (50 chars max)

Longer explanation if needed. Explain what and why,
not how (the code shows how).

- Bullet points for multiple changes
- Reference issues: Fixes #123
```

**Types:** `Add`, `Fix`, `Update`, `Remove`, `Refactor`, `Docs`

---

## Research Contributions

### Theoretical Work

If contributing theoretical analysis:

1. **Mathematical Rigor**
   - Provide clear derivations
   - State assumptions explicitly
   - Include proofs when applicable

2. **References**
   - Cite relevant literature
   - Use standard citation format
   - Link to papers (arXiv, DOI)

3. **Documentation**
   - Explain concepts clearly
   - Use both mathematical and intuitive descriptions
   - Include diagrams if helpful

### Experimental Work

If contributing experimental results:

1. **Methodology**
   - Describe experimental setup
   - Document parameters used
   - Explain measurement protocol

2. **Data**
   - Include raw data when possible
   - Provide analysis code
   - Show visualizations

3. **Reproducibility**
   - Clear instructions to reproduce
   - Specify hardware/software versions
   - Document any special requirements

### Peer Review

For theoretical contributions:
- Open issues for discussion before major changes
- Be receptive to critique
- Engage in scientific debate respectfully
- Acknowledge limitations and assumptions

---

## File Organization

When adding new files:

```
Directed Quantum Measurement/
├── experiments/           # New experiment implementations
│   └── your_experiment.py
├── theory/               # Theoretical analysis
│   └── your_theory.md
├── docs/                 # Additional documentation
│   └── your_tutorial.md
└── tests/                # Test files
    └── test_your_code.py
```

---

## Questions?

- **Issues**: For bugs and feature requests
- **Discussions**: For questions and ideas
- **Email**: For sensitive matters or collaboration inquiries

---

## Recognition

Contributors will be acknowledged in:
- README.md Contributors section
- CHANGELOG.md for each release
- Academic papers (for significant theoretical contributions)

---

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to DQM! Together we're exploring the frontiers of quantum measurement theory.** 🚀

*OMARINO Quantum Research Initiative*
