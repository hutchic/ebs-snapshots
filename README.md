# EBS Auto Snapshots

Ansible to automatically backup all EBS Volumes on instances
tagged `EBS_backup:true` and a small bit of python to remove
old EBS backups.

# Instructions

Prerequisites:
- Docker
- AWS access credentials

```
export AWS_SECRET_ACCESS_KEY="YOUR_AWS_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="AWS_ACCESS_KEY_ID"
export AWS_REGION="us-east-1 is the default"

make snapshots
```

original credit: [Marvin Pinto](https://github.com/marvinpinto)
