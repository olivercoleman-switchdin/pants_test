Repo for testing and debugging some things with Pants.

#Important note

The first time you open, or if you rebuild, the container, you should see a message in the output terminal window that says:

```Running the postCreateCommand from devcontainer.json...```

followed by some more lines like:

```[14841 ms] Start: Run in container: ...```

You must wait until you see the line:

```Done. Press any key to close the terminal.```

before doing anything other than opening and editing files (for example do not reload the window).

**You will then likely need to reload (or open and close) the window for VS Code to use the newly build Pants venv**
