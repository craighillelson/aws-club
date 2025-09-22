# Create a Secret and Access It From the CLI
1. Navigate to Secrets Manager through the Services menu.
1. Click on Store a new secret.
    1. Select the secret type: Other type of secrets (for custom key-value pairs)
        Credentials for RDS database, Redshift, DocumentDB, or others if applicable.
    1. Enter the secret information: For custom secrets, add key-value pairs. For database credentials, fill in username, password, and database details.

1. Click Next.
1. Provide a name for your secret (e.g., MySecret) and optionally add a description.
1. Configure automatic rotation if needed, or choose to disable rotation.
1. Review all settings, then click Store.
1. Access the secret using the AWS CLI:

    `aws secretsmanager get-secret-value --secret-id MySecret`