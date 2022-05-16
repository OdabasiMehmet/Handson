# How to add Volume to Ec2 instance

# PART 1 - EXTEND EBS VOLUME WITHOUT PARTITIONING
In this part, we will spin up an Ec2 instance and add a volume but we will not do partitioning

1. Launch an instance from aws console, edit network settings, change subnet "No preference" to "us-east-1a" AZ.
2. Go to volumes in EC2 and change the name to Root_volume. 
3. Go to terminal and use lsblk command to see which volumes attached to instance. 
    You should see one volume with 8GB

## Create new Volume 

4. Got EC2 Dashboard, choose volumes
5. Create a new volume in the same AZ "us-east-1" with the instance from AWS console. Choose "5 GB" for this hands on.
6. Name the voluume Ekstra1 for this handson
7. Select the new volume, click on actions menu and click attach volume.
8. From the drop down menu, choose your instance and attach the new volumelume should be listed
9. Go to terminal and use lsblk command to see which volumes attached to instance. 
    You should see two volumes: one volume with 8GB and one volume with 5GB

## Mounting Volume

10. First we will check if the attached volume is already formatted or not and has data on it.
11. Use the following command: sudo file -s /dev/xvdf
Since it is not formatted, it will show /dev/xvdf: data
12. Format the new volume with the following command to format it with ext4 formatting
sudo mkfs -t ext4 /dev/xvdf
13. Now, check again with sudo file -s /dev/xvdf
 Now we can see: /dev/xvdf: Linux rev 1.0 ext4 filesystem data, UUID=38d5fdb5-31aa-4cfb-bed7-2b7678318e5e
14. Formatting was the first step now we need to mount it.
15. First step in mounting is to create a mounting point path for new volume with the following command:
    sudo mkdir /mnt/mp1
16. Second step in mounting is to actually mount it with the following command
    sudo mount /dev/xvdf /mnt/mp1/
17. Use lsblk to check if the attached volume is mounted to the mounting point path
   We should see xvdf    202:80   0   5G  0 disk /mnt/mp1
18. To show the available space, on the mounting point path use the following command
    df -h
19. To check if there is data on it or not.
    ls  /mnt/mp1/
    We should only see lost+found because we have not created any files yet.
20. Go to the new volume and create a new file and then check with ls
cd /mnt/mp1
sudo touch hello.txt
ls
## Enlarge the new volume in AWS console and modify from terminal

21. Go to the console and modify the additional volume by enlarging capacity from 5GB to 6GB .
22. Check if the attached volume is showing the new capacity
    lsblk  --> will show updated volume
    df -h  --> will show old volume  
23. First, we need to resize the file system on the new volume to cover all available space.
    sudo resize2fs /dev/xvdf # This command will copy the format of existing 5GB file system to enlarged 1GB
24. df -h --> Now it will show updated volume
25. Now check back to see if the data still is there
    ls /mnt/mp1/
    You will see hello.txt which we created earlier

## Rebooting Instance

26. If you reboot the instance mounting point path will be gone  
    sudo reboot 
27.  When you run lsblk you will see that new volume is still attached, but not mounted
     lsblk
28. Check if the attached volume is "already formatted" or not and has data on it.
    sudo file -s /dev/xvdf # This command checks for formatting
29. Mount the new volume to the mounting point path again 
    Mounting point previously created is still there but it is cleared now, so we will mount again
    sudo mount /dev/xvdf /mnt/mp1/
30. Now run df-h and you will see it is mounted again
    df -h
31. Check and see that the data is still there
    ls  /mnt/mp1/
    You will see hello.txt which we created earlier.