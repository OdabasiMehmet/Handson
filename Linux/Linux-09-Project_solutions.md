## Part 1: Security Issue
You are working in a Financial Company as DevSecOps. Recently, one of your instances has been terminated by someone within the firm. That instance was very important for firm's web-app and also your infrastructure has been affected by this termination. Your team lead is suspecting `Serdar` user. You have assigned to find instances' ids terminated by `Serdar` user. You have Cloudtrail event history file named `event_history.csv`. Instance ids within this event history look like `i-0c127ab5cdf997cf4`. You have to apply some filtering and string manipulation commands to find ids. To be able to handle this tasks, you decided to create a bash script, then, save instances' ids terminated by `Serdar` user in `result.txt` file.  

cat event_history.csv | grep serdar | grep -i Terminateinstance | grep -Eo "i-[a-zA-Z0-9]{17}" > /tmp/result.txt

1. Use cat filename to display the event file

2. Pipe the output as input and use grep to find the string "serdar"

3. Pipe the output and use grep -i to find TerminatedInstances without case sensitivity

4. Use grep -Eo to enable regex and show only the exacth matches
  We know that the id is 17 charcters long after the i- so we use square brackets to find any matching characters that will fill the 17 characters

5. Save the output to a file by using > character

## Part 2: User and Password Script
You're working as a System Administrator for a e-commerce company. The latest company initiative requires you to write an ansible file for dozens of servers. You're falling behind schedule and are going to miss your deadline for these ansible files because you are constantly being interrupted by the HR calling you to create new Linux accounts for all the people in the company who have been recruited to test out the company's newest Linux-based application.

In order to meet your deadline and keep your sanity, you decide to write a shell script that will create new user account and automatically generate a password for each of new account. Once you're done with the shell script you can put the HR in charge of creating new accounts which will finally allow you to work uninterrupted and complete your server deployments on time. 

Your script accepts user account name and comments as parameter. Then create a new user and a password for them. At the same time, you want users to change their password, when they login the system at the first time. Please create this bash scripting file named `user_password.sh`. 

1. Create a script file and add shebang at the beginning

#!/bin/bash

2. Check whether the script is being executed with superuser privileges. (Root user id number is 0)

if [[ "${UID}" -ne 0 ]]
then
   echo 'Please run this script with sudo or as root.'
   exit 1
fi

3. Use the read command to get the username (login).
read -p 'Enter the username to create: ' USER_NAME

4. Use the read -p command to get the real name (contents for the description field).

read -p 'Enter the name of the person or application that will be using this account: ' COMMENT

5. Use read -sp command to get the password.
read -sp 'Enter the password to use for the account: ' PASSWORD

6. Create the new user account by using the previously saved variables

useradd -c "${COMMENT}" -m ${USER_NAME} 2> /dev/null 

7. Check to see if the useradd command succeeded.
Use +? to check the last process. (0 ,1 or 127)
if [[ "${?}" -ne 0 ]]
then
  echo 'This username is already exit. Please select different username '
  exit 1
fi

8. Set the passwrod for the new user
echo ${PASSWORD} | passwd --stdin ${USER_NAME}

9. Check to see if the passwd command succeeded.
if [[ "${?}" -ne 0 ]]
then
  echo 'The password for the account could not be set.'
  exit 1
fi

10. Make sure that user changes password on first login

passwd -e ${USER_NAME}

10. Display user properties 
echo
echo 'username:'
echo "${USER_NAME}"
echo
echo 'password:'
echo "${PASSWORD}"
