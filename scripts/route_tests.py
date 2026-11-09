import sys
import subprocess
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Map source files to their corresponding test files
TEST_MAPPING = {
    "src/auth.py": "tests/test_auth.py",
    "src/cart.py": "tests/test_cart.py",
    "src/inventory.py": "tests/test_inventory.py",
    "src/pricing.py": "tests/test_pricing.py",
}

def route_tests(changed_files):
    # If no files are provided, run the complete test suite
    if not changed_files:
        print("No changed files provided. Running all tests.")
        return ["tests"]

    selected_tests = set()

    for file in changed_files:
        normalized_file = file.replace("\\", "/").lower()

        if normalized_file in TEST_MAPPING:
            selected_tests.add(TEST_MAPPING[normalized_file])
        else:
            print(f"Unknown file: {file}")
            print("Running all tests as a safe fallback.")
            return ["tests"]

    return sorted(selected_tests)


if __name__ == "__main__":
    changed_files = sys.argv[1:]
    selected_tests = route_tests(changed_files)

    print("\nSelected test files:")
    for test in selected_tests:
        print(f"- {test}")

    print("\nRunning selected tests...\n")

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-v"] + selected_tests,
        cwd=PROJECT_ROOT
    )

    sys.exit(result.returncode)