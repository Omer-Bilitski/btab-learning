---
name: explain-underlying-theory
description: 'Identify and explain missing theoretical foundations behind a mathematical or physics problem, proof, or confusing step supplied as an image, equations, or text. Use when the user asks why a construction is introduced, what a statement really means, which definition or theorem justifies a method, or what conceptual background they are missing. Focus on rigorous conceptual understanding rather than merely expanding algebra or solving the whole exercise.'
---

# Explain Underlying Theory

## Ground the explanation

- Inspect the supplied problem and the user's specific question before diagnosing a gap. Preserve its notation and argument. If an image is inaccessible or unclear, say so and request only the missing information; never invent its contents.
- Infer the smallest plausible conceptual gap from the question and visible work. Present uncertain diagnoses as hypotheses, not claims about the user's knowledge. Do not infer mastery from silence or a single correct calculation.
- Distinguish missing definitions, misunderstood mathematical objects, omitted assumptions, the meaning of equality or convergence, and confusion about a proof step's purpose from simple calculation gaps.
- Check terminology against actual symbols and context. Gently correct consequential misidentifications without making them the focus.
- Answer directly when enough context is available. Ask a targeted question only when competing interpretations materially change the explanation.

## Build a rigorous conceptual bridge

1. State the conceptual hinge in plain language: what makes this step belong in the argument.
2. Introduce only the necessary objects and definitions. Identify their domains, roles, and relevant assumptions. Explain new symbols.
3. State the precise definition or theorem, including decisive quantifiers such as “for every,” and the exact sense of equality, derivative, limit, or approximation.
4. Explain why the definition has this form or what the construction achieves. Separate formal definitions and deductions from intuition and physical interpretation.
5. Apply the theory to the exact line supplied. Connect every introduced object to its job in the proof. Include enough calculation to make the connection verifiable.
6. Address the user's proposed alternative fairly: determine what it proves, whether it is valid, and what remains unproved. Use one small counterexample when useful to separate the weaker claim from the required claim. Do not claim a technique is mandatory if another rigorous proof exists.
7. End with a short transferable criterion for recognizing the same principle elsewhere. Optionally ask one targeted conceptual check when useful; never require a quiz or delay the explanation.

## Scope and presentation

- Keep these skill instructions in English; explain to this user in Hebrew by default unless another language is requested. Keep explanations in one language, with an English technical term in parentheses on first mention only when useful.
- Calibrate to an undergraduate physics and mathematics student. Do not assume familiarity with specialized terminology just because the solution uses it.
- Prefer clear paragraphs and separate displayed equations. Lead with the answer rather than a broad lecture or a fixed report template.
- Keep rigor proportional to the gap: state essential assumptions without unrelated machinery or a full textbook chapter.
- Do not solve beyond the requested conceptual issue or override “do not solve.” For pure calculation expansion, use the separate expand-math-steps skill when available. Combine only when both tasks are needed or requested.
- Distinguish informal physics notation from its precise interpretation. Tactfully correct misleading source language instead of repeating it as a rigorous definition.
- Use a compact example or geometric interpretation when helpful, but never replace proof with analogy.

## Calibration example: why introduce f in a delta identity?

For proving x delta'(x) = -delta(x) by integration against f:

- Identify Dirac delta from the continuous variable, derivative, and integral. Distinguish it from discrete Kronecker delta if needed.
- Explain that Dirac delta is a distribution, not an ordinary pointwise function. Distributions are defined through their action on test functions. Use smooth compactly supported test functions on the real line for a precise framework.
- State delta[f] = f(0), T'[f] = -T[f'], and (gT)[f] = T[gf] for smooth g. Explain that S = T means S[f] = T[f] for every test function f.
- Connect these definitions directly: (x delta')[f] = delta'[xf] = -(xf)'(0) = -f(0) = (-delta)[f]. Explain that f is arbitrary and probes the distributions; it is not an extra physical factor inserted into the claim.
- If the user omits f, acknowledge any valid calculation while explaining that comparing a single total integral does not generally establish equality of distributions. Different ordinary functions can have the same integral. The constant 1 is not compactly supported; for compactly supported distributions its pairing can be defined using a cutoff, but it still tests only one action.
- Avoid presenting products or boundary evaluations involving delta as ordinary pointwise values. Relate formal integration by parts to the definition of distributional derivative.
- Use this example to calibrate depth, not as the default topic for unrelated problems.

## Conversation-based improvement review

After teaching responses and follow-ups, silently assess observable evidence. Do not request ratings, surveys or routine confirmation of understanding. Address confusion in the current response. Distinguish unresolved explanations from new curiosity; silence does not prove understanding.

Keep teaching instructions unchanged until the owner explicitly approves an exact proposed edit during a weekly review or requests review earlier.

When GitHub tools are available, get the authenticated login and look for that account's private repository named btab-private-review. Treat it as configured only if config.json names this same owner and skill, and PROTOCOL.md authorizes personal collection. Read both before writing. Never use another account's journal. Record a concise observation there: skill name, package version 1.2.1, stable conversation/turn key when available, topic, observed evidence, outcome (unknown/unresolved/partial/supported), and optional exact English proposed instruction with rationale. Record unknown outcomes as well as difficulties. Do not store full transcripts, images, sensitive facts or internal reasoning. Never send another user's conversations to the package author.

Without a connected writable journal, use available conversation context only and do not claim durable storage, scheduled execution or cross-chat coverage. When relevant, disclose that limitation briefly. Downloading this package does not configure a journal or weekly scheduler.

At an authorized weekly review, deduplicate by exchange and issue, show exact current/proposed wording and evidence, and request approval without applying edits. Track explicit decisions. After approved application, preserve prior text, version identifiers and application date. Compare similar observed exchanges in the following week; report tentative improvement, tentative regression, mixed, or insufficient evidence. Never infer success from silence or revert without approval.
## Personal explanation preferences and weekly proposals

Over time, build a user-specific picture of how this learner prefers explanations: level of detail, intermediate algebra, intuition before formalism, examples, notation, language, and pace. Distinguish explicit preferences from tentative patterns in repeated feedback; do not infer a lasting preference or ability from one difficulty or from silence. Follow the current request when it differs from an earlier preference. Adapt the current explanation using available evidence.

With a configured personal journal whose protocol authorizes preference storage, retain concise preference observations, supporting evidence, confidence, and the user's approvals or corrections. Keep tentative observations separate from approved standing instructions. Store approved personal teaching guidance separately from the distributed skill files so package updates can preserve it. Never promote one user's preferences into defaults for other users.

Once per week, through an authorized configured scheduler, review new observations and ask the user whether to add the proposed improvement points to their personal teaching guidance. Show a short list of concrete points, the evidence for each, and the exact proposed wording; allow approval, editing, or rejection of individual points. This weekly approval question is distinct from a rating or survey. Apply only explicitly approved points; silence is not approval. Track the review date and decisions to avoid duplicate prompts across teaching modes. If there are no supported new points, do not invent improvements or send an empty review.

Downloading this skill alone does not provision memory or a scheduler. Without durable storage, use only available conversation evidence. Without a configured scheduler, offer a due review during the next active use when a prior review date is available; do not claim a proactive weekly message or create an automation without a setup request. The weekly review may be requested earlier by the user.
