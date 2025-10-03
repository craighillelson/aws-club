# Create and Connect to an EC2 Instance
1. Search for "EC2" in the AWS Management Console and select it.
1. In the EC2 dashboard, click on "Instances" in the left sidebar
1. Click "Launch instances"
1. Name your instance (e.g., "server")

## Application and OS Images (Amazon Machine Image)
Select "Amazon Linux"

## Instance type
Select "t2.micro" (this instance type is eligible for the free tier)

## Key pair (login)   
Select "Proceed without a key pair" 

## Network settings
1. Click Edit
1. Select "Create a new security group"
1. Set a name for the security group (e.g., MyFirstEC2-SG)
1. Add a rule to allow SSH access. In the interest of security, you should restrict access to your IP address and the EC2_INSTANCE_CONNECT service. Consult the list of [AWS IP ranges JSON](https://ip-ranges.amazonaws.com/ip-ranges.json) to find the appropriate IP address range for your region. 

For example, if you are in us-east-1, you would add the following rules:

**Rule 1:**

- Type: SSH
- Protocol: TCP
- Port Range: 22
- Source: My IP

**Rule 2:**

- Type: SSH
- Protocol: TCP
- Port Range: 22
- Source: Custom
- 18.206.107.24/29 (again, for use in us-east-1, check the JSON file for your region)

## Launch Instance
1. Click "Launch instance"
1. At this point, you should receive a message that reads "Successfully initiated launch of instance (i-xxxxxxxxxxxxxxxxx)"
1. The instance ID should be a link. Click on it to go to the instance details page.
1. Click "Connect" to connect to your instance using EC2 Instance Connect. 
1. With "EC2 Instance Connect" selected, click "Connect" again.
1. You should now be connected to your EC2 instance!