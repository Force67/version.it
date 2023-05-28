# Versioning Schemes

This document outlines the different versioning schemes that version-it supports and how they are interpreted.

> Can't find a versioning scheme you need? Please open an issue or submit a pull request!

## [Semantic Versioning](https://semver.org/)

```json
"versioning-type": "semantic",
```

> Please note that our interpretation deviates from the original specification in that we allow versioning to start from 0.0.0, and we do not mandate a major version increment for breaking changes. This approach makes sense as it's impractical to start versioning from 1.0.0 when the project is still under development, but you might still want to incorporate in-development version bumps into the first release.

Fields:

- major
- minor
- patch

When to use:

- For libraries that other software relies on.
- To understand if a new version maintains backward compatibility.
- To communicate the nature of changes incorporated in a new version (thus helping to gauge the impact of an update).

How does it work?

- For each change type tagged "patch" in a cycle, the patch version is incremented (As defined in "commit-tags" in the config file). For example, this could include tweaks and fixes.
- For each change type tagged "minor" in a cycle, the minor version is incremented. This might involve a completed feature or a breaking change.
- For each feature tagged "major", you need to manually increment the major version. This includes non-backwards compatible changes or a complete overhaul of the software.

## [CalVer](https://calver.org/)

This is a time-based versioning scheme where the version is dependent on the release date.

```json
"versioning-type": "calver",
```

Fields:

- year
- month
- micro
- (optional) branch

When to use:

- When each revision of the software will be utilized for a significant duration (for instance, a Linux distro). This aids in tracking the age of the software.
- When frequent substantial changes are made.
- For versioning data to swiftly determine if the dataset remains relevant.

How does it work?

- The Major (year) version always corresponds to the current year.
- The Minor (month) version always corresponds to the current month.
- The Micro (day) version is incremented with each commit. Features count as 2 bumps, while bugfixes/tweaks, etc., count as 1 bump.
- If enabled, the current branch is appended to the version. The branch is selected from the current branch on which version.it is run.

## Commit Versioning

This scheme increments a number by a given weight for each change.

```json
"versioning-type": "commit",
```

Fields:
Simply an integer

When to use:

- When you are indifferent about versioning or just desire a straightforward way to differentiate between versions.

How does it work?

- For each patch (including bug fixes, tweaks, etc.), the version is incremented by 1.
- For each minor change (feature), the version is incremented by 2.
- For each major change (breaking modification), the version is incremented by 3.
