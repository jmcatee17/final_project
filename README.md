### Ensure todo.py script is executable from anywhere

- **Step 1:** add .pickle file to the home directory
     - This is an invisible file, since it starts with a period. Meaning it is difficult for users to access.
     - Additionally, since it is in the home directory, all programs can access the .pickle file.

- **Step 2:** Add shebang line to top of todo.py file:
     - Add this to top of file so it can be executed from anywhere
     - ```#!/usr/bin/env python```

- **Step 3:** Change Permissions and Move file to a location in $PATH
     - If we run the linux command ```echo $Path```, we see all the locations where the computer looks to find an executable file.
     - We see `/usr/local/bin` is one of the paths, while is where we stored the pickle file.
     - We will add this script here. We will need to use the command `sudo chmod a+rx todo.py` to change the permissions, and write in our password
     - Then we can move the command using super user `sudo cp todo.py /usr/local/bin/`
     - Source: https://askubuntu.com/questions/877992/how-to-put-executable-to-usr-local-bin
     - Source: https://www.geeksforgeeks.org/linux-unix/chmod-command-linux/

- **Step 4:**
     - Now the program can be executed from any directory on the computer!