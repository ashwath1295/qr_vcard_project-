# QR Code Generator for Contact Sharing

This project is a web-based QR Code generator that allows users to create and download QR codes for sharing their contact details. The backend is powered by AWS Lambda and API Gateway.

## Features
- Generate QR codes for name, email, and phone number.
- Download the generated QR code.
- Clean and responsive design.

## Prerequisites
- An AWS account with Lambda and API Gateway set up.
- A hosted S3 bucket for the frontend.

## Backend (Lambda) Setup
1. Create a Lambda function in AWS.
2. Use the provided `lambda_function.py` code.
3. Integrate the Lambda function with an API Gateway.
4. Deploy the API Gateway to generate a public URL.

## Live Demo
[https://d2frxdemuijcij.cloudfront.net/](https://d2frxdemuijcij.cloudfront.net/)

## Frontend Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/qr_vcard_project.git
