# Legal Research Skill

> Global legal intelligence for AI agents — case law, legislation, regulations, and sanctions screening across US, UK, EU, Africa, Canada, and Australia.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--legal-green)](https://github.com/zavora-ai/mcp-legal)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Case Law Research | 2 | Find precedents by topic/jurisdiction |
| Legislation Lookup | 2 | Find and read statutes (UK, EU, US) |
| Sanctions Screening | 1-2 | Screen entities against OFAC/EU/UN lists |

### Jurisdiction Coverage
US (Federal Register), UK (legislation.gov.uk), EU (EUR-Lex), plus sanctions from OFAC, EU, UN, and regional lists.

## Installation

```bash
git clone https://github.com/zavora-ai/skill-legal-research.git ~/.skills/skills/legal-research
```

## Requirements

**Required:** `mcp-legal` (14 tools, free public databases)
**Cross-MCP:** `mcp-crm` (customer screening), `mcp-payments` (compliance gates)

## Success Criteria

| Metric | Target |
|--------|--------|
| Sanctions speed | Screen in 1 call |
| Citation quality | Always include jurisdiction + date |
| Coverage | US, UK, EU, Africa, Canada, Australia |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
