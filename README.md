# Hostile Tweets Processor

## Overview
This project fetches hostile tweets from a MongoDB Atlas database and processes them to detect:
- The rarest word in each tweet
- Sentiment (positive, neutral, negative)
- Weapons mentioned (from a blacklist)

The processed data is exposed via a FastAPI endpoint.

## Folder Structure
app/ # Python code
data/ # Weapons blacklist
infra/ # OpenShift/K8s manifests
scripts/ # Build & deploy scripts
Dockerfile
requirements.txt
README.md