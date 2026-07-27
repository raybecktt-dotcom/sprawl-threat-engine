# 🔍 SPRAWL THREAT ENGINE
> **Continuous Attack Surface & Threat Simulation Analysis Pipeline**

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Testing Framework](https://img.shields.io/badge/tested%20with-pytest-yellow.svg)](https://docs.pytest.org/)
[![CI Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/raybecktt-dotcom/sprawl-threat-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Sprawl Threat Engine** is an automated security scanning and threat analysis framework designed to evaluate attack surface sprawl, detect security boundary violations, and validate defensive controls across target scenarios.

---

## 🚀 Key Features

* **⚙️ Threat Analysis Engine (`src/engine.py`):** Core orchestration engine for loading threat scenarios, processing evaluation passes, and analyzing attack vectors.
* **🛡️ Security Control Layer (`src/security.py`):** Pattern matching and security validation modules built to identify exposed secrets, input anomalies, and policy violations.
* **📜 Scenario-Driven Benchmarking (`data/scenarios.json`):** Configurable threat scenario suite used to simulate target environments, system prompts, and security guardrails.
* **⚙️ Continuous Integration:** Pre-configured GitHub Actions workflow (`.github/workflows/ci.yml`) to enforce automated test collection and `pytest` execution on every push or pull request.

---

## 🏗️ Project Architecture

```text
sprawl-threat-engine/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI Workflow
├── data/
│   ├── scenarios.json      # Threat Scenarios & Target Configurations
│   └── schema.sql          # Database Schema for Scan & Threat Persistence
├── src/
│   ├── __init__.py         # Package Marker
│   ├── db.py               # Database Persistence Layer
│   ├── engine.py           # Core Threat Processing Engine
│   ├── main.py             # CLI Execution Entry Point
│   └── security.py         # Security Control & Pattern Matcher
├── tests/
│   └── (Test files)        # Automated Test Suite
├── conftest.py             # Root Pytest Module Path Resolver
├── README.md               # Project Documentation
└── .gitignore
