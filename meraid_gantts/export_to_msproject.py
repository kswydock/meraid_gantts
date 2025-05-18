
import pandas as pd

from meraid_gantts.gantt_parser import parse_gantt_chart


def export_gantt_to_msproject_csv(markdown_path, output_csv_path):
    """
    Parse a Gantt chart from a markdown file and export it as a CSV suitable for Microsoft Project import.

    Args:
        markdown_path (str or Path): Path to the markdown file containing the Gantt chart.
        output_csv_path (str or Path): Path to the output CSV file.
    """
    with open(markdown_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    gantt_data = parse_gantt_chart(markdown_content)
    if not gantt_data:
        raise ValueError("No Gantt chart data found in the markdown file.")

    df = pd.DataFrame(gantt_data)

    # Expanded column mapping for MS Project import (same as Excel)
    column_map = {
        'Task Name': 'Name',              # MS Project expects 'Name'
        'Task ID': 'ID',                  # Optional, for unique task IDs
        'Section': 'Outline Level',       # Can be mapped to outline level or summary task
        'Start Date': 'Start',            # Start date
        'End Date': 'Finish',             # Finish date
        'Duration': 'Duration',           # Duration
        'Depends On': 'Predecessors',     # Predecessors (dependencies)
        'Tags (active, done, crit, milestone)': 'Text1',  # Custom text field for tags
        'Is Milestone': 'Milestone',      # TRUE/FALSE for milestone
        'Is Done': 'Complete',            # % Complete or TRUE/FALSE
        'Notes': 'Notes',                 # Notes
    }
    df = df.rename(columns={k: v for k, v in column_map.items() if k in df.columns})

    # MS Project expects 'Milestone' as 1/0, and 'Complete' as percent or 1/0
    if 'Milestone' in df.columns:
        df['Milestone'] = df['Milestone'].apply(lambda x: 1 if str(x).strip().upper() == 'TRUE' else 0)
    if 'Complete' in df.columns:
        df['Complete'] = df['Complete'].apply(lambda x: 100 if str(x).strip().upper() == 'TRUE' else 0)

    # Save as CSV
    df.to_csv(output_csv_path, index=False)
    print(f"Exported Gantt chart to {output_csv_path}")


def export_gantt_to_msproject_excel(markdown_path, output_excel_path):
    """
    Parse a Gantt chart from a markdown file and export it as an Excel file suitable for Microsoft Project import.

    Args:
        markdown_path (str or Path): Path to the markdown file containing the Gantt chart.
        output_excel_path (str or Path): Path to the output Excel file.
    """
    with open(markdown_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    gantt_data = parse_gantt_chart(markdown_content)
    if not gantt_data:
        raise ValueError("No Gantt chart data found in the markdown file.")

    df = pd.DataFrame(gantt_data)

    # Expanded column mapping for MS Project import
    column_map = {
        'Task Name': 'Name',              # MS Project expects 'Name'
        'Task ID': 'ID',                  # Optional, for unique task IDs
        'Section': 'Outline Level',       # Can be mapped to outline level or summary task
        'Start Date': 'Start',            # Start date
        'End Date': 'Finish',             # Finish date
        'Duration': 'Duration',           # Duration
        'Depends On': 'Predecessors',     # Predecessors (dependencies)
        'Tags (active, done, crit, milestone)': 'Text1',  # Custom text field for tags
        'Is Milestone': 'Milestone',      # TRUE/FALSE for milestone
        'Is Done': 'Complete',            # % Complete or TRUE/FALSE
        'Notes': 'Notes',                 # Notes
    }
    # Only rename columns that exist in the DataFrame
    df = df.rename(columns={k: v for k, v in column_map.items() if k in df.columns})

    # MS Project expects 'Milestone' as 1/0, and 'Complete' as percent or 1/0
    if 'Milestone' in df.columns:
        df['Milestone'] = df['Milestone'].apply(lambda x: 1 if str(x).strip().upper() == 'TRUE' else 0)
    if 'Complete' in df.columns:
        df['Complete'] = df['Complete'].apply(lambda x: 100 if str(x).strip().upper() == 'TRUE' else 0)

    # Save as Excel
    df.to_excel(output_excel_path, index=False)
    print(f"Exported Gantt chart to {output_excel_path}")
