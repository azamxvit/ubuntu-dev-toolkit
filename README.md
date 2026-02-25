# Ubuntu Dev Toolkit (ubutool)

![Status](https://img.shields.io/badge/status-active_development-success)
![Tech](https://img.shields.io/badge/stack-Python_3.12_|_Poetry_|_Click_|_Rich-blue)

Hello everyone! A modern, professional CLI utility acting as a "Swiss Army knife" for Ubuntu developers. This tool automates the repetitive tasks of setting up a new Linux environment, monitoring system resources, and analyzing package dependencies directly from the terminal. 

## 🚀 Key Features

* Automated Environment Setup: Quickly bootstrap a fresh Ubuntu installation with essential developer tools (Git, curl, build-essential) via a single command.
* Modern Terminal UI: Built with rich to provide a beautiful, colorful, and highly readable terminal interface with visual feedback (spinners, success/error indicators).
* Component-Based Architecture: Highly modular design separating CLI routing, business logic (components), and system utilities, making it highly scalable.
* Modern Python Tooling: Managed entirely via Poetry with a strict pyproject.toml configuration, moving away from legacy requirements.txt.
* Robust Error Handling: Safely wraps bash commands (`subprocess`) with try/except blocks, providing clear, color-coded error messages instead of raw tracebacks.
* Fully Tested: Includes automated CLI command testing using pytest and click.testing.

## 🛠 Tech Stack

* Core: Python 3.12+
* Package Manager & Build Tool: Poetry
* CLI Framework: Click
* Terminal UI: Rich
* Code Quality & Testing: Pytest, Flake8, Black

## ⚙️ Getting Started

1. Clone the repository
     git clone [https://github.com/azamxvit/ubuntu-dev-toolkit.git](https://github.com/azamxvit/ubuntu-dev-toolkit.git)
   cd ubuntu-dev-toolkit
   
2. Install dependencies using Poetry
   If you don't have Poetry installed, install it via pip install poetry.
     poetry install
   
3. Run the toolkit
   Access the main help menu to see all available commands:
     poetry run ubutool --help
   
## 💻 Available Commands

* Setup Environment:
   poetry run ubutool setup
    *Updates apt packages and installs core developer tools.*

* System Monitor (WIP):
   poetry run ubutool monitor
    *Will display real-time CPU, RAM, and Network usage with smart recommendations.*

* Dependency Analyzer (WIP):
   poetry run ubutool deps <package_name>
    *Will build and display a dependency tree for the specified Ubuntu package.*

## 🏗 Architecture & Decisions

* Strict `src` Layout: All code resides within the src/ directory to prevent namespace collisions and enforce proper package installation.
* Isolated `utils/shell.py`: Encapsulates the subprocess logic. This completely decouples the CLI interface from the underlying OS-level command execution, allowing for safer execution and easier mocking during tests.
* Component Segregation: The application is split into setup, monitor, and package_deps. Each module handles its own specific domain logic independently of the cli entry point.
* Dunder Block Entry: Uses standard Python if __name__ == '__main__': pattern for safe execution when invoked directly.

## 🎥 Demo

*(Coming soon!)*