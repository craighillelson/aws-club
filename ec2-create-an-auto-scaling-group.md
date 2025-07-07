# Create an Auto Scaling Group

## Sign into the AWS Console
1. Go to https://console.aws.amazon.com/
1. Sign in with your IAM user credentials
1. In the AWS Management Console, click on "Services" at the top. Under "Compute", click on "EC2".

## Create a Launch Template:
1. In the EC2 dashboard, click on "Launch Templates" in the left sidebar
1. Click "Create launch template"
1. Provide a name for your launch template
1. Under "Amazon machine image (AMI)", select an Amazon Linux 2 AMI
1. For "Instance type", select t2.micro
1. Select or create a key pair
1. Under "Network settings", choose a VPC and subnet
1. Configure security groups as needed
1. Add any additional configuration you need (e.g., user data)
1. Click "Create launch template"

## Create an Auto Scaling Group:
1. In the EC2 dashboard, click on "Auto Scaling Groups" in the left sidebar
1. Click "Create Auto Scaling group"
1. Enter a name for your Auto Scaling group
1. Select the launch template you just created
1. Click "Next"
1. Configure Auto Scaling group details:
        Choose the VPC and subnets where you want to launch instances
        Click "Next"
1. Configure advanced options:
        You can leave the default settings or configure load balancing if needed
        Click "Next"
1. Configure group size and scaling policies:
    - Set "Desired capacity" to 2
    - Set "Minimum capacity" to 2
    - Set "Maximum capacity" to 2 (or higher if you want to allow scaling up)
    - You can add scaling policies here if you want automatic scaling, but for this example, we'll keep it simple
    - Click "Next"
1. Review:
        Review your Auto Scaling group configuration
        Click "Create Auto Scaling group"
1. Verify:
        Your Auto Scaling group will now be created
        Go back to the EC2 dashboard and click on "Instances"
        You should see two t2.micro instances being launched
1. Monitor:
        In the EC2 dashboard, under "Auto Scaling Groups", select your new ASG
        You can monitor the status and health of your instances here
1. Delete one instance:
    1. In the EC2 dashboard, click on "Instances"
    1. Select one of the instances in your Auto Scaling group
    1. Click on "Actions" > "Instance State" > "Terminate"