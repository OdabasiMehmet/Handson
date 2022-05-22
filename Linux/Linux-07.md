# Hands-on Filters and Control Operators
​
1. Create a folder and name it filters.
​
```bash
mkdir filters
cd filters
```
2. Create a `text` file named `days.txt` and enter days of the week.
​
```bash
vim days.txt
```
​
```bash
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```
3.  Display the content of days.txt.
```bash
cat days.txt
```
4. Create a `text` file named `count.txt` and enter numbers from one to eleven in string format.
​
```bash
nano count.txt
```
```text
one
two
three
four
five
six
seven
eight
nine
ten
eleven 
```
5. Display the content of count.txt.

```bash
cat count.txt
```

6. Write the content of the count.txt file in reverse order to another file named temp.txt and display the content of temp.txt in reverse order.

```bash
tac count.txt | tee temp.txt | tac
```
7. Check whether the temp.txt file created and display the content.
​
```bash
ls
cat temp.txt
```

8. Create a `text` file named `tennis.txt` by using cat command and enter four palyer names with countries.
​
```bash
cat > tennis.txt
​
Amelie Mauresmo, Fra
Justine Henin, BEL
Serena Williams, USA
Venus Williams, USA
```
>**press ctrl+d for EOF**
​
9. Display the content of tennis.txt.

```bash
cat tennis.txt
```

10. Display only the lines of tennis.txt that includes 'Williams'.
​
```bash
cat tennis.txt | grep Williams
```

10. Display the owners column (3rd column) of all the files in current directory by using cut command.
​
```bash
ls -l | cut -d' ' -f3
```

11. Display only the usernames in the ect/passwd.
​
```bash
cut -d: -f1 /etc/passwd
```

12. Create a `text` file named `mytext.txt` by using heredoc.
​
```bash
cat << EOF > meytext.txt
Work hard to achieve better
EOF
```

13. Display the content of mytext.txt.
​
```bash
cat mytext.txt
```

14. Replace or translate aer letters with 'QAZ'.
​
```bash
cat mytext.txt | tr aer QAZ
```
​
15. Delete all the vowels in the content of mytext.txt.
​
```bash
cat mytext.txt | tr -d aeiou
```
​
16. Write the whole content of mytext.txt in capital letters.
​
```bash
cat mytext.txt | tr [a-z] [A-Z]
```

17. Print line, word, and charecters for mytext.txt

-
​
```bash

wc mytext.txt
```

18. Find how many users are there in the computer.

```bash
wc -l /etc/passwd
```

19. Create a `text` file named `marks.txt` and enter several names with associated marks using heredoc
​
```bash
cat << EOF > marks.txt
aeron-9
albert-9
james-9
john-10
oliver-7
tom-7
victor-10
walter-8
EOF
```

20. Display the content of marks.txt.
​
```bash
cat marks.txt
```

21. Sort the content of marks.txt.
​
```bash
sort marks.txt
```

22. Sort the content of marks.txt in reverse order.
​
```bash
sort -r marks.txt
```

23. Display only the unique names in the content of marks.txt.
​

​
```bash
sort marks.txt | uniq
```

23. Create a `text` file named `file1.txt`.
​
```bash
cat << EOF > file1.txt
Aeron
Bill
James
John
Oliver
Walter
EOF
```

24. Create another `text` file named `file2.txt`.
​
```bash
cat << EOF > file2.txt
Guile
James
John
Raymond
EOF
```

25. Compare file1.txt and file2.txt.
​

​
```bash
sort file1.txt file2.txt ;comm file1.txt file2.txt
```

26. Run ls command and show that it is executed successfully.
​
```bash
ls
echo $?
```

27. Run lss command and show that it failed.
​
```bash
lss
echo $?
```