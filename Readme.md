# Rule Engine with AST in Python

## Overview
This project implements a 3-tier Rule Engine using Python's Abstract Syntax Tree (AST) to evaluate user eligibility based on custom conditions.

## Features
- Dynamically create, combine, and evaluate rules.
- Supports logical operations (`and`, `or`) and comparisons (`>`, `<`, `==`).
- Efficient evaluation using Python's `ast` module.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd RuleEngineProject
   ```

2. **Run tests:**
   ```bash
   python -m unittest test_engine.py
   ```

## Example Usage

Sample rule:
Sample data:
```json
{
  "age": 35,
  "department": "Sales",
  "salary": 60000,
  "experience": 3
}

---

### 2. **Additional Features (Optional Enhancements)**  
Consider adding more features if you want to push your skills further.

1. **Modify Existing Rules**  
- Add a feature to allow modification of existing rules.
- Example: Update operators, add conditions, or remove expressions from the AST.

2. **UI for Rule Creation**  
- Create a **simple web-based UI** (using Flask or Django) where users can create and modify rules dynamically.

3. **Database Integration**  
- Store rules and user data in a **SQLite** or **PostgreSQL** database.
- Example schema:
  - **Rules Table**: ID, Rule String
  - **Users Table**: ID, Attributes (age, department, salary, etc.)

4. **Error Handling and Validation**  
- Implement detailed error handling for invalid rules.
- Validate user data against a pre-defined catalog (e.g., `department` should only accept `Sales`, `Marketing`, etc.).

---

### 3. **Version Control & Deployment**  
- **Upload to GitHub**:  
- Initialize a git repository in your project directory:
  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  git branch -M main
  git remote add origin <your-repo-url>
  git push -u origin main
  ```

- **Deployment Options**:  
- If you built a UI, consider deploying it on **Heroku**, **Render**, or **PythonAnywhere**.

---

### 4. **Explore CI/CD with GitHub Actions (Optional)**
- Automate running tests on every commit with **GitHub Actions**.
- Example `.github/workflows/python-app.yml`:

  ```yaml
  name: Python application

  on: [push]

  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: python -m unittest discover
  ```

---

### 5. **Project Submission or Portfolio Addition**
- If this is part of a **course project** or **internship**, you can now:
  - Submit your work with clear instructions on running and testing it.
  - Add the project to your **portfolio** to showcase your skills in Python, rule engines, and AST manipulation.

---

## **What’s Next for You?**
- **Learn Flask/Django**: If you're interested in building web applications.
- **Deepen your knowledge of AST and parsers**: Explore advanced AST manipulation techniques.
- **Explore Machine Learning**: You could extend this rule engine with predictive models (e.g., automatically suggesting rules).

---

Let me know if you want more help with any of these steps or need ideas for further enhancements! 🚀😊
