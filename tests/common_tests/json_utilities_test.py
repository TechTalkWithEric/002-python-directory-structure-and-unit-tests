import unittest
from common.json_utilities import JsonUtilities


class JsonUtilitiesTest(unittest.TestCase):
    def test_string_to_json(self):
        print('testing test_string_to_json')    
        event = JsonUtilitiesTest.get_api_gateway_event_payload()
        body_string = event['body']
        body_json = JsonUtilities.convert_string_to_json(body_string)
        file_name = body_json["file_name"]
        self.assertEqual(file_name, "file-1234.csv")

    @staticmethod
    def get_api_gateway_event_payload():
        event = {
            "resource": "/files-create-upload-request",
            "path": "/files-create-upload-request",
            "httpMethod": "POST",
            "headers": "null",
            "multiValueHeaders": "null",
            "queryStringParameters": "null",
            "multiValueQueryStringParameters": "null",
            "pathParameters": "null",
            "stageVariables": "null",
            "requestContext": {
                "resourceId": "igfq5e",
                "resourcePath": "/files-create-upload-request",
                "httpMethod": "POST",
                "extendedRequestId": "FmsN_Gi-oAMFYjQ=",
                "requestTime": "27/May/2023:23:09:00 +0000",
                "path": "/files-create-upload-request",
                "accountId": "1111111111111",
                "protocol": "HTTP/1.1",
                "stage": "test-invoke-stage",
                "domainPrefix": "testPrefix",
                "requestTimeEpoch": 1685228940500,
                "requestId": "403107f5-edcb-4401-bb09-384d77cdd455",
                "identity": {
                    "cognitoIdentityPoolId": "null",
                    "cognitoIdentityId": "null",
                    "apiKey": "test-invoke-api-key",
                    "principalOrgId": "null",
                    "cognitoAuthenticationType": "null",
                    "userArn": "arn:aws:sts::1111111111111:assumed-role/AWSReservedSSO_AWSAdministratorAccess_4f6f06580fb4fad7/user-name-admin",
                    "apiKeyId": "test-invoke-api-key-id",
                    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
                    "accountId": "1111111111111",
                    "caller": "AROA56TU6Z7QLKWNYJ4TT:user-name-admin",
                    "sourceIp": "test-invoke-source-ip",
                    "accessKey": "ASIA56TU6Z7QDTUS5M57",
                    "cognitoAuthenticationProvider": "null",
                    "user": "AROA56TU6Z7QLKWNYJ4TT:user-name-admin"
                },
                "domainName": "testPrefix.testDomainName",
                "apiId": "6p7rfhkpo0"
            },
            "body": "{\n    \"file_name\": \"file-1234.csv\", \"user_id\": \"dev-234523578@1\"\n\n}",
            "isBase64Encoded": "false"
        }

        return event

if __name__ == '__main__':
    unittest.main()
    