# Configuration

## Overview

The configuration file is a `yaml` file that contains the configuration for the tool. The configuration file is located in the root of your project and is named `version-it.yaml` or `version-it.yml`.

## Properties

|Key|Values|Description|
|---|---|---|
|`versioning-scheme`|`semantic`, `calver` or `commit`|Which versioning engine should be used to generate the next tag.|
|`run-on-branches`|`array`|Branches on which the tool should run.|
|`first-version`|`string`|The starting version for the versioning engine.|
|`change-type-map`|`array`|Maps user defined commit tags to the type of change. Allowed values for the action part are: `major`, `minor`, `patch` or `null`. Null means that there should be no bump for a given change.|
|`changelog-sections`|`array`|The sections of the changelog. Each section should contain a title and an array of labels.|
|`change-substitutions`|`array`|List of tokens and their substitutions to be used in the changelog.|
|`changelog-exporters`|`object`|Contains `template-path` and `output-path` keys indicating the paths to the changelog template and the output file respectively.|

## Example

```yaml
versioning-scheme: semantic
run-on-branches:
  - master
  - dev
first-version: 0.0.0
change-type-map:
  - label: wip
    action: null
  - label: test
    action: null
  - label: chore
    action: null
  - label: fix
    action: patch
  - label: feat
    action: minor
  - label: perf
    action: minor
changelog-sections:
  - title: Added
    labels:
      - feature
      - enhancement
  - title: Changed
    labels:
      - refactor
      - improvement
  - title: Fixed
    labels:
      - bug
      - fix
change-substitutions:
  - token: "{{type}}"
    substitution: "Type"
  - token: "{{scope}}"
    substitution: "Scope"
changelog-exporters:
  template-path: examples/templates
  output-path: examples/outputs
```

### Possible values

- `versioning-scheme` can be either `semantic`, `calver` or `commit`.
- `run-on-branches` is an array of branches on which the tool should run.
- `first-version` is the starting version for the versioning engine.
- `change-type-map` is an array of objects with label and action pairs.
- `changelog-sections` is an array of objects, each containing a title and an array of labels.
- `change-substitutions` is an array of objects, each containing a token and its corresponding substitution.
- `changelog-exporters` is an object containing paths to the changelog template and the output file.
