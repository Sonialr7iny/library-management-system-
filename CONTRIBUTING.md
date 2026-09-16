# Contributing Guidelines

## Development Workflow

1. Create or receive an Issue
2. Create a feature branch
3. Implement the assigned task
4. Commit the changes
5. Push the branch
6. Open a Pull Request
7. Request a code review
8. Address review comments
9. Get approval
10. Merge the Pull Request
11. Close the related Issue

## Branch Naming

feature/<issue-name>
bugfix/<issue-name>

## Commit Convention

feat: add book model
fix: validate loan date
test: add loan tests
docs: update README
refactor: simplify repository logic

## Coding Conventions

- Follow consistent Python naming conventions.
- Use type hints.
- Keep business logic inside services.
- Keep data access inside repositories.
- Keep the CLI responsible for user interaction.
- Avoid duplicated logic.
- Keep classes focused on a single responsibility.

## Pull Request Guidelines

- Keep PRs focused on one Issue.
- Explain what was changed.
- Link the related Issue.
- Make sure tests pass before requesting review.
- Address reviewer feedback before merging.

## Code Review

- Review code for correctness, readability, and adherence to project conventions.
- Ask questions or suggest improvements when necessary.
- Approve the PR only after the requested changes have been addressed.