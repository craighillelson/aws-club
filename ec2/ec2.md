# EC2 Challenges

*Note: AMIs are region specific. If you create an AMI in one region, you will not be able to use it in another region.*

- Create an auto-scaling group with at least two instances using a launch template. Delete one of the instaces in the group. See if it is replaced.

    ➡️ [step by step instructions](ec2-create-an-auto-scaling-group.md)

- Create an AMI and use it to launch a new instance.

    ➡️ [instructions for creating an AMI](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html)

- Create a Lifecycle policy for an EBS volume that creates a snapshot every 24 hours and retains the last 3 snapshots.
- Create a user data script that installs and starts a web server on an EC2 instance at launch