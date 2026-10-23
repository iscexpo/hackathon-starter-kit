# Hackathon Starter Kit

A reusable, open starter kit for running inclusive, well-organized hackathons. It includes participant guidance, submission requirements, project templates, and a transparent judging rubric.

> **Event-specific details must be filled in by the organizers before publishing an event announcement.** This kit intentionally does not invent dates, prizes, eligibility rules, sponsors, or contact details.

## Start here

- Participants: [Participant guide](docs/participant-guide.md)
- Submit a project: [Submission instructions](docs/submission-guide.md) and [submission template](SUBMISSION.md)
- Judges: [Judging rubric](docs/judging-rubric.md)
- Mentors: [Mentor guide](docs/mentor-guide.md)
- Organizers: [Launch checklist](docs/organizer-checklist.md) and [event configuration](EVENT_CONFIG.md)

## Project templates

| Template | Good for | Start here |
|---|---|---|
| Web app | A browser-based prototype using HTML, CSS, and JavaScript | [`templates/web-app/`](templates/web-app/README.md) |
| Python CLI | A small Python tool, automation, or prototype | [`templates/python-cli/`](templates/python-cli/README.md) |
| Data / AI project | Data analysis, a model demo, or an AI-powered concept | [`templates/data-ai/`](templates/data-ai/README.md) |

Templates are starting points, not restrictions. Teams may use their own stack if the project can be reviewed and run as described in the submission.

## Repository map

```text
.
├── .github/ISSUE_TEMPLATE/       # Submission and project proposal forms
├── docs/                         # Participant, judge, mentor, organizer guides
├── templates/                    # Web, Python, and data/AI starter projects
├── SUBMISSION.md                 # Copy into a team's project repository
├── EVENT_CONFIG.md               # Organizer-owned event-specific settings
└── scripts/validate.py           # Local link and required-file checks
```

## Quick start for participants

1. Read the participant guide and the event-specific rules.
2. Choose or create a project repository.
3. Copy a starter template or bring your own project.
4. Build a small, testable solution to a clearly stated problem.
5. Prepare a working demo, setup instructions, and a completed `SUBMISSION.md`.
6. Submit using the event's published process before its deadline.

## Quick start for organizers

1. Fill in [EVENT_CONFIG.md](EVENT_CONFIG.md).
2. Publish dates, eligibility, team-size limits, tracks, submission cut-off, prize information, and contact channel.
3. Decide whether submissions arrive via GitHub issue form, event portal, or both; test the path using a dummy entry.
4. Recruit judges and disclose conflicts of interest.
5. Explain accessibility needs, code/data licenses, AI-use disclosure, privacy expectations, and judging criteria before registration opens.
6. Run `python scripts/validate.py` and confirm every template works before sharing the repository.

## Develop locally

Clone this repository and run the validation checks before adapting the kit:

```bash
git clone https://github.com/iscexpo/hackathon-starter-kit.git
cd hackathon-starter-kit
python scripts/validate.py
python -m unittest discover -s templates/python-cli/tests -v
python -m compileall -q templates/python-cli
```

Complete [EVENT_CONFIG.md](EVENT_CONFIG.md) before using the materials for a real event. Review all placeholders, submission channels, eligibility rules, privacy requirements, license terms, judging criteria, and contact details with the responsible organizers.

## Contributing

Issues and focused pull requests are welcome. Fork this repository if you do not have permission to push branches to it, then create a feature branch for your changes.

```bash
git switch -c docs/describe-your-change
# Make your changes, then run the checks shown above.
git add .
git commit -m "docs: describe your change"
git push -u origin docs/describe-your-change
gh pr create --base main
```

The `main` branch is protected. Pull requests must pass the **Content and template checks** workflow, receive one approving review, and resolve review conversations before merging. Do not push directly to `main`.

## License

- Code in this repository: [MIT License](LICENSE)
- Original guides, rubrics, and educational content: [CC BY 4.0](CONTENT-LICENSE.md)
- Third-party assets and dependencies retain their own licenses; teams must check and document them.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guidelines. Do not commit credentials, private participant information, or unlicensed material.
