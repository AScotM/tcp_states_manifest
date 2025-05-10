import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import List

# Define a dataclass to represent a TCP state
@dataclass
class TCPState:
    code: str
    name: str
    description: str

def load_tcp_states(manifest_path: Path) -> List[TCPState]:
    """Load TCP states from an XML manifest."""
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest file not found: {manifest_path}")

    tree = ET.parse(manifest_path)
    root = tree.getroot()

    states = []
    for state in root.findall("State"):
        states.append(TCPState(
            code=state.get("code"),
            name=state.get("name"),
            description=state.get("description")
        ))
    return states

def main():
    # Define the relative path to the XML file
    manifest_file = Path(__file__).parent.parent / "manifest" / "tcp_states_manifest.xml"

    try:
        tcp_states = load_tcp_states(manifest_file)
    except Exception as e:
        print(f"Error loading TCP states: {e}")
        return

    # Print the states
    for state in tcp_states:
        print(f"{state.code} - {state.name}: {state.description}")

if __name__ == "__main__":
    main()
