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

Enable Automatic Email Notification
A Gmail test account (machinelearning2k@gmail.com)has been created
for the purpose of sending out automated email notification. The
security level of this account has also been lowered to enable access
from apps such as this one:
https://support.google.com/accounts/answer/6010255

Simply change the recipient's email address in the program to get
automated notifcation from this application.

