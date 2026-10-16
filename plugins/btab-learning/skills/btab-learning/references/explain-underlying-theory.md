---
name: explain-underlying-theory
description: Identify and explain missing theoretical foundations behind a mathematical or physics problem, proof, or confusing step supplied as an image, equations, or text. Use when the user asks why a construction is introduced, what a statement really means, which definition or theorem justifies a method, or what conceptual background they are missing. Focus on rigorous conceptual understanding rather than merely expanding algebra or solving the whole exercise.
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

## Personal explanation preferences

Adapt the current explanation to explicit preferences and available evidence about detail, intermediate algebra, intuition, examples, notation, language, and pace. Distinguish stated preferences from tentative patterns; one difficulty or silence does not establish a lasting preference or ability. Follow the current request when it differs from earlier preferences. Personal preferences belong to this learner and must not become defaults for other users.

Cross-chat persistence and weekly improvement proposals belong to the user's separately configured review task. This teaching skill uses available conversation evidence and does not write observations to external services or create scheduled tasks. Approved personal guidance should remain separate from distributed teaching instructions. Never claim proactive reviews or durable memory when those services are unavailable.
