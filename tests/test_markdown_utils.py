import pytest

from meraid_gantts.markdown_utils import update_markdown


def test_update_markdown_runs(tmp_path):
    # This test checks that update_markdown can be called without error
    test_file = tmp_path / "test.md"
    test_file.write_text("")
    try:
        update_markdown(str(test_file), [{'Task': 'Test', 'Start': '2023-01-01', 'End': '2023-01-10'}])
    except Exception as e:
        pytest.fail(f"update_markdown raised an exception: {e}")