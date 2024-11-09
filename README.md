## What is this?
This repo contains stubs files for Cheshire Cat AI framework

## How to use?
In the folder where there is the `compose.yml` file, run:
```shell
git clone https://github.com/sambarza/cc-cheshire-cat-ai-stubs.git typings
``` 

Inside the `.vscode/settings.json` file put:
``` json
{
    "python.analysis.stubPath": "typings",
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    }
}
```
