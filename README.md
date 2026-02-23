# Advanced Programming (2025-2026) 🎓

Welcome to my repository for the **Advanced Programming** university course (Year 1, Semester 2). 

This repository serves as a personal archive for my coursework, containing practice solutions, algorithmic exercises, and Jupyter Notebook histories throughout the semester.

## 📁 Repository Structure

* **`Jupyter Projects/`**: Contains the main coursework, structured as interactive Jupyter Notebooks (`.ipynb`).
  * `practice1_exercises.ipynb`: Initial practice covering fundamental Python operations, string manipulation, and introductory algorithm design.
* **`.gitignore`**: Configured to keep the repository clean by ignoring local virtual environments (like `.venv`) and other system files.

## 🧠 Topics & Algorithms Covered

Based on the practice exercises, this repository explores:
* **Python Fundamentals**: List comprehensions, list manipulations (indexing, reversing), and understanding item-wise vs. object equality (`==` vs `is`).
* **String Manipulation**: Palindrome checking and naive pattern matching (brute-force substring search).
* **Algorithmic Problem Solving**:
  * **Largest Zero-Sum Sublist**: Solved efficiently using Dictionaries/Hash Maps and Prefix Sums.
  * **Merging Overlapping Intervals**: Solved by sorting and dynamically updating tuple boundaries.

## 🛠️ Local Setup & Installation

To run these notebooks locally, it is recommended to use a Conda environment to ensure dependency isolation. 

**1. Clone the repository**
```bash
git clone [https://github.com/mapi-developer/advanced-programming--2025-2026-.git](https://github.com/mapi-developer/advanced-programming--2025-2026-.git)
cd "Advanced-Programming--2025-2026--main"
```

**2. Create a local Conda environment**
This project uses a local .venv folder for the Python environment. Ensure you have Conda installed and added to your system PATH.
```bash
conda create --prefix ./.venv python=3.10 ipykernel
```

**3. Activate the environment**
```bash
conda activate ./.venv
```

**4. Running in VS Code**
* Open the repository in Visual Studio Code.
* Open any .ipynb file in the Jupyter Projects/ directory.
* Click Select Kernel in the top right corner.
* Choose Python Environments and select the local (.venv) environment.

**📝 License / Usage**

This is a personal university repository created for educational purposes. Feel free to explore the algorithmic solutions!
