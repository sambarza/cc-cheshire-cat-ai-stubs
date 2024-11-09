## What is this?
This repo contains stubs files for Cheshire Cat AI framework

## How to use?
launch `git clone https://github.com/sambarza/cc-cheshire-cat-ai-stubs.git typings` in the same folder where there is the `compose.yml` file.

Inside the `.vscode/settings.json` file put:
``` json
{
    "python.analysis.stubPath": "typings",
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    }
}
```
