## What is this?
This repository contains stubs files for the Cheshire Cat AI framework, necessary for autocomplete feature in VSCode

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

Now, autocomplete in VSCode should work properly:
![autocomplete](https://github.com/user-attachments/assets/90d70f2b-9a99-416b-9d94-408fe81cb112)
