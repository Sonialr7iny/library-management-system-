# Agent Rules — Library Management System

## 1. Project Goal

The current goal is to verify and test the existing Library Management System.

Do NOT treat this task as a feature-development task.

Focus on:

- Testing existing functionality.
- Finding real bugs.
- Fixing only necessary bugs.
- Keeping the existing architecture and scope intact.

---

## 2. Architecture

The project follows this architecture:

CLI
↓
Service
↓
Repository
↓
JsonRepository
↓
JSON storage

Respect the existing separation of responsibilities.

- CLI handles user interaction, navigation, input, and presentation.
- Services contain business logic and business rules.
- Repositories handle data access and persistence-related operations.
- JsonRepository handles generic JSON file storage.

Do NOT move business logic into the CLI.

Do NOT move persistence logic into the CLI or Service layer.

Do NOT introduce a new architecture unless explicitly requested.

---

## 3. Scope Control

Do NOT:

- Add new features.
- Add unnecessary abstractions.
- Perform unrelated refactoring.
- Rename public APIs without a clear reason.
- Change the project architecture unnecessarily.
- Add dependencies unless absolutely necessary.
- Rewrite working code just for stylistic preference.

If an improvement is not required for the current testing task, leave it unchanged.

---

## 4. Testing Strategy

Test the existing features systematically.

Cover:

### Books

- List all books.
- Search by title.
- Search by author.
- Search by category.
- Add a book.
- Update a book.
- Delete a book.
- Handle book-not-found cases.
- Validate required book fields.
- Verify book state changes when borrowed and returned.

### Members

- List all members.
- Search members by name.
- Add a member.
- Update a member.
- Delete a member.
- Handle member-not-found cases.
- Validate required member fields.

### Loans

- Borrow an available book.
- Prevent borrowing an unavailable book.
- Handle non-existent book IDs.
- Handle non-existent member IDs.
- Return a borrowed book.
- Prevent returning the same loan twice.
- Handle non-existent loan IDs.
- View active loans.
- Verify book state changes from AVAILABLE → BORROWED → AVAILABLE.

### CLI

- Main menu starts correctly.
- Books menu works.
- Members menu works.
- Loans menu works.
- Invalid menu choices are handled.
- Expected application exceptions are handled without exposing implementation details.
- The application exits cleanly.

---

## 5. Test Quality

Every test must verify actual behavior.

Do NOT create tests that only execute code without meaningful assertions.

Prefer:

- Arrange
- Act
- Assert

Tests should verify:

- Return values.
- State changes.
- Stored data.
- Raised exceptions.
- Relevant side effects.

Test both:

- Happy paths.
- Expected failure paths.

Do NOT weaken, delete, skip, or remove a test just to make the test suite pass.

---

## 6. Bug Fixing Rules

If a test exposes a real bug:

1. Identify the root cause.
2. Make the smallest reasonable production-code change.
3. Preserve existing behavior that is already correct.
4. Run the relevant test again.
5. Run the full test suite afterward.

Do NOT modify production code merely to satisfy an incorrectly written test.

If the expected behavior is ambiguous, stop and ask for clarification instead of guessing.

---

## 7. Production Code Changes

Before changing production code, determine whether:

- The implementation is actually incorrect.
- The test is incorrect.
- The issue is caused by test setup.

Do not change production code when the implementation already satisfies the intended behavior.

Keep fixes minimal and localized.

---

## 8. Data Isolation

Tests must not depend on the user's real data/data.json.

Use isolated test data or temporary storage where appropriate.

Tests should be repeatable and should not corrupt or permanently modify project data.

A test should be able to run independently whenever practical.

---

## 9. Code Quality

The project uses Python 3.11.

Follow the existing project conventions.

Run:

ruff check .

after relevant changes.

Do not introduce:

- Unused imports.
- Dead code.
- Unnecessary dependencies.
- Debug prints.
- Temporary test code in production files.

Keep type hints and naming consistent with the existing codebase.

---

## 10. Git Safety

The agent MUST NOT:

- Create commits automatically.
- Push to GitHub automatically.
- Merge branches automatically.
- Delete branches.
- Rewrite Git history.
- Use force push.
- Modify Git configuration.

Before making significant changes, preserve the current working state.

After changes, report:

- Which files changed.
- What was changed.
- Why it was changed.
- Test results.
- Ruff results.

The human developer will decide when to commit, push, merge, or create the PR.

---

## 11. Transparency

Never hide failures.

If a test fails:

- Report the failing test.
- Explain the likely cause.
- Show whether the issue is in the test or production code.
- Do not silently work around the failure.

Do not claim that the project is fully tested if some tests or features remain unverified.

---

## 12. Minimal Changes

Prefer the smallest change that solves the problem.

Do not refactor unrelated code while fixing a test failure.

Do not optimize prematurely.

Do not introduce abstractions that are not required by the current project.

---

## 13. Final Verification

Before considering the testing task complete, run:

1. The full test suite.
2. ruff check .
3. A basic CLI smoke test if practical.

Then provide a concise verification summary containing:

- Tests passed.
- Tests failed.
- Bugs found.
- Bugs fixed.
- Files changed.
- Ruff status.
- Any remaining known issues.

Do not commit or push the changes.
