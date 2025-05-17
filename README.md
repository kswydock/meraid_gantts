# Mermaid Gantt Chart Creation and Update

## Description

This project is intended to allow a user to use excel to create or update a mermaid gantt chart stored in a markdown file. Below are the requirements to properly define the project. 

## Requirements

1. A user will be asked to select an input excel file.
2. The user will then be asked to select the file that the gantt chart should be added to or where the current gantt chart is that will be updated.
3. The Gantt Chart will need to be under a specific header of the markdown file to make it easy to identify.
4. The code needs to assess if the input excel file items are already in the gantt chart and update them if dates have been changed or not.
5. The code needs to add new line items into the gantt chart if the ones in the input file are not found in an existing chart.
6. If no Gantt Chart is found in the user's selected markdown file, the code will need to add it to the file. It is okay if the chart is just appended to the bottom of the file and then a user can move it after the code is finished.
7. I would like the copilot to help develop what the input columns should be for the input file. There are multiple options like "is this a milestone?" or "Is this task done?" that a user should be able to add values to to properly update an existing chart.
8. I would like the code to also be able to generate an input excel file from an existing gantt chart so that a user can easily modify the entries in the excel file and then run the code to update the chart. (This is particulary useful for large gantt charts)
8. Tests should be written to test the code to ensure consistent gantt chart creation and updates.

## Excel Input Format for Mermaid Gantt Chart

Below is the recommended input format for the Excel file. Each row represents a task or milestone in the Gantt chart. The columns are based on the [Mermaid Gantt Docs](https://mermaid.js.org/syntax/gantt.html) and project requirements.

| Task Name      | Task ID | Section   | Start Date  | Duration | End Date   | Depends On | Tags (active, done, crit, milestone) | Is Milestone | Is Done | Notes           |
|---------------|---------|-----------|-------------|----------|------------|------------|--------------------------------------|--------------|---------|-----------------|
| Design Phase  | d1      | Planning  | 2023-01-01  | 10d      |            |            | active                               |              |         | Initial design  |
| Dev Phase     | dev1    | Execution | 2023-01-11  | 20d      |            | d1         |                                      |              |         | Coding          |
| Review        | r1      | Review    |             | 5d       | 2023-02-05 | dev1       | done                                 |              |   TRUE  | Code review     |
| Launch        | l1      | Release   | 2023-02-10  |          |            | r1         | milestone                            |   TRUE       |         | Go-live         |

**Column Descriptions:**
- **Task Name**: Human-readable name for the task or milestone.
- **Task ID**: Unique identifier for referencing dependencies (optional but recommended).
- **Section**: Gantt chart section/group (optional).
- **Start Date**: Task start date (YYYY-MM-DD). Required unless using dependency.
- **Duration**: Task duration (e.g., 10d for 10 days). Required unless End Date is provided.
- **End Date**: Task end date (YYYY-MM-DD). Optional, can be calculated from Start Date and Duration.
- **Depends On**: Task ID(s) this task depends on (for 'after' syntax in Mermaid).
- **Tags**: Mermaid tags (active, done, crit, milestone) for styling and logic.
- **Is Milestone**: TRUE/FALSE. If TRUE, task is a milestone.
- **Is Done**: TRUE/FALSE. If TRUE, task is marked as done.
- **Notes**: Any additional notes (optional).

See [Mermaid Gantt Docs](https://mermaid.js.org/syntax/gantt.html) for more details on syntax and options.

## Documentation Links:

1. [Mermaid Gantt Docs](https://mermaid.js.org/syntax/gantt.html)