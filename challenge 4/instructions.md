# Challenge 4 Instructions
1. Create an S3 bucket. Deselect "Block all public access" and select "I acknowledge that the current settings might result in this bucket and the objects within becoming public."
1. Copy the contents of "bucket-policy.json" and paste them into the "Bucket policy" section of the "Permissions" tab.
1. Upload "index.html" and "error.html" to your bucket.
1. Run the following command from the command line `aws s3 website s3://<your bucket name> --index-document index.html --error-document error.html`
1. In the "Properties" tab, scroll to the bottom of the page and copy the "Bucket website endpoint" value. Paste the copied URL into a private browsing window
