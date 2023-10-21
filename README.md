# RedshiftMicroservice
An example of a lambda microservice that runs redshift queries, logs results, and logs execution times. 

This repository contains the code and necessary configurations to deploy a Dockerized AWS Lambda function via GitHub Actions. It is structured to automate the deployment process, ensuring a smooth and error-free release cycle.

## **Repository Structure**

- **`.github/workflows/`**: Contains GitHub Actions workflow for CI/CD.
- **`docker/`**: Contains the Dockerfile and application code.
- **`cloudformation/`**: Contains CloudFormation templates for setting up IAM roles.
- **`.gitignore`**: Specifies intentionally untracked files that Git should ignore.
- **`README.md`**: Documentation providing an overview and setup instructions.

## **Prerequisites and Assumptions**

- You have an AWS account with necessary permissions.
- Docker is installed on your local machine.
- Basic knowledge of AWS, Docker, Lambda functions, and GitHub Actions.
- This setup assumes that the Lambda function will be deployed whenever there’s a push to the main branch.

## **Setup and Deployment**

### **1. Setting Up Environment Variables:**

   - Go to your GitHub repository, navigate to `Settings` > `Secrets`.
   - Add the following secrets:
     - `AWS_ACCESS_KEY_ID`: Your AWS access key.
     - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.

### **2. Configuration in AWS:**

   - Make sure an ECR repository is created where the Docker images will be pushed.
   - Ensure necessary permissions are in place to push images to ECR and update Lambda functions.

### **3. Local Development:**

   - Clone this repository to your local machine.
   - Navigate to the `docker/` directory to make changes to the application code or to update dependencies in `requirements.txt`.

### **4. Using GitHub Actions:**

   - The workflow is pre-configured to handle the building and deployment processes.
   - Push your changes to the main branch. GitHub Actions will automatically handle the rest.

### **5. Verifying the Deployment:**

   - After the GitHub Actions workflow completes, you can verify the deployment in the AWS Lambda console.

## **Troubleshooting**

- Ensure that the AWS credentials set in the GitHub secrets have necessary permissions.
- Make sure the Dockerfile is correctly configured to match your application’s needs.
- Ensure that the IAM roles and permissions are correctly set up in the CloudFormation template.
- Ensure you have the proper iam role permissions for GitHub actions.

## **Conclusion**

This repository is configured for a streamlined deployment of a Dockerized AWS Lambda function. Ensure all prerequisites are met and environment variables are correctly set up before initiating the deployment process.

