{
	"info": {
		"_postman_id": "b39000fd-155b-4ab5-b922-5315208448c4",
		"name": "Djangi User APi",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "31634558"
	},
	"item": [
		{
			"name": "User Registration",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Accept",
						"value": "application/json",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "// {\r\n//     \"name\" : \"Test User\",\r\n//     \"email\" : \"test_user02@gmail.com\",\r\n//     \"tc\" : \"False\",\r\n//     \"password\" : \"karachi12\",\r\n//     \"password2\" : \"karachi12\"\r\n// }\r\n\r\n{\r\n    \"name\" : \"Wajid Hussain\",\r\n    \"email\" : \"wajid_hussain@gmail.com\",\r\n    \"tc\" : \"True\",\r\n    \"password\" : \"karachi12\",\r\n    \"password2\" : \"karachi12\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/user/register/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"user",
						"register",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "User Login",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Accept",
						"value": "application/json",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "// {\r\n//     \"email\" : \"mehfooz.connect@gmail.com\",\r\n//     \"password\" : \"karachi12\"\r\n// }\r\n\r\n// {\r\n//     \"email\" : \"test_user05@gmail.com\",\r\n//     \"password\" : \"s\"\r\n// }\r\n\r\n{\r\n    \r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/user/login/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"user",
						"login",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "User Profile",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Accept",
						"value": "application/json",
						"type": "text"
					},
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNzQ1NzYzLCJpYXQiOjE3MDM3NDQ1NjMsImp0aSI6IjVhODJhMjRkNWFhYzQ1Y2E4NGEzYzQ2NDhhOTZlOGZlIiwidXNlcl9pZCI6NH0.8LRCdryeQiaKdB3Zg_cg5PrE2mJEKylAL_D-L9Ku2ik",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/user/profile/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"user",
						"profile",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Sharing Resource to other machine",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://192.168.18.33:5000/api/user/profile/",
					"protocol": "http",
					"host": [
						"192",
						"168",
						"18",
						"33"
					],
					"port": "5000",
					"path": [
						"api",
						"user",
						"profile",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "User Change Password",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Accept",
						"value": "application/json",
						"type": "text"
					},
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNzQ5MTUzLCJpYXQiOjE3MDM3NDc5NTMsImp0aSI6IjA2MThlN2U2MzY2OTRmMmNhMjIyM2I4ZjUwZmQ3YjA2IiwidXNlcl9pZCI6OH0.IGqG6-2ORQA8LNXijyPV8MiujOP944Wq6TkJ5d-G1RQ",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"password\" : \"karachi123\",\r\n    \"password2\" : \"karachi123\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/user/changepassword/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"user",
						"changepassword",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "User Registered Data",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Accept",
						"value": "application/json",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/user/register/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"user",
						"register",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Password Resent Send Link",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Accept",
						"value": "application/json",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n\r\n    \"email\" : \"wajid_hussain@gmail.com\"\r\n\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/user/send-reset-password-email/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"user",
						"send-reset-password-email",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Reset Password",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Accept",
						"value": "application/json",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/user/reset-password/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"user",
						"reset-password",
						""
					]
				}
			},
			"response": []
		}
	]
}