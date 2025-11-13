# EC2

EC2 is AWS's virtual server service.

## What it does:

- **Virtual machines** - Launch Linux or Windows servers in minutes
- **Full control** - SSH/RDP access, install any software, configure however you want
- **Flexible sizing** - Choose CPU, memory, storage, and network capacity
- **Multiple purchasing options** - On-Demand (pay by hour), Reserved (commit for discount), Spot (bid on unused capacity)
- **Placement control** - Choose regions, availability zones, even placement groups
- **Integration** - Works with EBS for storage, security groups for firewall, IAM for access

## Key Concepts
Understand the following concepts:
- [Instance types](https://aws.amazon.com/ec2/instance-types/) and use cases (compute-optimized vs memory-optimized, etc.)
- [Purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) (On-Demand, Reserved, Spot, Savings Plans)
- [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [User data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- [Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)
- [Instance lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-lifecycle.html)

# Challenges

*Note: AMIs are region specific. If you create an AMI in one region, you will not be able to use it in another region.*

- Create an EC2 using an Amazon Linux 2 AMI. Connect to it using EC2 Instance Connect.

    ➡️ [step by step instructions](ec2-create-and-connect-to-an-ec2-instance.md)
- Create an auto-scaling group with at least two instances using a launch template. Delete one of the instaces in the group. See if it is replaced.

    ➡️ [step by step instructions](ec2-create-an-auto-scaling-group.md)

- Create an AMI and use it to launch a new instance.

    ➡️ [instructions for creating an AMI](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html)

- Create a Lifecycle policy for an EBS volume that creates a snapshot every 24 hours and retains the last 3 snapshots.
- Create a user data script that installs and starts a web server on an EC2 instance at launch