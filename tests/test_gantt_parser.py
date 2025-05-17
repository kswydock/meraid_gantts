# Test Gantt Parser Module

import pytest

from meraid_gantts.gantt_parser import parse_gantt_chart


@pytest.fixture
def sample_markdown():
    return """
    # Gantt Chart
    gantt
        title A Gantt Diagram
        dateFormat  YYYY-MM-DD
        section Section
        A task           :a1, 2023-01-01, 30d
        Another task     :after a1  , 20d
        Task in sec      :2023-01-12  , 12d
    """


def test_parse_gantt_chart(sample_markdown):
    parsed_data = parse_gantt_chart(sample_markdown)
    assert isinstance(parsed_data, list)
    assert len(parsed_data) > 0