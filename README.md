# ML_Projects
Software and account Requirements
[Github account](https://github.com)
[Heroku Account](https://dashboard.heroku.com/login)
[VS CODE IDE]
[GIT CLI]
after cloning git hub 


we need to create conda env syntax below
conda create -p <anyname> python==3.7 -y

open new terminal and then give below code
..........
conda create -p venv python==3.7 -y
......


After creating virtual env we need to activate it by below command
.....
conda activate venv/

or

conda activate venv
......

create requirement.txt 
.......
pip install -r requirements.txt 
......
create app.py file
enter your code
to run
.......
python app.py
..............

add files to the git to maintain the version
.......
git add <filename1 filename2>

or

git add .

to add all the files
.....

reject files or folder we can write name of file/ folder  in .gitignore file

to check  the files untracked files 
.......
git status 
........
To check all version maintained by git
......
git log
......

to create version/commit all changes by git

.......
git commit -m "message"

..........."
To send  the changes to git use push
...........
git push origin main
..........

to check remote url(gives git link where these files stored)
.........
git remote -v
............

to get branch name
.........
git branch
..........
