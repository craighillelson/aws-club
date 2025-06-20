# Challenge 1 Instructions

## Step 1: Create an AWS Account

1. Go to the AWS homepage [aws.amazon.com](https://aws.amazon.com/).
1. Click on "Create an AWS Account" in the upper right corner.
1. Enter your email address, create a password, and choose an AWS account name.
1. Provide your contact information, including name, address, and phone number.
1. Enter your payment information (credit card details).
1. Verify your identity by phone or text message.
1. Choose a support plan (Basic is free and sufficient for most new users).
1. Complete the account creation process.

## Step 2: Access the AWS Management Console

1. Return to [aws.amazon.com](https://aws.amazon.com/) and click "Sign In to the Console".
1. Enter your email address and password to log in as the root user.

## Step 3: Enable MFA for the Root User

1. In the AWS Management Console, click on your account name in the top right corner.
1. Select "Security Credentials" from the dropdown menu.
1. If prompted, click "Continue to Security Credentials".
1. In the "Multi-factor authentication (MFA)" section, click "Activate MFA".
1. Choose the type of MFA device you want to use (virtual MFA device is most common).
1. If you chose a virtual MFA device: a. Install an MFA app on your smartphone (e.g., Google Authenticator, Authy). b. Click "Show QR code" in the AWS console. c. Scan the QR code with your MFA app. d. Enter two consecutive MFA codes from your app into the AWS console. e. Click "Assign MFA".

## Step 4: Verify MFA Setup

1. Sign out of the AWS Management Console.
1. Sign back in as the root user.
1. You should now be prompted to enter an MFA code along with your password.
