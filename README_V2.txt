How to run OVERWATCH:

Installation:
First clone the repository into your desired installation folder. I made some changes to Overwatch so that it can be run from anywhere instead of only the root directory.

git clone https://github.com/aaniin/OVERWATCH

Commit d957d5c3baea29b9cdf1d9cbb1e06b45e58d4e8c is the last version before I started implementing the TRD.

OVERWATCH uses python 2.7.9 or newer, python 3 support seems to be implemented, but has not been tested. Install these dependencies using pip:

Flask
Flask-Login
bcrypt
Flask-Bcrypt
ZODB
Flask-ZODB
numpy
flup
flup6
future
requests
uwsgi

sphinx
sphinxcontrib-napoleon
recommonmark

Download jsRoot from here https://root.cern.ch/js/jsroot.html and copy the scripts and style directories to <installation_directory>/OVERWATCH/static/

Install bower using npm:

sudo apt-get install npm
npm install -g bower
cd <installation_directory>/OVERWATCH/webApp/static/
bower install

If you get the error:
/usr/bin/env: node: No such file or directory
when running bower install do this:
sudo ln -s /usr/bin/nodejs /usr/bin/node


Configuration:
Set the basePath variable in /config/sharedParams.py to your OVERWATCH folder path:

basePath = os.path.abspath("<installation_directory>/OVERWATCH/")

Copy /config/serverParams_stub.py to /config/serverParams.py
The defaultUsername variable should remain empty.

Generating the documentation:
cd <installation_directory>/OVERWATCH/doc
make html
Running OVERWATCH:
Download testing data from here: https://aliceoverwatch.physics.yale.edu/contact
Unzip the file and copy the Run<run_number> folders to
<installation_directory>/OVERWATCH/data/

To start processing the data run this command in the OVERWATCH main directory after entering AliPhysics:
python runProcessRuns.py
To start the web app run this command in the OVERWATCH main directory after entering AliPhysics:
python runWebApp.py
Open a web browser and go to http://localhost:8850
Login using username as username and password as password.
Press crtl c in the terminal to stop the web app.