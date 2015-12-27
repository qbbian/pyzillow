Installation
--------------------------------------
Install pip:
1. sudo easy_install pip # Install pip

Install ipythonn (Optional):
1. Create .pydistutils.cfg in your $HOME following contents
[global]
verbose=1

[install]
install-scripts=$HOME/bin

[easy_install]
install-scripts=$HOME/bin

2. Run:
pip install -U --user --force ipython

3. Add ~/bin to PATH in .bash_profile (create the file if it does not exist)

Install pandas:
1. Run:
pip install -U --user --force pandas

To enable automatic email alert from this Python script, please change
your settings to allow less secure apps to access your account:

https://support.google.com/accounts/answer/6010255

