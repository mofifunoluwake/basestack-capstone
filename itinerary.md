Week 1 — Foundation & Core Services (Days 1–7)
Day	Section	Tasks	Evidence to Capture
Day 1	VPC + IAM	Create custom VPC: 4 subnets (2 public, 2 private) across 2 AZs. Attach IGW. Configure route tables. Create 3 SGs (web, db, bastion).	VPC console screenshot, route tables, SG inbound rules
Day 2	IAM Roles	Create 3+ IAM roles with least-privilege policies (EC2, Lambda, RDS). Write one custom policy JSON.	IAM roles list + JSON screenshot
Day 3	EC2 + ALB + ASG	Launch template with UserData (web server). ALB in public subnets. Target group. ASG with Min=1, Desired=2, Max=3.	Launch template, ALB DNS working, ASG config, Activity history
Day 4	Bastion + Private Access	Bastion host in public subnet. SSH from bastion to private EC2.	Terminal screenshot showing bastion → private instance
Day 5	Architecture Diagram	Draw VPC layer diagram (Excalidraw/draw.io). Label subnets, SGs, IGW, ALB, ASG, bastion.	PNG exported
Day 6	S3 Static Website	S3 bucket with static site. Public access enabled (portfolio only). Versioning ON. Lifecycle rule (e.g., transition to IA after 30 days). SSE-S3/KMS encryption.	Live URL, bucket properties, lifecycle rule, encryption
Day 7	S3 Replication + Pre-signed URL	Cross-region replication to secondary bucket. Generate pre-signed URL with ≤5 min expiry. Test before/after expiry.	Replication rule, CLI command + expiry screenshots
Week 2 — Databases, Serverless, Observability (Days 8–14)
Day	Section	Tasks	Evidence to Capture
Day 8	RDS/Aurora	Aurora MySQL in private subnet. Public accessibility = NO. Choose Multi-AZ or Read Replica (justify). Create schema (5+ columns). Insert 3 sample rows.	RDS Connectivity tab, justification, SELECT * output
Day 9	DynamoDB	Write access pattern first. Create table. Create GSI. Query using GSI. Run Query vs Scan — explain cost difference.	Access pattern text, GSI tab, query result, Scan vs Query screenshots + explanation
Day 10	ElastiCache Redis	Redis cluster. Implement TTL pattern (SET/GET/TTL). Test expiry → returns (nil). Write cache-aside pattern explanation.	redis-cli TTL showing (nil), written explanation
Day 11	Lambda + API Gateway	Lambda 1 (primary business logic) → test returns 200. Lambda 2 (separate responsibility). Each has least-privilege IAM role (no *). API Gateway HTTP API (POST) → Lambda → DynamoDB write confirmed.	Lambda console, IAM role JSON, curl/Postman 200, DynamoDB item from API call
Day 12	SQS + SNS	SQS queue decoupling Lambda 1 → Lambda 2. Visibility timeout set + justified. SNS email subscription confirmed.	Queue config, Lambda 2 SQS trigger, SNS subscription confirmed + email received
Day 13	Observability	CloudWatch dashboard with 3+ services (Lambda + API Gateway + DB). Alarm with SNS action (OK or ALARM state). Lambda log stream annotated (START/END/REPORT). Logs Insights query. Error simulation → find → fix.	Dashboard screenshot, alarm console, log annotation, query result, error fix cycle
Day 14	Documentation + Submission	Complete architecture diagram (all 6 layers). GitHub repo with README. Portfolio post (LinkedIn/Twitter). Final review.	Diagram PNG, repo URL, post screenshot
