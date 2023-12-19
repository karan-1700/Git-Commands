Git and Github

#########################################

Git is a distrubuted version control system / tool, while Github is a web-based hosting service for git repositories.

#########################################

Basic Git Workflow: Local storage -->  Staging area --> Github

#########################################

Command: git status

#########################################

Add files into the Staging area
Command: git add file1 file2

#########################################

Commiting
Command: git commit -m "initial commit"

Command: git commit -m "Fixed the bug that ..."

#########################################
#########################################

# Create a new Repository on the command line
echo "# Temp" >> README.md
git init
git add README.md
git commit -m "First commit"
git remote add origin <url>  -> Add the URL for the remote repository where your local repository will be pushed
	git remote add origin https://github.com/karan-1700/Git-Commands.git
git push -u origin master

# push an existing repository from the command line
git remote add origin https://github.com/karan-1700/Git-Commands.git
git push -u origin master

#########################################
#########################################

git remote add origin git@github.com:karan-1700/Git-Commands.git