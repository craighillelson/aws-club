# Secrets Manager 
Secrets Manager is AWS's service for storing and rotating sensitive credentials.

**What it does:**

- **Secure storage** - Encrypts secrets (passwords, API keys, tokens) at rest and in transit
- **Automatic rotation** - Changes credentials on a schedule (especially useful for RDS databases)
- **Fine-grained access** - IAM controls who/what can retrieve secrets
- **Versioning** - Keeps history of secret values
- **Cross-service integration** - Works natively with RDS, Redshift, DocumentDB
- **Auditing** - CloudTrail logs every access to secrets

# Challenge
Create a Secret and Access It From the CLI
    
➡️ [instructions](secrets-manager-create-secret-and-access-it.md)