# Architecture Decisions

## Consumer interface remains stable

The application preserves its existing public interface unless an issue
explicitly changes it. This keeps each backlog issue independently testable.

## Dependencies remain intentional

New dependencies are not added unless a future issue explicitly requires them.

## Requirements and feedback are separate layers

GitHub issues and repository instructions define the intended behavior. Tests,
coverage CI, pull-request review, and acceptance metrics provide feedback about
whether that behavior was implemented reliably. The acceptance-rate log is a
process signal and does not replace technical review.

## Optimization is experiment-driven

Level 4 changes to instructions, tests, or workflows are recorded as
experiments with a baseline, a measurable success criterion, and follow-up
pull requests. The feedback report counts rejection reasons on rejected pull
requests so remediation labels on accepted follow-ups do not inflate failure
counts.
