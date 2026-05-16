# invoice-mcp-server
Asynchronous Model Context Protocol (MCP) financial server containerized for Azure Container Apps. Automates invoice validation, duplicate prevention via Azure Table Storage, and live SunSystems GL account status lookups via Microsoft Dataverse OData integrations.

# Invoice MCP Server

An asynchronous, production-grade Model Context Protocol (MCP) server built with Python and FastAPI. This service acts as the core transactional "brain" for the resort's automated invoice workflows, providing high-scale validation, structural ledger coding, and financial guardrails for Microsoft Copilot Studio agents.



## Core Features

*   **Double-Approval Mitigation:** Employs an ultra-fast $O(1)$ point-lookup against Azure Table Storage to reject duplicate invoice tracking submissions instantly before triggering downstream approvals.
*   **Live Ledger Status Verification:** Directly queries the Microsoft Dataverse Web API using the container's Managed Identity to verify that nominal codes are marked as `OPEN` within the SunSystems (Cloud FMS) export snapshot.
*   **Dynamic Matrix Routing:** Parses tier-bracket boundaries out of a SharePoint-synced `Approval_Matrix.xlsx` sheet to dynamically determine and return the required departmental sign-offs.
*   **Strict Security Layer:** Enforces implicit inbound OAuth 2.0 bearer-token validation via Microsoft Entra ID integration at the Azure App Ingress layer.

---

## Tech Stack & Dependencies

*   **Runtime:** Python 3.14 (Optimized Linux footprint)
*   **Frameworks:** FastMCP (Anthropic/Microsoft SDK), FastAPI, Uvicorn
*   **Cloud Infrastructure:** Azure Container Apps (ACA), Azure Table Storage, Microsoft Dataverse OData Engine
*   **Data Analysis:** Pandas, Openpyxl, Aiofiles, Aiocsv

---

## Local Sandbox Setup & Testing

To test the lookup subroutines, file handling, and database connection logic on your local machine before pushing code to the cloud:

### 1. Replicate File Storage
Create a folder directory at `C:\McpTesting\data` and add mock compliance records for your financial assets:
*   `CRR_COA.csv` (Chart of accounts keywords mapping to Nominal/T-codes)
*   `SUN_Listing.csv` (Export ledger account tracking statuses)
*   `Approval_Matrix.xlsx` (Andy's approval authority hierarchy rules)
*   `Approval_Log.csv` (Audit log of previously handled invoice lines)

### 2. Configure Environment Variables
Set the target path matching your local repository structure in your terminal profile:

**PowerShell:**
```powershell
$env:FINANCE_DATA_PATH="C:\McpTesting\data"
$env:AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=..."
$env:DATAVERSE_ENVIRONMENT_URL="[https://orgffff.crm.dynamics.com](https://orgffff.crm.dynamics.com)"
