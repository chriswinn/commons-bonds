# feedback_no_autosend_outbound_email

**Ratified:** 2026-10-31 (author). **Class:** feedback / hard rule.

## The rule

**No session ever sends outbound correspondence. Every email is author-sent.**

This covers all outbound email without exception: interview confirmation / recording-handling
emails, citation-accuracy notifies, courtesy notifications and post-launch courtesy copies,
submission cover letters and pitch emails, agent query letters, and any outreach or follow-up.

A held or queued email's **"trigger" firing is a prompt to SURFACE it to the author for review** —
*"this trigger has fired; here is the draft and where it lives; is it still useful / relevant?
revise, send, or decommission?"* — and is **never** a send authorization. The session drafts and
flags; the author reviews, decides relevance, and sends (from their own client, or by an explicit,
in-session "send this specific message" instruction).

This extends the long-standing submission-is-author-gated discipline (CLAUDE.md: "SUBMISSION
itself… emailing the editor… requires explicit author action") to **all** outbound email, including
the courtesy/notify class that prior tracker language had framed as auto-firing on a trigger.

## Why

Author direction 2026-10-31: *"pause sending any and all held emails and just make me aware of them
so we can review them as appropriate if they ever get triggered to be sent and decide if they are
still useful, relevant, etc."* Several held emails carried trigger conditions phrased as send
authorizations (e.g., the Darity confirmation email's "publisher-interest moment → send"); those are
reframed to surface-for-review. Held drafts also age — relevance, figures, timing and framing must be
re-checked at trigger time, never assumed (verify-stale-memory discipline applies).

## How to apply

- **Never** call a send tool (`mcp__Gmail__send_message` / reply / forward, or any other outbound
  send) for correspondence without an explicit, in-session author "send it" for that specific
  message. Drafting, saving, and surfacing are fine; sending is not.
- When a held email's trigger fires, or a pre-submission notify is due, **surface it**: name the
  email, its path, what triggered it, and ask the author to decide (send / revise / decommission).
- Re-verify a held draft before any send (stale figures, closed windows, changed framing).

## Held-email inventory — snapshot 2026-10-31 (live home: `../../research/outreach/_pipeline/consent-tracker.md`)

| Email | Where | Trigger / status |
|---|---|---|
| Darity post-interview confirmation (recording-handling + Tier W/S attribution) | `research/outreach/subjects/darity/post-interview-confirmation-email_2026-05-31.md` | HELD; trigger (2) "publisher-interest" **may be live** (publishing-path hint 2026-10-31) → SURFACE, don't send; draft needs revision before any send |
| Aeon courtesy email | `publishing/essays/aeon-mask-of-abundance/courtesy-email-READY_2026-06-11.md` | Marked READY; author-send |
| VIMS Ch 3 follow-ups (Lipcius + Mann) | `research/outreach/_pipeline/interview-outreach-followups_2026-05-31_vims-ch3.md` | Drafted; wait-window (~2026-06-21) long past → likely quiet-decline; author-send only if still wanted |
| Mazzucato post-launch courtesy copy | `publishing/book-proposal/_post-launch-courtesy-copies.md` | Fires at book launch (far off); author-send |
| Chesapeake §C.1 citation-accuracy notifies (watermen/scientists/officials) | `research/outreach/_pipeline/consent-tracker.md` §C.1 | "fire pre-submission" of Atlantic-Main / Noema / NYRB / BR; courtesy (not consent gate) → surface at each essay's submission; author-send |
| Essay/op-ed cover letters + pitch emails; agent query letters | per-essay `cover-letter.md` / `pitch-email.md`; `publishing/agents/` | Author-send at submission (already gated; unchanged) |

Snapshot only — the consent tracker is the live operational home for outreach-email state.
