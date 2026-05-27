# Legal Examples

## Example 1: "Screen Acme Corp for sanctions"
```
screen_entity(name: "Acme Corp", type: "company") → {match: false, checked: ["OFAC", "EU", "UN"]}
```
Response: "✅ Acme Corp — no sanctions match. Checked: OFAC (US), EU Consolidated, UN Security Council."

## Example 2: "Find UK data protection legislation"
```
search_uk_legislation(query: "data protection") → [{title: "Data Protection Act 2018", id: "ukpga/2018/12"}]
get_uk_legislation(id: "ukpga/2018/12") → full text + sections
```
Response: "Found: Data Protection Act 2018 (UK). Implements GDPR into UK law. 215 sections."
