import json

def lambda_handler(event, context):
    # Validate input
    try:
        body = json.loads(event['body'])
        name = body.get('name', '').strip()
        email = body.get('email', '').strip()
        phone = body.get('phone', '').strip()

        if not name or not email or not phone:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "All fields are required."}),
                "headers": {"Content-Type": "application/json"}
            }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Invalid request: {str(e)}"}),
            "headers": {"Content-Type": "application/json"}
        }

    # Generate vCard content
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
EMAIL:{email}
TEL:{phone}
END:VCARD"""

    # Return vCard in the response
    return {
        "statusCode": 200,
        "body": json.dumps({"vcard": vcard}),
        "headers": {"Content-Type": "application/json"}
    }
