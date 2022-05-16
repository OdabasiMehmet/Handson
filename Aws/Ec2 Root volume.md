# EXTEND ROOT VOLUME

1. Originally, root volume is actually partitioned but only 1 partition
2. Go to the console and modify the root volume to 12Gb for the hands on study
3. We need to extend partition 1 on the root volume .
   sudo growpart /dev/xvda 1
4. Now Resize the xfs file system on the extended partition.
   sudo xfs_growfs /dev/xvda1 --> Root format is xfs so we used this command
