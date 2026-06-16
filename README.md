# OluPay 2.0: AWS Cloud Infrastructure

## Overview
OluPay is a Lagos-based fintech scale-up. This repository contains the architecture and infrastructure deployment for OluPay 2.0, designed to handle high-throughput financial transactions (up to 2 million users) with strict security, high availability, and automated scaling. 

## Architecture Diagram


## Core AWS Services Implemented
* **Networking:** Custom VPC, Public/Private Subnets, IGW, Bastion Host
* **Compute:** EC2 Auto Scaling Groups, Application Load Balancer (ALB)
* **Storage:** Amazon S3 (Static Hosting, Versioning, Cross-Region Replication)
* **Databases:** Aurora MySQL (Ledger), DynamoDB (Merchant Catalog), ElastiCache Redis (OTP)
* **Serverless & Integration:** AWS Lambda, API Gateway, SQS, SNS
* **Observability:** CloudWatch Dashboards, Alarms, and Logs Insights

## Security Highlights
* All databases are deployed in isolated private subnets.
* Strict least-privilege IAM roles utilized across all services.
* Security Groups configured to prevent public access to backend resources.

## How to Test
