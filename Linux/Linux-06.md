# Loops

1. Create a folder and name it `loops`.

```bash
mkdir loops && cd loops
```

2. Display numbers from 1 to ten with `while loop`. Create a `script` file named `while-loop.sh`. 

```bash
#!/bin/bash

number=1

while [[ $number -le 10  ]]
do
  echo $number
  ((number++))
done
echo "Now, number is $number"
```

3. Make the script executable and execute it.

```bash
chmod +x while-loop.sh
./while-loop.sh
```

4. Create a `script` file named `until-loop.sh`. 

```bash
#!/bin/bash

number=1

until [[ $number -ge 10  ]]
do
  echo $number
  ((number++))
done
echo "Now, number is $number"
```

5. Make the script executable and execute it.

```bash
chmod +x until-loop.sh
./until-loop.sh
```

6. Create a `script` file named `for-loop.sh`. 

```bash
#!/bin/bash

echo "Numbers:"

for number in 0 1 2 3 4 5 6 7 8 9
do
   echo $number
done

echo "Names:"

for name in Joe David Matt John Timothy
do
   echo $name
done

echo "Files in current folder:"

for file in `pwd`/*
do
   echo $file
done
```

7. Make the script executable and execute it.

```bash
chmod +x for-loop.sh
./for-loop.sh
```

8. Create a `script` file named `for-array.sh`. 

```bash
#!/bin/bash

devops_tools=("docker" "kubernetes" "ansible" "terraform" "jenkins")

for tool in ${devops_tools[@]}
do
   echo $tool
done
```

9. Make the script executable and execute it.

```bash
chmod +x for-array.sh
./for-array.sh
```

10. Create a `script` file named `infinite-loop.sh`. 

```bash
#!/bin/bash

number=1

until [[ $number -lt 1  ]]
do
  echo $number
  ((number++))
done
echo "Now, number is $number"
```

11. Make the script executable and execute it.

```bash
#!/bin/bash

number=1

until [[ $number -lt 1  ]]
do
  echo $number
  ((number++))
  if [[ $number -eq 100 ]]
  then
    break
  fi
done
```

12. Execute the script.

```bash
./infinite-loop.sh
```

13. Modify the `infinite-loop.sh`. This time we do not display 10 and its multiples (10, 20 ..)

```bash
#!/bin/bash

number=1

until [[ $number -lt 1  ]]
do
  ((number++))
  
  tens=$(($number % 10))
  
  if [[ $tens -eq 0 ]]
  then
    continue
  fi

  echo $number
    
  if [[ $number -gt 100 ]]
  then
    break
  fi
done
```

14. Execute the script.

```bash
./infinite-loop.sh
```

15. Create a `script` file named `select-loop.sh`. 

```bash
#!/bin/bash

read -p "Input first number: " first_number
read -p "Input second number: " second_number

PS3="Select the operation: "

select operation in addition subtraction multiplication division exit
do
  case $operation in
    addition) 
      echo "result= $(( $first_number + $second_number))"
    ;;
    subtraction)
       echo "result= $(( $first_number - $second_number))"
    ;;
    multiplication)
       echo "result= $(( $first_number * $second_number))" 
       ;;
    division)
       echo "result= $(( $first_number / $second_number))"
    ;;
    exit)
       break
    ;;   
    *)
       echo "Wrong choice..." 
    ;;
  esac
done
```

16. Make the script executable and execute it.

```bash
chmod +x select-loop.sh
./select-loop.sh
```