![PyLint Score](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/devs-des1re/pylint-badge-action/badges/badges/devs-des1re/pylint-badge-action/main/pylint-badge.json)

# PyLint Badge Action
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

Using Github Actions, I have created a workflow, which creates a badge for your repository, showing the score for PyLint. This is so that your developers, or viewers know what your code is like, so they can improve from it!

| Score Description           | Badge                                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Perfect Score:** Score = 10 | ![Perfect Score](https://img.shields.io/badge/Pylint-10.00-brightgreen?logo=python&logoColor=white) |
| **Good Score:** 8 ≤ Score < 10 | ![Good Score](https://img.shields.io/badge/Pylint-8.32-yellow?logo=python&logoColor=white) |
| **Ok Score:** 5 ≤ Score < 8 | ![Ok Score](https://img.shields.io/badge/Pylint-6.92-orange?logo=python&logoColor=white) |
| **Bad Score:** Score < 5 | ![Bad Score](https://img.shields.io/badge/Pylint-3.64-red?logo=python&logoColor=white) |


# Workflow
To be able to generate your badge, you need to use the workflow provided.
You are able to change some of the settings to your preference so that you are satisfied with your badge.

## Inputs
Inputs are like parameters but for workflows, so that you can customize how yours works.

### gk-token
- Used for publishing your badge.
- **Required:** true (although its not directly passed)

### python-version
- The Python version you want to lint on.
- **Required:** true

### requirements-file
- The dependencies file for Python to install.  
- **Default:** `none`
- **Required:** false

### pylintrc-file
- The path to your custom **PyLint configuration file**.  
- **Default:** `None`
- **Required:** false

### badge-text
- The text to display on the badge (e.g., “PyLint”).  
- **Default:** `PyLint`
- **Required:** false

### perfect-score
- The **badge color** when the PyLint score is exactly `10`.  
- **Default:** `brightgreen` 
- **Required:** false

### good-score
- The **badge color** when the PyLint score is between `8` and `10`.  
- **Default:** `yellow`
- **Required:** false

### ok-score
- The **badge color** when the PyLint score is between `5` and `8`.  
- **Default:** `orange`
- **Required:** false

### bad-score
- The **badge color** when the PyLint score is below `5`.  
- **Default:** `red`
- **Required:** false

## Template

```yaml
name: PyLint Badge Workflow
permissions:
  contents: write

on: [push]

jobs:
  pylint-badge:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Generate PyLint Badge
        uses: devs-des1re/pylint-badge-action@v1
        with: # Add your inputs below
          python-version: "3.11"
```

## Notes
- To use your badge, use the link provided, and edit it to your preferences
```
https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/devs-des1re/pylint-badge-action/badges/badges/<USERNAME>/<REPOSITORY NAME>/<BRANCH NAME>/pylint-badge.json
```
- When **changing** the color of the badge, you can use **HEX**, **RGB** , **RGBA**, **HSL**, **HSLA**, and **CSS**

# Credits
This is a composite Github Action, which uses the following...
- [actions/checkout](https://github.com/actions/checkout)
- [actions/setup-python](https://github.com/actions/setup-python)

Credits also go to [Silleellie](https://github.com/Silleellie/pylint-github-action) for the idea & [shields.io](https://shields.io/) for creating the badge!

# Contributing
Do you want to contribute? If you have found and bugs, or brainstormed any ideas, **first check** if it has not already been mentioned. This clears up `Issues` so that its easier to read and manage.