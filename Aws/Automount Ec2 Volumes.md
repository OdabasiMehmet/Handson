AUTOMOUNT EBS VOLUMES AND PARTITIONS ON REBOOT

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