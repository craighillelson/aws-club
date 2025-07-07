# Create an IAM user with AdministratorAccess 

## 1. Sign in to the AWS Management Console

1. Go to [aws.amazon.com](https://console.aws.amazon.com/)
1. Sign in with your root account credentials

## 2. Navigate to IAM

1. In the AWS Management Console, click on "Services" at the top
1. Under "Security, Identity, & Compliance", click on "IAM"

## 3. Create a new IAM User

1. In the IAM dashboard, click on "Users" in the left sidebar
1. Click the "Add user" button
1. Enter a username for the new IAM user
1. Under "Select AWS access type", choose "AWS Management Console access"
1. You can either allow AWS to auto-generate a password or create a custom password
1. Click "Next: Permissions"

## 4. Attach AdministratorAccess Policy

1. On the "Set permissions" page, click on "Attach existing policies directly"
1. In the search box, type "AdministratorAccess"
1. Check the box next to "AdministratorAccess"

## 5. Review and Create the User

1. Review all the information to ensure it's correct
1. Click "Create user"