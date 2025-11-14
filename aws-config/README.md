# AWS Config

AWS Config is a service that tracks and evaluates your AWS resource configurations.

**What it does:**

- **Configuration tracking** - Records the state of resources over time (what changed, when, who changed it)
- **Configuration history** - Look back and see how resources were configured at any point
- **Compliance rules** - Define rules (like "all S3 buckets must have encryption") and get alerts when violated
- **Automated remediation** - Automatically fix non-compliant resources
- **Relationship mapping** - Shows how resources are connected

# Challenges
- Create a rule that checks if an S3 bucket has versioning enabled. If it does not, enable versioning.
- Create a rule that checks if an S3 bucket has server-side encryption enabled. If it does not, enable server-side encryption.
- Create a rule that checks if an S3 bucket has logging enabled. If it does not, enable logging.
- Create a rule that checks if an S3 bucket has public access blocked. If it does not, block public access.
- Create a rule that checks if an S3 bucket has a lifecycle policy. If it does not, create a lifecycle policy that transitions objects to Glacier after 30 days and deletes them after 60 days.
- Create a rule that checks if HTTP connections are disallowed for an S3 bucket. If they are allowed, disallow them.