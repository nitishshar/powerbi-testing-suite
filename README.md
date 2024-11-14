# Power BI Test Results Viewer

## Overview
Power BI Test Results Viewer is a web application that visualizes test execution results in Power BI format. It provides an interactive dashboard for analyzing test outcomes, trends, and metrics.

## Features
- Interactive dashboard for test results visualization
- Real-time test execution monitoring
- Detailed test case analysis
- Customizable reporting views
- Integration with Power BI
- Support for multiple test frameworks

## Prerequisites
- Node.js (v14.x or higher)
- Python (v3.8 or higher)
- Power BI Desktop (latest version)
- Angular CLI (v13.x or higher)

## Project Structure 
powerbi-testresults-viewer/
├── backend/ # Python backend server
├── docs/ # Documentation files
├── src/ # Frontend source code
│ └── app/ # Angular components
├── tests/ # Test files
│ ├── features/ # BDD feature files
│ └── step_definitions/ # Step definitions
└── requirements/ # Project dependencies

## Installation

### Backend Setup
1. Create a virtual environment:
bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
2. Install backend dependencies:
bash:README.md
pip install -r backend/requirements.txt

### Frontend Setup
1. Install Node.js dependencies:
npm install
2. Install Angular CLI globally:
npm install -g @angular/cli

## Running the Application

### Start Backend Server
```bash
cd backend
python app.py
```

### Start Frontend Development Server
```bash
ng serve
```
Navigate to `http://localhost:4200/` in your browser.

## Testing

### Running Backend Tests
```bash
pytest tests/
```

### Running Frontend Tests
```bash
ng test
```

### Running E2E Tests
```bash
npm run e2e
```

## Configuration
- Configure backend settings in `config.py`
- Environment variables can be set in `.env` file
- Power BI connection settings in `powerbi-config.json`

## API Documentation
API documentation is available at `/docs/api` when running the backend server.

### API Endpoints

#### 1. Test Results

##### Get All Test Results
```http
GET /api/tests
```

**Response**
```json
{
    "status": "success",
    "data": [
        {
            "id": "test-123",
            "name": "Login Test",
            "status": "passed",
            "duration": 1.5,
            "timestamp": "2024-03-15T10:30:00Z",
            "metadata": {
                "browser": "Chrome",
                "environment": "staging"
            }
        }
    ],
    "total": 1
}
```

##### Submit Test Results
```http
POST /api/tests
Content-Type: application/json

{
    "name": "Authentication Test",
    "status": "failed",
    "duration": 2.3,
    "metadata": {
        "browser": "Firefox",
        "environment": "production"
    }
}
```

**Response**
```json
{
    "status": "success",
    "message": "Test result recorded",
    "id": "test-124"
}
```

#### 2. Dashboard Data

##### Get Dashboard Statistics
```http
GET /api/dashboard/stats
```

**Response**
```json
{
    "status": "success",
    "data": {
        "total_tests": 150,
        "passed": 130,
        "failed": 15,
        "skipped": 5,
        "success_rate": 86.67,
        "average_duration": 1.8
    }
}
```

##### Get Test Trends
```http
GET /api/dashboard/trends?period=7d
```

**Response**
```json
{
    "status": "success",
    "data": {
        "dates": ["2024-03-10", "2024-03-11", "..."],
        "passed": [45, 50, "..."],
        "failed": [5, 3, "..."],
        "duration": [1.7, 1.8, "..."]
    }
}
```

### Error Responses

```json
{
    "status": "error",
    "message": "Invalid request parameters",
    "code": "INVALID_REQUEST"
}
```

### Authentication

All API endpoints require authentication using Bearer token:

```http
Authorization: Bearer <your_api_token>
```

### Rate Limiting

- Rate limit: 100 requests per minute
- Rate limit headers included in response:
  - `X-RateLimit-Limit`
  - `X-RateLimit-Remaining`
  - `X-RateLimit-Reset`

### Query Parameters

Common query parameters supported by most endpoints:

| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number for pagination |
| limit | integer | Number of items per page |
| sort | string | Field to sort by (e.g., "timestamp") |
| order | string | Sort order ("asc" or "desc") |
| filter | string | Filter criteria (e.g., "status=failed") |

### Webhook Integration

Configure webhooks to receive real-time test result notifications:

```http
POST /api/webhooks
Content-Type: application/json

{
    "url": "https://your-server.com/webhook",
    "events": ["test.completed", "test.failed"],
    "secret": "your_webhook_secret"
}
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Guidelines
- Follow Angular style guide for frontend development
- Use PEP 8 style guide for Python code
- Write unit tests for new features
- Update documentation as needed

## Troubleshooting
Common issues and solutions:
- **Backend connection failed**: Check if Python server is running
- **Dashboard not loading**: Verify Power BI credentials
- **Test execution errors**: Ensure all dependencies are installed

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- Project Maintainer: [Your Name]
- Email: [your.email@example.com]
- Project Link: [https://github.com/yourusername/powerbi-testresults-viewer](https://github.com/yourusername/powerbi-testresults-viewer)

## Acknowledgments
- Power BI SDK
- Angular Framework
- Python Flask
- All contributors who have helped shape this project

## Version History
- v1.0.0 (2024-03-XX)
  - Initial release
  - Basic dashboard functionality
  - Test results integration