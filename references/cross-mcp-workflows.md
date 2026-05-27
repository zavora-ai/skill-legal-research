# Legal Cross-MCP Workflows

## Legal + CRM: Customer Sanctions Check
```
CRM: get_company(id) → {name: "New Customer Inc", country: "RU"}
LEGAL: screen_entity(name: "New Customer Inc", type: "company") → check sanctions
→ If match: CRM: update_company(status: "blocked", reason: "sanctions match")
```

## Legal + Payments: Compliance Gate
```
LEGAL: screen_entity(name: recipient_name) → sanctions check
→ If clear: PAYMENTS: create_payout_intent(...)
→ If match: BLOCK payment, alert compliance team
```
