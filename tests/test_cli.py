from click.testing import CliRunner
from cli.main import cli

def test_setup_command():
    """Test the setup command"""
    runner = CliRunner()
    result = runner.invoke(cli, ['setup'])
    assert result.exit_code == 0
    assert "Starting setup module" in result.output

def test_monitor_command():
    """Test the monitor command"""
    runner = CliRunner()
    result = runner.invoke(cli, ['monitor'])
    assert result.exit_code == 0
    assert "Starting monitoring" in result.output