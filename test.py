"""Test that templated project builds successfully."""
import unittest
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
import os


class TestCookiecutterTemplate(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).parent
        self.temp_dir = TemporaryDirectory()
        self.project_dir = Path(self.temp_dir.name) / "newproject"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_make_command(self):
        # Invoke cookiecutter template
        subprocess.run(["cookiecutter", "--no-input", "-o", self.temp_dir.name, str(self.repo_root)], check=True)

        # Change directory to the new project
        os.chdir(self.project_dir)

        # Run make command
        result = subprocess.run("make", check=True)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
