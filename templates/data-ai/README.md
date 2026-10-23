# Data / AI Project Template

Use this template for a data analysis, machine-learning, or AI-powered proof of concept. It emphasizes reproducibility and transparent limitations rather than requiring a particular framework.

## Suggested structure

- `data/`: place only data you have permission to share; avoid personal or sensitive data.
- `src/`: reusable code.
- `reports/`: charts, findings, and limitations.
- `README.md`: problem, data provenance, setup, methods, results, and evaluation.

## Reproducibility checklist

- [ ] State where data came from and what license or terms apply.
- [ ] Explain cleaning, assumptions, and known data gaps.
- [ ] Record model or API details and required configuration.
- [ ] Evaluate results on suitable test cases; explain uncertainty and failure modes.
- [ ] Document privacy, bias, safety, and misuse risks relevant to the project.
- [ ] Keep API credentials in environment variables or a secret manager, never in code.
- [ ] Make it clear when output is generated or estimated rather than verified fact.

There is intentionally no sample dataset. Add only data that you are authorized to use and disclose.
