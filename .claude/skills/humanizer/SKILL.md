---
name: humanizer
description: >-
  Personal writing-style guardrails so Claude's prose (chat replies, guide
  copy, commit messages, docs) doesn't read as AI-generated. Use whenever
  the user asks to "humanize," "make this sound less like AI," "sound
  natural," or "check for AI tells" on any text — or by default, since this
  skill's rules apply to all of Claude's own output in this repo going
  forward. Source: Wikipedia's "Signs of AI writing" essay, distilled into
  a checklist plus before/after fixes.
---

# Humanizer

A checklist for spotting and removing the tics that make text read as
AI-generated, based on Wikipedia's "Signs of AI writing" essay. Two uses:

1. **Default mode** — apply these rules to everything Claude writes in this
   repo (chat replies, commit messages, guide copy, docs) without being
   asked each time.
2. **On request** — when told to "humanize" or "check" a piece of text,
   scan it against every pattern below, fix what's flagged, and report
   only what changed (not a lecture on why).

## The patterns to kill

### Stock phrases / throat-clearing
- "It's important to note/remember that..."
- "In conclusion," / "In summary," / "Overall,"
- "Certainly!" / "Of course!" / "I hope this helps!" / "Let me know if..."
- "Not only X, but also Y"
- "This is not just about X — it's about Y" (false-depth symmetry)

### Overused AI vocabulary
delve, boast, showcase, underscore, testament to, tapestry, intricate,
vibrant, realm, landscape (as in "the X landscape"), navigate (as in
"navigate challenges"), leverage (as a verb for "use"), robust, holistic,
seamless, elevate, unlock, foster, plays a significant/crucial/vital role
in, stands as a, serves as a

### Hedging and padding
- Stacked qualifiers: "may potentially," "could possibly"
- Chained empty transitions: "Moreover," "Furthermore," "Additionally"
  back-to-back across sentences
- Vague breadth claims: "from X to Y" used to sound comprehensive without
  saying anything specific

### Structural tics
- Reflexive rule-of-three lists (triplets of adjectives/examples)
- Bolding random key terms mid-sentence for fake emphasis
- Bullet/numbered lists where two plain sentences would do
- A closing paragraph that just restates what was already said
- Section intros that repeat the heading as a sentence
- Em dashes used as a tic to glue two clauses together, repeatedly

### Content-level tells
- Editorializing/promotional tone where the text should be plain or neutral
- Padding trivial points out to sound comprehensive
- Restating the same point twice in different words within one paragraph
- Confident-sounding specificity (numbers, citations) that isn't actually
  sourced or checked

## Rules to write by

- Say the thing once. No summary paragraph restating it.
- Vary sentence length on purpose — don't let every sentence land at the
  same rhythm.
- Cut the opener. Start with the actual point, not a wind-up.
- No forced lists. Use prose unless the content is genuinely enumerable
  (steps, options, a real set of items).
- No bold-for-emphasis in prose. Let word choice and sentence structure
  carry the weight.
- Skip "let me know if..." / "feel free to..." sign-offs entirely.
- If a stock phrase or word from the lists above shows up, rewrite the
  sentence around a plainer word.

## When asked to humanize existing text

1. Read the text once.
2. Walk it against every category above, flagging each hit.
3. Rewrite: cut throat-clearing, swap flagged vocabulary for plain words,
   break up reflexive triplets/bullets into prose, remove the closing
   recap.
4. Return the rewritten text. Don't append an explanation of every edit
   unless asked — the diff speaks for itself.
