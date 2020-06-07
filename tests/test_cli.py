"""Test the CLI"""
import pytest
from apy.cli import main
from click.testing import CliRunner
import tempfile
import shutil

test_data_dir = "tests/data/"
test_collection_dir = test_data_dir + "test_base/"

def test_cli_base_directory():    
    runner = CliRunner()
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        # should fail when given base directory is invalid ...
        result = runner.invoke(main, ["-b", tmpdirname])
        assert result.exit_code != 0
        
        # ... and succeed when it is valid
        shutil.copytree(test_collection_dir, tmpdirname, dirs_exist_ok=True)
        result = runner.invoke(main, ["-b", tmpdirname])
        assert result.exit_code == 0

test_markdown_files = [
    # add files here that apy should be able to use
    # add-from-file on successfully
    "basic.md",
    "empty.md",
]

@pytest.mark.parametrize("notes_filename",
                         [test_data_dir + i for i in test_markdown_files])
def test_cli_add_from_file(notes_filename):
    runner = CliRunner()
    
    with tempfile.TemporaryDirectory() as tmpdirname:      
        shutil.copytree(test_collection_dir, tmpdirname, dirs_exist_ok=True)
        result = runner.invoke(main, ["-b", tmpdirname, "add-from-file", notes_filename])
        
        assert result.exit_code == 0