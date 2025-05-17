import pytest

from meraid_gantts.excel_utils import load_data


def test_load_data_returns_list():
    # This test assumes a sample Excel file exists with at least one row
    # You may need to create 'sample_input.xlsx' with appropriate columns for a real test
    try:
        data = load_data('sample_input.xlsx')
        assert isinstance(data, list)
    except FileNotFoundError:
        pytest.skip('sample_input.xlsx not found')