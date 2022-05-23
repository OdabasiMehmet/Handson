# sed & awk commands

1. Create a folder,name it awk_sed_handson and go into the directory

```bash
mkdir awk_sed_handson && cd awk_sed_handson
```

2. Create a file named testsed.txt and enter the following text.

```txt
Linux is an OS. Linux is life. Linux is a concept.
I like linux. You like linux. Everyone likes linux.
Linux is free. Linux is good. Linux is hope.
```

3. Replace the word “linux” with “ubuntu” in the file by using sed command.

```bash
sed 's/linux/ubuntu/' testsed.txt
```
4. Use the /1, /2 etc flags to replace the first, second occurrence of a pattern in a line. Replace the third occurrence of the word “linux” with “ubuntu” in a line.

```bash
sed 's/linux/ubuntu/3' sed.txt
```

5. Aplly the previous command but ignore case sensitivity.

```bash
sed 's/linux/ubuntu/i' sed.txt
```

6. Use the sed command to replace all the occurrences of the linux witth ubuntu .

```bash
sed 's/linux/ubuntu/g' sed.txt
```

7. Replace all the occurances by ignoring case distinctions. 

```bash
sed 's/linux/ubuntu/ig' sed.txt
```


8. Replace all the patterns from the any occurrence of “linux” word with “ubuntu” word but ignore the first one.

```bash
sed 's/linux/ubuntu/2ig' sed.txt
```

9. Replace the string only on the second line.

```bash
sed '2 s/linux/ubuntu/ig' sed.txt
```

10.  Create a file named testawk.txt 

```txt
This is line 1
This is line 2
This is line 3
This is line 4
This is line 5
```

11. Use awk to show all the lines

```bash
awk '{print}' testawk.txt
```

12. Print the lines which matches that includes "This" in them.

```bash
awk '/This/ {print}' testawk.txt
```
13. Use awk to print the second column

```bash
awk '{print $2}' testawk.txt
```

13. Display the second and fourth columns

```bash
awk '{print $2,$4}' testawk.txt
```

14. Use the delimeter –F option and separate the fields by " " space.

```bash
awk -F" " '{print $2}' testawk.txt
```
15. Use awk command as filter. 

```bash
ls -l | awk '{print $9}'
```