# PROJECT MANIFEST: ZONE-GPTP
# Status: Core Scaffolding Complete (Microservice Architecture)
# Date: February 2026

## 1. Core Directives (Immutable)
- **Primary Goal:** Multi-agent business intelligence and operational management.
- **Anti-Aura Policy:** The term "Aura" is strictly legacy. Use "Ecosystem" or "Experience."
- **Grounding Strategy:** Retrieval-Augmented Generation (RAG) via CSV/Markdown files.
- **Tone:** Professional, data-driven, strategic, and zero-inference.

## 2. Repository Architecture (GitHub: ZONE-GPTP)
- **/core:** FastAPI server, RBAC Security, Audit Logging (audit.py).
- **/agents:** Segmented logic for [Compliance, Customer Service, Strategy, Accounting].
- **/tools:** functional scripts for [Web Search, CSV Reader, Internal Ticketing].
- **/knowledge_vault:** Source of truth for [Peddler Data, Inventory, Routes, Canonical Corpus].
- **/deploy:** Dockerized environment (Dockerfile, compose.yaml).

## 3. Knowledge Vault Schemas
- **Peddlers:** [Peddler_ID, Full_Name, Vehicle_Type, Route_Assigned, Status]
- **Inventory:** [Product_ID, Product_Name, Category, Unit_Price, Stock_Level]
- **Routes:** [Route_ID, Zone_Name, Primary_Street, Permit_Status]

## 4. Current Engineering State
- The Brain is built as a **Decoupled Microservice** (FastAPI).
- It is designed to be called by an external Frontend UI via the `/process` endpoint.
- All interactions are logged in `brain_audit.log` for security.
- The "Strategy Brain" is configured to synthesize Market Watch data with internal CSVs.

## 5. Next Planned Phase
- Integration of the "Engineering Thread" UI to the Brain API.
- Bulk population of the Canonical Corpus within the knowledge_vault.
- Automation of weekly strategic growth reporting.