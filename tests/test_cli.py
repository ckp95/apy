"""Test the CLI"""
from apy.cli import main
from click.testing import CliRunner
import tempfile
import shutil

test_collection_dir = "tests/data/test_base"

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