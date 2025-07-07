# aws-club
This repo contains a number of progressive AWS challenges. After the Inital Setup, you will find challenges grouped by AWS service. Each challenge describes what is to be accomplished in broad terms and is followed by a link to step by step instructions.

As a reminder, be sure to delete any resources you create in AWS to avoid unexpected charges. 

# Initial Setup

If you alredy have an AWS account, you can skip this section.

Create an AWS account 

➡️ [step by step instructions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)

Turn MFA on for the root user

➡️ [step by step instructions](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-step3.html)

Create an IAM user with AdministratorAccess 

➡️ [step by step instructions](setup-create-iam-user-with-administratoraccess.md)

***Note**: Following this step will allow you to use the AWS Management Console without using your root account. It is a best practice to use an IAM user with AdministratorAccess for daily tasks. Only use the root account when absolutely necessary.* 

Create a budget

➡️ [step by step instructions](setup-create-budget.md)
    
# Challenges
## S3

Create an S3 bucket, upload a picture of a cute dog, and access the picture over the web.

➡️ [step by step instructions](s3-upload-and-access-a-pic-of-a-cute-dog.md)

Create a static website with AWS S3

➡️ [step by step instructions](s3-create-a-static-website.md)

Create an S3 bucket and upload an object. Apply a policy that allows a user to view the object and disallows connections over HTTP.

➡️ [step by step instructions](s3-create-a-bucket-disallow-http-connections.md)

Create a pre-signed URL.

➡️ [step by step instructions](s3-create-a-pre-signed-url.md)

Turn on MFA Delete for an S3 bucket.

➡️ [step by step instructions](s3-enable-mfa-delete.md)

## VPC

Create a VPC using the VPC and more feature

➡️ [step by step instructions](vpc-create-vpc-using-vpc-and-more.md)

## EC2

Create an auto-scaling group with at least two instances using a launch template. Delete one of the instaces in the group. See if it is replaced.

➡️ [step by step instructions](ec2-create-an-auto-scaling-group.md)