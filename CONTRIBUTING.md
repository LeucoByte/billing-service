# Contributing to billing-service

Thanks for helping out. This is a small team so the rules are short, but please follow them,
reviews go much faster that way.

## Setup

Python 3.11 or newer. There are no dependencies, just clone and run the tests:

```
python -m unittest discover -s tests -v
```

## Branches and commits

- Branch from `main`. Use `feat/<short-name>` for new things and `fix/<short-name>` for bug fixes.
- Keep commits small and write the message in the imperative ("add", not "added").
- Do not push to `main` directly, it is protected.

## Issues

- Search before opening a new one, there are a lot of old ones.
- Every issue needs at least one label (`bug`, `feature`, `docs` or `blocked`). Unlabelled issues
  get lost during planning, so add it when you create the issue.
- If something is waiting on another issue, add the link as "blocked by" in the issue and use the
  `blocked` label only while it is really stuck.

## Pull requests

- The title starts with `feat:` or `fix:` (for example `fix: round VAT per line`).
- The description must include `Closes #N` for the issue it solves, so the issue closes when the PR is merged.
- One approving review is required and the `test` check in CI has to be green before merging.
- Add or update tests for what you change.
- Resolve the review conversations when the comment is addressed. The reviewer can also do it.
- We squash merge unless there is a good reason not to.

## Releases

Tagged from `main` by whoever is on call that week. Ask in the team channel.
