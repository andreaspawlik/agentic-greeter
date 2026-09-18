# Agentic Greeter Consumer

This is a non-calculator consumer smoke test for the shared agentic project contract.

The shared agentic workflow templates are sourced from
[`agentic-engineering-workflows`](https://github.com/andreaspawlik/agentic-engineering-workflows)
release `v1.0.0`. Consumer-specific code, tests, Project configuration, and
metrics remain in this repository.

The public greeting function is:

```python
greet(name: str, punctuation: bool = True, capitalized: bool = False) -> str
```

The default preserves excited punctuation. Pass `punctuation=False` to return
the greeting without punctuation.
Pass `capitalized=True` to uppercase the first character of the name while
preserving surrounding whitespace.

Run the configured commands with:

```bash
python scripts/project_config.py run project.test_command
python scripts/project_config.py run project.coverage_command
```

## Coordinator self-review

For a single-maintainer demo repository, the repository owner may record an
explicit self-review after CI passes:

```text
/coordinator issue-1-c53f1a46 self_reviewed
```

This records `review_source: self`; it does not create a GitHub approval.
Production repositories should use a second reviewer or an approved
administrator bypass policy.
