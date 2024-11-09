## What is this?
This repository contains stubs files for the Cheshire Cat AI framework.

## How to use it?
In the folder containing the `compose.yml` file, run:
```bash
git clone https://github.com/sambarza/cc-cheshire-cat-ai-stubs.git typings
``` 

Then, inside the `.vscode/settings.json` file, add:
``` json
{
    "python.analysis.stubPath": "typings",
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    }
}
```

Now, autocomplete in VSCode should work properly.
