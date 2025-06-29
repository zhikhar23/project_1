
from unittest.mock import patch, mock_open
from src.csv_loader import loader


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_loader_empty_csv(mock_file):
    result = loader("empty.csv")
    assert result == []
    mock_file.assert_called_once_with("empty.csv")
