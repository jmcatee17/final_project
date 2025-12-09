### Ensure todo.py script is executable from anywhere

- **Step 1:** add .pickle file to the home directory
     - This is an invisible file, since it starts with a period. Meaning it is difficult for users to access.
     - Additionally, since it is in the home directory, all programs can access the .pickle file.

- **Step 2:** Add shebang line to top of todo.py file:
     - Add this to top of file so it can be executed from anywhere
     - ```#!/usr/bin/env python```

- **Step 3:** Move file to a location in $PATH
     - If we run the linux command ```echo $Path```, we see all the locations where the computer looks to find an executable file.
     - We see `/opt/anaconda3/bin` is one of the paths, while is where we stored the pickle file.
     - We will add this script here.

- **Step 4:** Change permissions of the file so any program can run it:
     - If we run the linux command ```echo $Path```, we see all the locations where the computer looks to find an executable file.
     - Source: https://www.geeksforgeeks.org/linux-unix/chmod-command-linux/

