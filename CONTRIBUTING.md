# Contributing

Improvements to the starter kit are welcome. Please open an issue for broad changes and submit focused pull requests.

- Keep guides suitable for different experience levels and accessible to participants.
- Do not invent event details or imply a template is an official policy.
- Preserve clear separation between code licensing and educational-content licensing.
- Check third-party rights and cite sources when adding adapted content.
- Never submit secrets, private participant data, or confidential reports.

Run these checks before opening a pull request:

```bash
python scripts/validate.py
python -m unittest discover -s templates/python-cli/tests -v
python -m compileall -q templates/python-cli
```

Changes to scoring and participant rules should be transparent, reviewed, and published before the relevant event starts.
