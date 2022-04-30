# Hands-on Linux-01 : Managing Files in Linux

## Part 1 - Working with File Contents

- Create a folder and name it linux-lessons.

```bash
mkdir linux-lessons
cd linux-lessons
```

- Create a `text` file named `test.txt`.

```txt
Welcome to the linux lessons
line 2
line 3
line 4
line 5
line 6
line 7
line 8
line 9
line 10
line 11
line 12
line 13
line 14
Line 15
```

- Show the first 10 lines of test.txt.

```bash
head test.txt
```

- Show the first 5 lines of test.txt.

```bash
head -5 test.txt
```

- Show the last 10 lines of test.txt.

```bash
tail test.txt
```

- Show the last 5 lines of test.txt.

```bash
tail -5 test.txt
```

- Display the test.txt file on the screen.

```bash
cat test.txt
```

- Create three files with echo command and name them file1 file2 file3.

```bash
echo "this is file1" > file1
echo "this is file2" > file2
echo "this is file3" > file3
```

- Display the file1, file2 and file3 files on the screen.

```bash
cat file1 file2 file3
```

- Concatenate file1, file2 and file3 to `all.txt` file.

```bash
cat file1 file2 file3 > all.txt
```

- Create a file with `cat` command.

```bash
cat > summer.txt 
Today is cold.
Today is rainy
```

- After the last line, type and hold the Control (Ctrl) key and press d.

- View the test.txt file with the `more` command.

```bash
more test.txt
```

- View the test.txt file with the `less` command.

```bash
less test.txt
```

- The main difference between more and less is that less command is faster because it does not load the entire file at once and allows navigation though file using page up/down keys. 

- Display test.txt file in reverse.

```bash
tac test.txt
```

- Create reverse-test.txt in reverse of test.txt.

```bash
tac test.txt > reverse-test.txt
```