# ML_Projects
Software and account Requirements
[Github account](https://github.com)
[Heroku Account](https://dashboard.heroku.com/login)
[VS CODE IDE]
[GIT CLI]
[GIT DOCS](https://git-scm.com/docs/gittutorial)
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
To setup CI/CD pipeline in heroku we need 3 info
1. Heroku_Email=
2. Heroku_API_KEY=
3.HEROKU APP_NAME=

create Docker file
dockerignore

Build Docker Image
..........
docker build -t <image_name>:<tagname>.

docker build -t ml-project:latest.

Note:IMAGE NAME FOR DOCKER MUST BE LOWERCASE

To list docker image
........
docker images
......
Run docker image
..........
docker run -p 5000:5000 -e PORT=5000 <IMAGE ID WHICH WE GOT FROM ABOVE SCRIPT>

to check running container in docker
``````
docker ps
`````````

TO STOP IMAGE WE CAN USE
.........
docker stop <container id>
id get it from above
