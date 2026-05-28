# tests_py

Simple programs being tested using pytest.



## Repository Structure

```text
├── euclidian_dif/
│   ├── micode.py          # Calculates the Euclidean distance between two points.
│   └── test_micode.py     # Unit tests for the distance calculator.
└── pswrd_check/
    ├── passwort.py        # Script to validate password strength based on specific rules.
    └── test_passwort.py   # Unit tests for the password validator.
```

## Features

### 1. Distance Calculator

Calculates the Euclidean distance between two points in a 2D space.

- **Core Script:** `micode.py`
- **Input:** Coordinates for **Point 1** `(x1, y1)` and **Point 2** `(x2, y2)`
- **Formula:**

$$d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$


### 2. Password Validator

Validates whether a password meets a set of specific security criteria.

- **Core Script:** `passwort.py`
- **Validation criteria:**
  - At least **8 characters** long
  - Contains at least one **uppercase letter**
  - Contains at least one **lowercase letter**
  - Contains at least one **digit**
  - Contains **no whitespace** characters

## Getting Started

### Prerequisites

- **Python 3.x** — [Download here](https://www.python.org/downloads/)
- **pytest** — Install via pip:

```bash
pip install pytest
```



### Running the Programs

**Distance Calculator:**

```bash
cd euclidian_dif
python micode.py
```

**Password Validator:**

```bash
cd pswrd_check
python passwort.py
```


## Running Tests

pytest automatically discovers all test files in subdirectories — no extra configuration needed.

**Run all tests at once:**

```bash
pytest
```

**Run tests for each module individually:**

```bash
# into euclidian_dif dir only
pytest distance_calculator/

# into pswrd_check dir only
pytest test_passwort/
```
