## Virtru Technical Assignment: Python

### Getting Started

This project is intended to demonstrate a test automation framework in Python but can be easily setup in a variety of
programming languages. A test automation framework should be configurable and customizable, allow organizing and
executing tests by group, and have a robust logging mechanism.

### Tech Stack

The Virtru Technical Assignment project is built with the following set of technologies:

* **Pip**: Lifecycle and dependency management
* **Python**: Programming language
* **Selenium**: Web driver automation

### System Requirements

Python is required in order to install dependencies and run the script. You can download
it [here](https://www.python.org/downloads/). To test the installation, run the following commands:

**Mac/Linux:**

```bash
python3 --version; pip3 --version
```

**Windows:**

```
py --version & pip3 --version
```

If `py` does not work but `pip3` does, rerun the command with:

```
python --version & pip3 --version
```

### Installation

All required dependencies can be installed by running the following command from the `scripts` directory:

**Mac/Linux:**

```bash
./setup.sh
```

**Windows:**

```
setup.bat
```

If errors regarding an "externally-managed-environment" occur during setup, pass `--break-system-packages` as a
parameter to the script. Example:

**Mac/Linux:**

```bash
./setup.sh --break-system-packages
```

**Windows:**

```
setup.bat --break-system-packages
```

### Setup

The Virtru Technical Assignment project is expecting two environment variables to be set in order to log into Gmail. You
can set these variables using a variety of methods, but the simplest method is to put them in a `.env` file in the
project root directory.

* **GMAIL_LOGIN_EMAIL**: The login email.
* **GMAIL_LOGIN_PASSWORD**: The login password.

### Running the Tests

To run a group of tests from the command line, use the `run-tests` script from the `scripts` directory.

**Mac/Linux:**

```bash
./run-tests.sh [group]
```

**Windows:**

```
run-tests.bat [group]
```

where `group` is the name or (names separated by a comma) of the group of tests you want to run. The following groups
are currently defined:

* **encryption**
* **gmail**
* **ui**

You can also run your tests in a GUI if your IDE supports it. 
