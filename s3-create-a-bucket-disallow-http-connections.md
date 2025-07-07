# Create a Bucket in S3 and Disallow HTTP Connections

## 1. Create a new S3 bucket

1. Click the "Create bucket" button
1. Enter a globally unique bucket name 
1. Choose the AWS Region where you want the bucket to reside
1. Leave all other settings as default for now
1. Click "Create bucket" at the bottom of the page

## 2. Upload an object to the bucket

1. Click on the name of your newly created bucket
1. Click the "Upload" button
1. Click "Add files" and select the file you want to upload
1. Click "Upload" at the bottom of the page

## 3. Edit bucket-policy.json

1. Edit the bucket-policy below, replacing "your-bucket-name" with the actual name of your bucket.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "PublicReadGetObject",
               "Effect": "Allow",
               "Principal": "*",
               "Action": "s3:GetObject",
               "Resource": "arn:aws:s3:::{your-bucket-name/*}"
           },
           {
               "Sid": "ForceSSLOnlyAccess",
               "Effect": "Deny",
               "Principal": "*",
               "Action": "s3:*",
               "Resource": [
                   "arn:aws:s3:::{your-bucket-name}",
                   "arn:aws:s3:::{your-bucket-name/*}"
               ],
               "Condition": {
                   "Bool": {
                       "aws:SecureTransport": "false"
                   }
               }
           }
       ]
   }
   ```
1. Save the file as `bucket-policy.json`.

## 4. Configure bucket policy to permit GET requests:

1. In your bucket's management page, click on the "Permissions" tab
1. Scroll down to "Bucket policy" and click "Edit"
1. Paste the following policy (replace "your-bucket-name" with your actual bucket name):

## 5. Test the policy:

1. Open a new browser tab
1. Enter the URL of the object you uploaded, which should look like this:
   ```
   https://{your-bucket-name}.s3.amazonaws.com/{your-object-name}
   ```
   If the policy is set correctly, you should be able to view the object in your browser
1. Try to connect to the object over HTTP (`http://{your-bucket-name}.s3.amazonaws.com/{your-object-name}`). You should receive an error indicating that the connection is not allowed.