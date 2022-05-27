Get user input and ask them to enter 5 different numbers. Then without using the mx function find the largest number. Instead of using pyhton, use bash script to find the largest number and provide it as an input

```bash
#!/bin/bash
COUNT=0
until [[ $COUNT -eq 5 ]] # This command will run until it returns truthy
do
    read -p “Enter a number to find greatest of them :” NUMBER
    echo $NUMBER >> text.txt
    (( COUNT++ ))
done
sort -n text.txt | tail -1

```