# Case Brief Template

Use this structure when presenting legal research findings.

---

## ⚖️ {case_name}

**Citation:** {citation} | **Court:** {court} | **Date:** {decision_date}

### Case Summary

| Field | Value |
|-------|-------|
| Jurisdiction | {jurisdiction} |
| Area of Law | {area_of_law} |
| Disposition | {disposition} |
| Judge | {judge_name} |

### Key Facts

{facts_summary}

### Legal Issues

| Issue | Ruling |
|-------|--------|
| {issue_description} | {ruling} |

### Holding

{holding_summary}

### Relevance

| Factor | Assessment |
|--------|-----------|
| Precedent Strength | {precedent_strength} |
| Applicability | {applicability_rating} |
| Risk Level | {risk_emoji} {risk_level} |

{risk_emoji mapping: low=✅, medium=⚠️, high=🚨}

{if precedent_strength == "Strong": "✅ Strong precedent — favorable for argument"}
{if risk_level == "high": "🚨 Adverse precedent — consider distinguishing facts"}

---

*Generated from mcp-legal | {timestamp}*
