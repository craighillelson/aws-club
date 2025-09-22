# Enable MFA Delete on an S3 Bucket 
Important Note: MFA Delete can only be enabled by the AWS account root user, not by IAM users, even if they have full admin privileges. Also, the bucket must have versioning enabled.

1. Enable Versioning on the Bucket (if not already enabled):

    ```
    aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled
    ```
1. Enable MFA Delete:

This must be done using the AWS CLI or SDK, as it's not available in the AWS Management Console. You'll need to use the root user's access keys and MFA device.

Using AWS CLI:
    
    aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa "arn-of-mfa-device mfa-code"
    
Replace:

- your-bucket-name with your actual bucket name
- arn-of-mfa-device with the ARN of your MFA device
- mfa-code with the current code from your MFA device

Verify MFA Delete is Enabled:

You can check if MFA Delete is enabled using:

```
aws s3api get-bucket-versioning --bucket your-bucket-name
```
The output should include `"MFADelete": "Enabled"`