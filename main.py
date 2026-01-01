from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("josef")

BASE_DIR = os.path.dirname(__file__) if "__file__" in globals() else os.getcwd()
NOTES_FILE = os.path.join(BASE_DIR, "notes.txt")


def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")


@mcp.tool()
def add_note(message: str) -> str:
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note saved!"


@mcp.tool()
def read_notes() -> str:
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or "No notes yet."


@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the most recently added note from the sticky note file.

    Returns:
        str: The last note entry. If notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."



@mcp.prompt()
def note_summary_prompt()->str:
    """
    Generate a prompt asking the AI to summarize all current notes.

    Returns:
        str: A prompt string that includes all notes asks for a Summary.
            If no notes exist, a message will be shown indicationg that.
    """
    ensure_file()
    with open(NOTES_File, "r") as f:
        content = f.read().strip()
    if not content:
        return "There are notes yes."
    return f"Summarize the current notes: {content}"
