"""Minimal Python CLI starter."""


def summarize_project(project_name: str) -> str:
    """Return a friendly project summary for a non-empty name."""
    cleaned = project_name.strip()
    if not cleaned:
        raise ValueError("project_name must not be empty")
    return f"Project ready: {cleaned}"


def main() -> None:
    print(summarize_project("Your hackathon idea"))


if __name__ == "__main__":
    main()
