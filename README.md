# CPEN 442 - Password Cracking + Reverse Engineering
This repository assumes a Linux environment.

**Requirements**:
* Wine
* Python2.7

## Usage
```
bash autopatcher.sh
```
The script will prompt you for a password. Enter it once to patch the executable. The executable is then immediately run and will accept your new password.

Note that `autopatcher.sh` will revert the password patch before terminating.