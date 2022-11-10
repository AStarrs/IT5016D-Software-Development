
`git init` - create a new local repository

`git add` - adds one or more files to staging. You can either detail a specific
file to add to staging or add all changed files by typing `git add .`   

`git commit` - commits your changes to the repository. Commits must always be
must be accompanied by the -m flag and commit message.

`git commit -m 'This is a test commit'`

`git status` - tells you what branch are you currently on and whether you have changes to commit or not.

`git clone` -  allows you to clone (copy) a repository into the directory you're
currently in. 
Keep in mind you can clone both remote repositories (in GitHub, GitLab, and so on) and local repositories (those that are stored in your computer).

`git clone https://github.com/coccagerman/MazeGenerator.git`

`git remote add origin` - is used to detail the URL of the remote repository you're going to use for your project. In case you'd like to change it at some
point, you can do it by using the command 

`git remote set-url origin`

`git remote add origin https://github.com/coccagerman/testRepo.git`

Keep in mind you need to create your remote repo first in order to get its URL

`git remote -v` - lets you list the current remote repository you're using

`git push` - uploads your commited changes to your remote repo

`git branch` - lists all the available branches on your repo and tells you what branch you're currently on. If you want to create a new branch, you just have to
add the new branch name as parameter like 

`git branch <branch name>`

`git checkout` - moves you from one branch to another. It takes your destination
branch as paremeter

`git checkout newBranch`- Switched to branch 'newBranch'

`git pull` - pulls (downloads) the code from your remote repository and combines
it with your local repo. This is particularly useful when working in teams, when
many developers are working on the same code base. In this case each developer
periodically pulls from the remote repo in order to work in a code base that
includes the changes done by all the other devs

If there's new code in your remote repo, the command will return the actual
files that were modified in the pull. If not, we get Already up to date

`git diff` - allows you to view the differences between the branch you're
currently in and another

`git diff newBranch`

As a side comment, when comparing differences between branches or repos,
ussually visual tools like Meld are used. It's not that you can't visualize it
directly in the terminal, but this tools are greate for a clearer visualization.

To exit from diff list press `q` or `h` for help

`git merge` - merges (combines) the branch you're currently in with another.
Keep in mind the changes will be incorporated only to the branch you're
currently in, not to the other one.

`git merge newBranch`

`git log` lists all previous commits you've done in the repo

To exit from log list press `q` or `h` for help

The `--help` flag will show you information about a given command, exactly the
same way it works with bash

`git diff --help` 