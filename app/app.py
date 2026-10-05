import os
from datetime import datetime, timezone
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        app_version=os.getenv("APP_VERSION", "Local"),
        build_time=os.getenv("BUILD_TIME", "Local Build"),
        region=os.getenv("AWS_REGION", "ap-south-1"),
        environment=os.getenv("DEPLOY_ENV", "AWS ECS Fargate")
    )

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "service": "aws-ecs-cicd-app",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/api/status")
def status():
    return jsonify({
        "application": "aws-ecs-cicd-app",
        "status": "Operational",
        "platform": "AWS ECS Fargate",
        "region": os.getenv("AWS_REGION", "ap-south-1"),
        "ci_cd": "GitHub Actions",
        "container": "Docker",
        "registry": "Amazon ECR",
        "infrastructure": "Terraform",
        "version": os.getenv("APP_VERSION", "Local"),
        "build_time": os.getenv("BUILD_TIME", "Local Build")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)