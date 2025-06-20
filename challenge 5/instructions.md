# Challenge 5 Instructions

## 1. Create a new S3 bucket:

1. Click the "Create bucket" button
1. Enter a globally unique bucket name 
1. Choose the AWS Region where you want the bucket to reside
1. Leave all other settings as default for now
1. Click "Create bucket" at the bottom of the page

## 2. Upload an object to the bucket:

1. Click on the name of your newly created bucket
1. Click the "Upload" button
1. Click "Add files" and select the file you want to upload
1. Click "Upload" at the bottom of the page

## 3. Edit bucket-policy.json

1. Edit the `bucket-policy.json` file in this repo to include your bucket name
1. Save the file

## 4. Configure bucket policy to permit GET requests:

1. In your bucket's management page, click on the "Permissions" tab
1. Scroll down to "Bucket policy" and click "Edit"
1. Paste the following policy (replace "your-bucket-name" with your actual bucket name):
