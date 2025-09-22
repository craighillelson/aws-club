# aws-club
This repo contains a number of progressive AWS challenges. After the Inital Setup, you will find challenges grouped by AWS service. Each challenge describes what is to be accomplished in broad terms and is followed by a link to step by step instructions.

As a reminder, be sure to delete any resources you create in AWS to avoid unexpected charges. 

# Resources
- Start with [The Well Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Tech Fundamentals](https://learn.cantrill.io/p/tech-fundamentals)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
- [AWS YouTube Channel](https://www.youtube.com/user/AmazonWebServices)
- [AWS Skill Builder](https://skillbuilder.aws/)
- [AWS Podcasts](https://aws.amazon.com/podcasts/)
- [AWS Migration Evaluator](https://aws.amazon.com/migration-evaluator/)
- [AWS Pricing Calculator](https://aws.amazon.com/tco-calculator/)

# Initial Setup

If you alredy have an AWS account, you can skip this section.

Create an AWS account 

➡️ [step by step instructions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)

Turn MFA on for the root user

➡️ [step by step instructions](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-step3.html)

Create a group in IAM and attach the AdministratorAccess policy to it. Create a user and add it to the group. Log in as the user and verify that you can access the AWS Management Console.

➡️ AWS Documentation
- [Create a group in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html)
- [Attach a policy to a group](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#attach-policy-group-console)
- [Add a user to a group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_add-remove-users.html)

***Note**: Following this step will allow you to use the AWS Management Console without using your root account. It is a best practice to use an IAM user with AdministratorAccess for daily tasks. Only use the root account when absolutely necessary.* 

Create a budget

➡️ [step by step instructions](setup-create-budget.md)

Grant IAM user permissions to manage budgets

➡️ [step by step instructions](setup-grant-iam-user-permissions-to-manage-budgets.md)

Create Access Keys for the IAM user

➡️ [step by step instructions](https://docs.aws.amazon.com/keyspaces/latest/devguide/create.keypair.html)

# Challenges
## S3

Create an S3 bucket, upload a picture of a [cute dog](rocky.jpeg), and access the picture over the web.

➡️ [step by step instructions](s3-upload-and-access-a-pic-of-a-cute-dog.md)

Create a static website with AWS S3

➡️ [step by step instructions](s3-create-a-static-website.md)

Create an S3 bucket and upload an object. Apply a policy that allows a user to view the object and disallows connections over HTTP.

➡️ [step by step instructions](s3-create-a-bucket-disallow-http-connections.md)

Create a pre-signed URL.

➡️ [step by step instructions](s3-create-a-pre-signed-url.md)

Turn on MFA Delete for an S3 bucket.

➡️ [step by step instructions](s3-enable-mfa-delete.md)

Set up lifecycle rules for an S3 bucket to transition an object to Glacier after 30 days and delete it after 60 days.

➡️ [Transitioning objects using Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html)

## VPC

Create a VPC using the VPC and more feature

➡️ [step by step instructions](vpc-create-vpc-using-vpc-and-more.md)

## EC2

Create an auto-scaling group with at least two instances using a launch template. Delete one of the instaces in the group. See if it is replaced.

➡️ [step by step instructions](ec2-create-an-auto-scaling-group.md)

Create an AMI and use it to launch a new instance.

➡️ [instructions for creating an AMI](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html)

*Note: AMIs are region specific. If you create an AMI in one region, you will not be able to use it in another region.*

Create an encrypted EBS volume and attach it to an instance.

Create an unencrypted EBS volume and attach it to an instance. Now, encrypt the volume and attach it to the instance.

Create a Lifecycle policy for an EBS volume that creates a snapshot every 24 hours and retains the last 3 snapshots.

## DynamoDB
Create Table
1. Upload [music.csv](music.csv) to an S3 bucket.
1. Import the CSV file into a DynamoDB table named "Music".

Create a Scheduled Backup

➡️ [instructions](https://aws.amazon.com/blogs/database/set-up-scheduled-backups-for-amazon-dynamodb-using-aws-backup/)

## Secrets Manager
Create a secret in Secrets Manager and access it using the AWS CLI.

➡️ [step by step instructions](secrets-manager-create-secret-and-access-it.md)

## AWS Config
- Create a rule that checks if an S3 bucket has versioning enabled. If it does not, enable versioning.
- Create a rule that checks if an S3 bucket has server-side encryption enabled. If it does not, enable server-side encryption.
- Create a rule that checks if an S3 bucket has logging enabled. If it does not, enable logging.
- Create a rule that checks if an S3 bucket has public access blocked. If it does not, block public access.
- Create a rule that checks if an S3 bucket has a lifecycle policy. If it does not, create a lifecycle policy that transitions objects to Glacier after 30 days and deletes them after 60 days.
- Create a rule that checks if HTTP connections are disallowed for an S3 bucket. If they are allowed, disallow them.