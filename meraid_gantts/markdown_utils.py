# markdown_utils.py

def find_gantt_section(markdown_content):
    """
    Find the Gantt chart section in the markdown content.

    Args:
        markdown_content (str): The content of the markdown file.

    Returns:
        str: The Gantt chart section if found, otherwise None.
    """
    lines = markdown_content.splitlines()
    gantt_section = []
    # Look for a header (##, ###, etc.) containing 'Gantt' (case-insensitive)
    for idx, line in enumerate(lines):
        if line.strip().lower().startswith('#') and 'gantt' in line.lower():
            gantt_section.append(line)
            # Collect lines after the header until the next header or end of file or next header
            for next_line in lines[idx+1:]:
                if next_line.strip().startswith('#') and next_line.strip() != line.strip():
                    break
                gantt_section.append(next_line)
            break
    return '\n'.join(gantt_section) if gantt_section else None


def update_gantt_section(markdown_content, new_gantt_data):
    """
    Replace the content of the Gantt chart section in the markdown content with new_gantt_data.
    Assumes the Gantt section header has already been found and is unique.

    Args:
        markdown_content (str): The content of the markdown file.
        new_gantt_data (str): The new Gantt chart data to insert.

    Returns:
        str: The updated markdown content.
    """
    lines = markdown_content.splitlines()
    updated_content = []
    gantt_header_idx = None

    # Find the Gantt section header
    for idx, line in enumerate(lines):
        if line.strip().lower().startswith('#') and 'gantt' in line.lower():
            gantt_header_idx = idx
            break

    if gantt_header_idx is None:
        # No Gantt section found, just append at the end
        return f"{markdown_content}\n\n{new_gantt_data}"

    # Copy lines up to the Gantt header
    updated_content.extend(lines[:gantt_header_idx])
    # Add the header
    updated_content.append(lines[gantt_header_idx])

    # Skip old Gantt section, add new data
    for idx in range(gantt_header_idx + 1, len(lines)):
        line = lines[idx]
        if line.strip().startswith('#') and idx != gantt_header_idx:
            # Found the next header, stop skipping
            updated_content.append(new_gantt_data)
            updated_content.extend(lines[idx:])
            break
    else:
        # No more headers, replace everything after header
        updated_content.append(new_gantt_data)

    return '\n'.join(updated_content)


def append_gantt_section(markdown_content, gantt_data):
    """
    Append a Gantt chart section to the markdown content.

    Args:
        markdown_content (str): The content of the markdown file.
        gantt_data (str): The Gantt chart data to append.

    Returns:
        str: The updated markdown content with the appended Gantt chart.
    """
    return f"{markdown_content}\n\n{gantt_data}"