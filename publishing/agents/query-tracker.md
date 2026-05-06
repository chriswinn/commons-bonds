# Query Tracker

**Status.** Skeleton — first entries land in Wave 1 (Nov 2026) per cascade plan.

**Purpose.** One row per agent query. Discipline: log on send, update on response. The tracker is what prevents accidentally simultaneous queries to exclusivity-only agents and what surfaces patterns when 0/8 in a wave returns interest.

## Wave plan

- **Wave 1 (Nov 2026)** — 8 queries. Priority-A agents.
- **Wave 2 (Jan 2027)** — 8 queries. Priority-B agents. Incorporates Wave 1 feedback.
- **Wave 3 (Mar 2027)** — 9 queries. Priority-C agents. Incorporates Wave 1 + 2 feedback.

## Tracker

| # | Agent | Agency | Wave | Date sent | Simultaneous OK? | Status | Response date | Outcome | Personalization used | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TBD | TBD | — | — | — | — | — | — | — | — |

## Status values

- `queried` — query sent, no response yet
- `pass-no-response` — exceeded agent's stated response window with no reply (default to "no")
- `pass-explicit` — explicit pass; capture any reasoning given
- `request-partial` — agent wants partial materials (sample chapters, partial manuscript)
- `request-full` — agent wants full manuscript / proposal
- `offer` — offer of representation
- `withdrawn` — query withdrawn (e.g., signed with someone else)

## Discipline

- Update the tracker the same day as send / response.
- Never query an agent whose `simultaneous OK?` is false while another query is open with a same-policy agent.
- After each wave, before the next, write a one-paragraph wave-retro at the bottom: what worked, what didn't, what to change in the query letter.

## Wave retros

(Append after each wave.)
