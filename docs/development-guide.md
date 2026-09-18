# Development Guide

This guide records the conventions that keep AI-assisted changes consistent
and reviewable.

## Change shape

One pull request implements one GitHub issue. Start from the issue, inspect
the nearest implementation and tests, and make the smallest change that
satisfies its acceptance criteria.

For a new application behavior:

1. Implement the smallest behavior that satisfies the issue.
2. Preserve the consumer application's existing interface unless the issue
   specifies a change.
3. Add focused automated tests for the behavior.
4. Add tests for issue-specific edge cases and errors.

## Compatibility

Preserve the consumer application's existing argument formats, output style,
command names, and successful exit status unless an issue explicitly changes
them. Error behavior must be clear and must not expose a traceback to users
when the issue requires user-facing error handling.

For numeric operations, explicitly define behavior for zero, negative,
`nan`, positive infinity, and negative infinity when those values can be
parsed. Add unit and CLI tests for the required edge cases, including clear
non-zero errors without tracebacks.

For workflow and agent inputs, validate values at the boundary that parses them.
Normalize equivalent documented forms, such as `58` and `#58`, and test both
accepted forms plus malformed input behavior.

For workflow, agent, or repository-usage changes, update the README with the
user-facing workflow and link any detailed guide that was added or changed.

## Work categorization

Assign exactly one primary category to every issue and pull request. Categories
describe what changed, not whether the work was successful:

- `cli`: parsing, help, version output, and user-facing errors;
- `testing`: tests, fixtures, and coverage configuration;
- `ci`: workflows, checks, and build automation;
- `agent-guidance`: Copilot instructions, agent files, and development guides;
- `architecture`: design decisions and structural changes;
- `documentation`: README and other user-facing documentation; or
- `metrics`: acceptance tracking and reporting.

Keep review or rework reasons separate from the primary category. Use reason
labels such as `acceptance-gap`, `missing-tests`, `regression`, `ci-failure`,
`scope-creep`, `documentation-gap`, or `merge-conflict` when they apply.
The primary category answers "what changed?"; the reason answers "what went
wrong or required rework?".

## Review rejection reasons

A change should be sent back for revision when it:

- misses or weakens an acceptance criterion;
- changes an existing command or output without an explicit requirement;
- adds behavior without both unit and CLI coverage where applicable;
- omits a required edge case or error path;
- introduces an unnecessary dependency or broad abstraction;
- mixes unrelated cleanup into the feature;
- lowers coverage below the configured 90% threshold; or
- cannot be reproduced from the stated verification commands.

These are review signals, not a substitute for judgment. Record a new
recurring rejection reason here when it represents a stable repository
convention.

## Verification commands

Use the commands configured in `agentic-project.json`.
