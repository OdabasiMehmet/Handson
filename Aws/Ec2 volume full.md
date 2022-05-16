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
8. From the drop down menu, choose your instance and attach the new volume 
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
20. Create a new file and then check with ls in the mp1 folder
sudo touch /mnt/mp1/hello.txt
ls /mnt/mp1


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

# PART 2 - EXTEND EBS VOLUME WITH PARTITIONING

## Create new volume

1. Create another volume  with 5 GB in the same AZ "us-east-1" and attach it to the instance
   lsblk --> list volumes --> updated
   df -h -->show the used and available capacities --> not updated, old volumes

2. Before moving on to making the partition we can check the current partitions
sudo fdisk -l

## Make partition-1

3. To start partitioning use command:
   sudo fdisk /dev/xvdg # This command will let you in fdisk utility menu
4. Write n for new partition and click eneter for a new partition
    n
5. Choose primary and continue
    p
6. Enter partition number from 1-4
    1
7. Choose partition size
    First just press enter without entering a value than enter +2G to make it a 2GB partition
       --> +2G
8. Repeat the new partition commands for the second partition
   n --> p --> 2 --> From this point just press enter two times and it will start from 2GB to the end of 5GB

9. Write w to leave the fdisk utility
    w
10. lsblk will show the partitioned state but df -h will not show the new volume
because we have not formatted the new volume yet.
11. Format the new partitions seperately like they are two different volumes
    sudo mkfs -t ext4 /dev/xvdg1 --> This will format 1.partition
    sudo mkfs -t ext4 /dev/xvdg2 --> This will format 2.partition
12. Create a mounting point path for new volumes seperately
    sudo mkdir /mnt/mp2 --> For the 1.partition
    sudo mkdir /mnt/mp3 --> For the 2.partition
13. Mount the new volumes to the mounting point patha
    sudo mount /dev/xvdg1 /mnt/mp2/ --> For the 1.partition
    sudo mount /dev/xvdg2 /mnt/mp3/ --> For the 2.partition
14. Now lsblk and df-h will show updated volumes
15. Create a new file to see whether it will stay after enlarging the volume in the next part
    sudo touch /mnt/mp3/helloguys.txt
    ls  /mnt/mp3/

## Enlarge capacity 
16. Now we will enlarge the third volume that we partitioned.
   Go to the console and increase the third volume from 5 GB to 6gb
17. If you use lsblk you wil see updated total 6Gb but the partitioned part will still show 5GB(2+3)
    lsblk
18. Now we have to resize the 3GB partition that we created earlier. Because the partitioned ended at the 
    end of the 3GB partition  which was xvdg2 
    sudo growpart /dev/xvdg 2 # Here there is a space between xvdg and 2 because we worked on the 2nd partition of xvdg
19. Finally we have to format the newly changed xvdg2 by copying format of the xvdg to xvdg2
    sudo resize2fs /dev/xvdg2 --> Now df -h will show updated
20. Check if the files are still there
    ls  /mnt/mp3/ --> Yes, they are still there


# PART 3 EXTEND ROOT VOLUME

1. Originally, root volume is actually partitioned but only 1 partition
2. Go to the console and modify the root volume to 12Gb for the hands on study
3. We need to extend partition 1 on the root volume .
   sudo growpart /dev/xvda 1
4. Now Resize the xfs file system on the extended partition.
   sudo xfs_growfs /dev/xvda1 # Root formatı xfs yani farklı olduğu için bu kodu kullandık


# PART 4 - AUTOMOUNT EBS VOLUMES AND PARTITIONS ON REBOOT

1. If we reboot we will see that configuration is gone
2. So before reboot we make a copy of fstab file which keeps configuration of formatting
3. Back up the /etc/fstab file.
   sudo cp /etc/fstab /etc/fstab.bak
4. Modify the fstab file with an editor like nano
   sudo nano /etc/fstab 
5. Add the following info to the existing.(UUID's can also be used)
 /dev/xvdf       mnt/mp1   ext4    defaults,nofail        0       0
 /dev/xvdg1      mnt/mp2   ext4  defaults,nofail        0       0
 /dev/xvdg2      mnt/mp3   ext4  defaults,nofail        0       0

6. Ctrl O --> Enter --> Ctrl X 
7. Now you can reboot and see that nothing changed
# NOTE: You can use "sudo mount -a" to mount volumes and partitions after editing fstab file without rebooting.