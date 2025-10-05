"""Creates badge and formats"""
import json
import os
import subprocess

def get_score(pylintrc=None):
    """Runs Pyint and returns the score.

    Args:
        pylintrc (_type_, optional): The pylintrc config file. Defaults to None.

    Returns:
        score: The PyLint score.
    """

    # Run PyLint and get the score
    command = ["pylint"]
    if pylintrc:
        command.append(f"--rcfile={pylintrc}")
    
    command += ["git", "ls-files", "*.py"]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False
    )

    for line in result.stdout.splitlines():
        print(line)
        if "Your code has been rated at" in line:
            score = line.split("at")[1].split("/")[0].strip()

            try:
                return float(score)
            except ValueError:
                return 0.0

    return 0.0

def get_color(score, perfect, good, ok, bad):
    """Gets color for badge and returns it.

    Args:
        score (_type_): Score of PyLint.
        perfect (_type_): Perfect color.
        good (_type_): Good color.
        ok (_type_): Ok color.
        bad (_type_): Bad color.

    Returns:
        _type_: Color of badge.
    """
    if score == 10:
        return perfect

    if score >= 8:
        return good

    if score >= 5:
        return ok

    return bad

def main():
    """Generates badge and writes in desired folder.
    """
    # Environment information
    github_repository = os.environ.get("GITHUB_REPOSITORY", "")
    user, repo = github_repository.split("/")
    branch = os.environ.get("GITHUB_REF_NAME", "main")

    # Badge configuration
    badge_text = os.environ.get("BADGE_TEXT", "Pylint")
    pylintrc_file = os.environ.get("PYLINTRC_FILE", None)
    perfect_score = os.environ.get("PERFECT_SCORE", "brightgreen")
    good_score = os.environ.get("GOOD_SCORE", "yellow")
    ok_score = os.environ.get("OK_SCORE", "orange")
    bad_score = os.environ.get("BAD_SCORE", "red")

    # Run PyLint
    score = get_score(pylintrc_file)
    color = get_color(score, perfect_score, good_score, ok_score, bad_score)

    badge_data = {
        "schemaVersion": 1,
        "label": badge_text,
        "message": f"{score:.2f}",
        "color": color
    }

    # Write badge JSON
    dir_path = os.path.join("badges", user, repo, branch)
    os.makedirs(dir_path, exist_ok=True)
    badge_path = os.path.join(dir_path, "pylint-badge.json")

    with open(badge_path, "w", encoding="utf-8") as f:
        json.dump(badge_data, f, indent=2)

    print("PyLint badge has been created successfully!")

if __name__ == "__main__":
    main()
