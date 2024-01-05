# Git and Github

**Git** is a distrubuted version control system / tool, while **Github** is a web-based hosting service for git repositories.

## Basic Git Workflow: 
**Local storage -->  Staging area --> Github**
```
git status
git add .
git status
git commit -m "initial commit"

git remote set-url origin https://<<SSH Key>>@github.com/karan-1700/Git-Commands
git push origin main
```

# Git-Commands
List of Git commands

## Add files into the Staging area
- Command: `git add file1 file2`
- Command: `git add .`  - to add everything at once
- Command: `git add ./folder` - to add any specific folder
- Command: `git add *.py`  - to add all files with the given suffix

## Commiting
- Command: `git commit -m "initial commit"`
- Command: `git commit -m "Fixed the bug that ..."`

## If you need to remove a single file from the staging area, use
- `git reset HEAD -- <file>`

### If you need to remove a whole directory (folder) from the staging area, use
- `git reset HEAD -- <directoryName>`

Your modifications will be kept. When you run `git status` the file will once again show up as modified but not yet staged.

### To unstage a specific file

- `git reset <file>` -> That will remove the file from the current index (the "about to be committed" list) without changing anything else. 

To unstage all files from the current change set:
- `git reset`

# Push an existing repository from the command line
- `git remote add origin <url>`  -> Add the URL for the remote repository where your local repository will be pushed
- `git remote add origin https://github.com/karan-1700/Git-Commands.git`
- `git push origin master`


# Create Personal Access Token on GitHub

From 2021-08-13, GitHub is no longer accepting account passwords when authenticating Git operations. You need to add a PAT (Personal Access Token) instead, and you can follow the below method to add a PAT on your system.

> From your GitHub account, go to **Settings → Developer Settings → Personal Access Token → Tokens (classic) → Generate New Token** (Give your password) → **Fillup the form** → click **Generate token → Copy the generated Token**, it will be something like `ghp_sFhFsSHhTzMDreGRLjmks4Tzuzgthdvfsrta`


# Clone on Linux/Debian (`git clone` as follows):

`git clone https://<tokenhere>@github.com/<user>/<repo>.git`



