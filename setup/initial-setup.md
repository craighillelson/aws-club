# Initial Setup Instructions

If you alredy have an AWS account, have configured an IAM user with AdministratorAccess, and have configured the AWS CLI, you can skip this section.

- Create an AWS account 

    ➡️ [step by step instructions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)

- Turn MFA on for the root user

    ➡️ [step by step instructions](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-step3.html)

- Create a group in IAM and attach the AdministratorAccess policy to it. Create a user and add it to the group. Log in as the user and verify that you can access the AWS Management Console.

    ➡️ AWS Documentation
    - [Create a group in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html)
    - [Attach a policy to a group](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#attach-policy-group-console)
    - [Add a user to a group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_add-remove-users.html)

***Note**: Following this step will allow you to use the AWS Management Console without using your root account. It is a best practice to use an IAM user with AdministratorAccess for daily tasks. Only use the root account when absolutely necessary.* 

- Create a budget

    ➡️ [step by step instructions](setup-create-budget.md)

- Grant IAM user permissions to manage budgets

    ➡️ [step by step instructions](setup-grant-iam-user-permissions-to-manage-budgets.md)

- Create Access Keys for the IAM user

    ➡️ [step by step instructions](https://docs.aws.amazon.com/keyspaces/latest/devguide/create.keypair.html)