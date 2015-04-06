##Setting up the Virtual Environment
==================
1. If you do not have virtualenv installed, run the following command: `pip install virtualenv`
2. Create a new virtualenv: `virtualenv venv`
3. Activate the virtualenv: `source venv/bin/activate`
4. The first time you activate your new virtualenv, perform the following command to install all of the necessary dependencies: `pip install -r requirements.txt`
5. When done, decative the virtualenv: `deactivate`

##Integrating the utilties as a subtree
==================
1. Add the utilities as a remote: `git remote add utils https://github.com/Reviewify/utilities.git`
2. Fetch the remote: `git fetch utils`
3. Checkout and populate a branch for utils: `git checkout -b utils_branch utils/master`
4. Checkout the master branch: `git checkout master`
5. Read the remote tree into the local directory 'utils': `git read-tree --prefix=utils/ -u utils_branch`

## Updating the utils_branch
==================
1. Checkout the subtree branch: `git checkout utils_branch`
2. Pull changes: `git pull`
3. Checkout master branch: `git checkout master`
4. Merge changes (using --squash): `git merge --squash -s subtree --no-commit utils_branch`
