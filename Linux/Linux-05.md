# Shell Scripting Basics Hands On Study
## Part 1 - Shell Scripting Basics
1. Create a folder and name it shell-scripting and go into the folder

```bash
--> mkdir shell-scripting && cd shell-scripting
```
2. Create a script file named `script.sh`. The script should print out Hello World

```bash
#!/bin/bash
echo "Hello World"
```
3. Make the script executable by adding execute permisson.

```bash
chmod +x script.sh
```
4. Execute the script
```bash
./script.sh
```

5. Modify the script file by adding other commands and execute again

```bash
#!/bin/bash
echo "hello"
date
pwd
ls
```

6. Add a comment to some of the commands to see how comments affect the script

```bash
#!/bin/bash
echo "hello"
# date
pwd # This is an inline comment
# ls
```
7. Use HEREDOC syntax to create a multiline comment. Use two HEREDOC comments and 
include cat command to one of them to see the difference. Cat will work as a command and will
print the HEREDOC but without cat command it will be just a multiline comment.

```bash
#!/bin/bash

cat << EOF
Welcome to the Linux Lessons.
This lesson is about the shell scripting
EOF

<< multiline-comment
pwd
ls
Everything inside the
HereDoc body is
a multiline comment
multiline-comment
```

## Part 2 - Shell Variables

1. Create a new file and name it `variable.sh`.

```bash
#!/bin/bash
NAME=Michael
echo $NAME
```

2. Make the script executable and then execute it.

```bash
chmod +x variable.sh && ./variable.sh
```
3. Create a new variable commands.sh and assign a command to the variable

```bash
CURR_DIRECTORY=$(pwd)
echo $CURR_DIRECTORY
```
4. Make the script executable and execute it. 

```bash
chmod +x commands.sh && ./commands.sh
```
5. Modify the script and add echo command and include the new variable in the string requested with the echo command.
```bash
#!/bin/bash
CURR_DIRECTORY=$(pwd)
echo "Welcome, your working directory is $CURR_DIRECTORY."
```
6. Execute the script 
```bash
./commands.sh
```

7. Use read command to store input into a new variable

```bash
echo "Enter your name"; read name
```
8. Creata new file read.sh and write a script with read command
```bash
#!/bin/bash
echo "Enter your age: "
read AGE
echo "Welcome $AGE"
```
9. Make the file executable and execute it.

10. Modify the file  and use read -p command. Now with -p you do not need the initial echo

```bash
read -p "Enter your name: " NAME
echo "Welcome $NAME"
```
11. Execute file

12. When entering sensitive information use `read -s`
```bash
read -s -p "Enter your password: " PASSWORD
echo -e "\nYour password is $PASSWORD"
```

13. Create an array of Linux distributions

```bash
DISTROS[0]="ubuntu"
DISTROS[1]="fedora"
DISTROS[2]="debian"
DISTROS[3]="centos"
DISTROS[4]="alpine"
```
14. Create an array of devops_tools using another method
```bash
devops_tools=("docker" "kubernetes" "ansible" "terraform" "jenkins")
```

15. Call specific array items by index numbers

```bash
echo ${DISTROS[0]}
echo ${DISTROS[1]}
```

16. Call every item in the array

```bash
echo ${DISTROS[@]}
```

17. Check the number of elements.

```bash
echo ${#DISTROS[@]}
```

## Part 3 - Simple Arithmetic

1. Use `expr` command to print  the value of expression to standard output.
Do not leave any whitespace 

```bash
expr 3 + 5
expr 6 - 2
expr 7 \* 3
expr 9 / 3
expr 7 % 2
```

2. Create a simple calculator. Create a file and name it `calculator.sh`.

```bash
#!/bin/bash
read -p "Input first number: " first_number
read -p "Input second number: " second_number

echo "SUM="`expr $first_number + $second_number`
echo "SUB="`expr $first_number - $second_number`
echo "MUL="`expr $first_number \* $second_number`
echo "DIV="`expr $first_number / $second_number`
```
3. Make the script executable. 

```bash
chmod +x calculator.sh
```

4. Use let command to do an arithmetic operation and save the output to a file.
 Do not use whitespace if you dont use quotes

```bash
let sub=8-4
echo $sub
```

5. Use let to increase or decrease the variable by 1 

```bash
x=5
let x++
echo $x

y=3
let y--
echo $y
```

6. Use double parentheses for arithmetic expressions. Create a varibale sum by adding 2 and 3 using with double parentheses. 

```bash
sum=$((3 + 5))
echo $sum
```
7. Create a calculator using double paranthesis by creating a file and name it to my_calc.sh

```bash
#!/bin/bash
read -p "Enter first number: " num1
read -p "Enter second number: " num2

sum=$(($num1 + $num2)) 
sub=$(($num1 - $num2)) 
mul=$(($num1 * $num2)) 
div=$(($num1 / $num2)) 


echo "SUM=$sum"
echo "SUB=$sub"
echo "MUL=$mul"
echo "DIV=$div"
