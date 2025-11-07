# MCP Agent Orchestra

## Overview
This project provides an MCP (Model Context Protocol) server implementation for interacting with Jira. The server is designed to handle requests from an MCP client and execute Jira-related operations using the Jira API.

## Features
- **Tool Listing**: Lists all available tools for interacting with Jira.
- **Tool Execution**: Executes specific tools, such as fetching Jira issues or adding comments.
- **Environment Configuration**: Uses environment variables for secure and flexible configuration.

## Prerequisites
Before running the server, ensure the following are installed:

- Python 3.8 or higher
- Required Python packages (see `pyproject.toml`)
- A Jira account with API access

## Environment Variables
The server requires the following environment variables to be set:

- `JIRA_HOST`: The Jira instance host (e.g., `yourcompany.atlassian.net`)
- `JIRA_EMAIL`: The email associated with your Jira account
- `JIRA_API_TOKEN`: The API token for authentication

You can set these variables in a `.env` file:

```
JIRA_HOST=yourcompany.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd mpc-agent-orchestra
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
### Starting the Server
Run the following command to start the server:
```bash
python src/jira/server.py
```

### Connecting the Client
Ensure the client is configured to connect to the server. Update the `JIRA_SERVER_SCRIPT_PATH` environment variable or pass the server path directly when running the client:
```bash
python client.py src/jira/server.py
```

### Example Commands
Once the client is connected, you can use commands like:
- `get issue SCRUM-1`: Fetch details of the Jira issue `SCRUM-1`.
- `list tools`: List all available tools.

## Project Structure
- `src/jira/server.py`: The main server implementation.
- `src/jira/tools/`: Contains tool implementations for interacting with Jira.
- `client.py`: The MCP client for interacting with the server.

## Troubleshooting
### Common Errors
- **`[WinError 2] The system cannot find the file specified`**:
  Ensure the `JIRA_SERVER_SCRIPT_PATH` is set correctly and points to `src/jira/server.py`.
- **`ValueError: Missing required environment variables`**:
  Verify that all required environment variables are set in the `.env` file.

## License
This project is licensed under the MIT License.