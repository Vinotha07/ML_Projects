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
docker installation  is optional

create .github folder inside that create workflow and then create a file main.yaml
write code to trigger by writing git hub comments to push the docker image to heroku for continous deployment
in main.yaml we need to pass the heroku email id, api key and the app name in the secrets. so that we can continous deployment.
in git hub go to setting and click on secrets at the left side and select actions then click on New repository secret give name "HEROKU_EMAIL" give your heroku email id in the Value and add secret then heroku email secret got created
again give new scret then give name as "HEROKU_API_KEY" and enter the key in the Value
again create new secret and give"HEROKU_APP_NAME" and enter the app  name in the value and add secret
then go to action tab and go to workflow folder and select main.yaml and rerun in the git hub.
if we again change anything in the code after push the code then go to action tab and click on the build in the github it will automatically deploy the changes . 


create the folder housing folder.this is the root folder where we can write all our code.
create setup.py file .....its like requirement txt file
create __init__.py under housing. like create the library as the housing
in setup file give the packages as a list since it has the folder name used in the pjt

..........
python setup.py install
..................
above command install all the modules in the requirement.txt and create some folders like
Housing_Predictor.egg
build
dist 
folders by default

.............
pip install -e .
............
above command helps to install the available pkgs

find package() in setup file automatically find the __init__.py file and return the folder in which it has

folder name - package
file name- module
for -e. the setup.py is mandatory. to update the version of the pjt
egg pkg has our custom package information

create folder structure and every folder should have __init__.py file
..................
config
exception
logger
component
entity
pipeline
..................

1st we have to work on logger and exception at root level
while we write code we need logger to see what happening and exception give how u can handle the error

once u create logger file, create the logging config and test if it is working by adding logging command to the app.py
then run pip install-r req.txt and python app.py


cntrl+c for stop running

to write custom exception class by inherit python exception class

we are customizing the exception which is needed to find in which line error is occured and its type

entity-real world object, its like table, we have to identify the entity
for example in college admission system the entities are
student
class room
subject
department
exam
the attribute of the student is roll no, dob,name
methods of student are attendance, results


create files in the component
then create pipeline.py files in the pipeline folder

start to create config_entity file under entity pkg

create notebook file and install for jupyter notebook and choose our env at the top right corner. example folder is not the part of the pjt
..........
pip install ipykernel
................

create config folder outside and that should have the yaml file which should have all the details of the configuration which will be read by the entity config


...........
pip install PyYAML

helper function will be write in util folder

we can decalre all the constant in the constant folder that is hardcoded

artifact entity is for the output file 