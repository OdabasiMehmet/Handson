 # EXTEND EBS VOLUME WITH PARTITIONING

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
