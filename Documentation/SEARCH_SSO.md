# Search SSO

## Purpose

Search SSO provides one team-member view across Dark Universe schedule, PQS, PM-cycle, and SuccessFactors information.

## Eligibility Logic

### Current Dark Universe Line Schedule member

Display:

- Name and SSO
- Shift
- Working days
- Relevant schedule details
- PQS module information
- PM cycle information
- SuccessFactors outstanding items or All Good

### Not on the Dark Universe Line Schedule

Display:

- Name and SSO from SuccessFactors
- SuccessFactors organization
- SuccessFactors outstanding items or All Good
- Notice that the person is not currently listed on the Dark Universe Line Schedule

Do not display Dark Universe PQS or PM information.

### Not found

Display a not-found message when the SSO is absent from both the Line Schedule and the current SuccessFactors source.

## SuccessFactors Rules

- Outstanding: `Days Until Due <= 15`
- Overdue: `Days Until Due < 0`
- Due Soon: `Days Until Due` from `0` through `15`
- All Good: no outstanding items

## Working-Day Rules

The Line Schedule uses columns from Sunday through Saturday.

- `OFF`: not scheduled to work
- Blank cell: scheduled to work

## PM Cycles

Each PM cycle appears separately with:

- Qualification
- Cycle number
- Cycle start
- Due date
- PM completion date
- Days remaining
- Cycle status
- Task number
- Evidence source

## Data Minimization

Search SSO does not display supervisor, manager, or HR Box information.

## Test Cases

1. Dark Universe SSO with PQS, PM, and SF data.
2. Non-Dark-Universe SSO with SF data only.
3. SSO with no outstanding SF items.
4. Unknown SSO.
5. Built EXE launch and search.
