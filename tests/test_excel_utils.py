
import pandas as pd
import pytest

from meraid_gantts.excel_utils import load_data
from meraid_gantts.export_to_msproject import export_gantt_to_msproject_excel


def test_load_data_returns_list():
    # This test assumes a sample Excel file exists with at least one row
    # You may need to create 'sample_input.xlsx' with appropriate columns for a real test
    try:
        data = load_data('sample_input.xlsx')
        assert isinstance(data, list)
    except FileNotFoundError:
        pytest.skip('sample_input.xlsx not found')


def test_export_gantt_to_msproject_excel(tmp_path, monkeypatch):
    # Create a fake markdown file with a simple Gantt chart
    markdown_content = """
    # Gantt Chart
    gantt
        title Example
        dateFormat  YYYY-MM-DD
        section Section
        Task 1 :t1, 2023-01-01, 5d
        Task 2 :after t1, 2023-01-06, 3d
    """
    md_file = tmp_path / "gantt.md"
    md_file.write_text(markdown_content)
    excel_file = tmp_path / "output.xlsx"

    # Patch parse_gantt_chart to return a known structure
    def fake_parse_gantt_chart(content):
        return [
            {'Task Name': 'Task 1', 'Start Date': '2023-01-01', 'Duration': '5d', 'Depends On': '', 'End Date': '2023-01-05'},
            {'Task Name': 'Task 2', 'Start Date': '2023-01-06', 'Duration': '3d', 'Depends On': 't1', 'End Date': '2023-01-08'},
        ]
    monkeypatch.setattr('meraid_gantts.gantt_parser.parse_gantt_chart', fake_parse_gantt_chart)

    export_gantt_to_msproject_excel(str(md_file), str(excel_file))
    # Check that the Excel file was created and has expected columns
    df = pd.read_excel(excel_file)
    assert 'Task Name' in df.columns
    assert 'Start' in df.columns
    assert 'Finish' in df.columns
    assert 'Duration' in df.columns
    assert 'Predecessors' in df.columns
    assert len(df) == 2