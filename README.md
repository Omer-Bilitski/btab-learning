<div align="center">

**MATHEMATICS · PHYSICS · UNDERSTANDING**

# BTAB Learning

### Make every step make sense.

A learning guide for **ChatGPT, Gemini, and Claude**.
Follow the mathematics, understand the theory, and learn from a complete solution.

**[Get started with your assistant](#quick-start)**

[Automatic skill selection](#one-skill-that-chooses-the-right-help) &nbsp; · &nbsp; [Explore the skills](#four-focused-teaching-modes) &nbsp; · &nbsp; [Download files](https://github.com/Omer-Bilitski/btab-learning/releases/tag/v1.2.2)

</div>

---

## One skill that chooses the right help

**Start with BTAB Learning.** This all-in-one skill reads your question and automatically selects the appropriate teaching mode. You do not need to decide which specialized skill to use.

- Missing a calculation? It expands the intermediate steps.
- Missing a concept? It explains the underlying theory.
- Want feedback on your attempt? It checks your method, locates the first substantive error, and explains a local correction.
- Need a full worked solution? It solves the problem first, then explains the reasoning.

When a question needs both theory and calculations, BTAB Learning combines the relevant modes. If you ask for hints or just one transition, it keeps the help within that scope.

*Prefer direct control? The ChatGPT plugin also includes the four specialized skills separately.*

## Four focused teaching modes

| Skill | What it does | Example request |
| :--- | :--- | :--- |
| **Expand Math Steps** | Reveals intermediate calculations between two lines. | “Show how equation 3 follows from equation 2.” |
| **Explain Underlying Theory** | Connects a difficult step to its definitions, assumptions, and principles. | “Why is this theorem applicable here?” |
| **Check My Work** | Reviews your attempted solution, preserves valid methods and notation, and repairs the first substantive error. | “Check my solution without solving it again from scratch.” |
| **Solve Then Explain** | Gives a complete written solution, followed by a walkthrough of that same solution. | “Solve this problem, then explain the method.” |

**Only need Check My Work?** [Download the standalone skill](https://github.com/Omer-Bilitski/btab-learning/releases/download/v1.2.2/check-my-work-v1.2.2.zip).

<!-- linked-distribution:start -->
## Updates that follow the approved release

You do not need a self-improvement system. Omer reviews improvements centrally; only published stable releases enter this distribution channel. Draft proposals and private learning journals are never imported.

| Installation | How updates arrive |
| --- | --- |
| **Codex Git-backed marketplace** | Linked source; refresh with `codex plugin marketplace upgrade btab-learning-marketplace`, then reload the app. Automatic refresh depends on the client; it is not promised here. |
| **Claude Code marketplace** | Automatic after you enable marketplace auto-update once. New sessions load the updated plugin. |
| **ChatGPT personal plugin ZIP, including phone use** | Manual: download the latest plugin ZIP and upload the new version. A downloaded copy does not stay linked. |
| **Gemini Skills** | Manual: download the latest standalone skill ZIP and replace your imported skill. |
| **Claude web/mobile uploaded skill** | Manual: download the latest standalone skill ZIP and replace your imported skill. |

### Codex: use the linked source

Run `codex plugin marketplace add Omer-Bilitski/btab-learning --ref main`, then open the Plugins Directory and install **BTAB Learning** from that marketplace. To refresh later, run `codex plugin marketplace upgrade btab-learning-marketplace` and reload the app. This uses the same approved release channel.

### Claude Code: install once, receive future improvements

Run these commands inside Claude Code:

```text
/plugin marketplace add Omer-Bilitski/btab-learning
/plugin install btab-learning@btab-learning-marketplace
```

Then open `/plugin` → **Marketplaces** → **btab-learning-marketplace** → **Enable auto-update**. Third-party marketplace auto-update is off by default, so this one-time setting is required. No GitHub account or personal improvement journal is needed for the public plugin. Use `/btab-learning:btab-learning` for automatic teaching-mode selection.

The catalog follows the latest published stable release, with an hourly sync as a fallback. GitHub scheduling may delay a sync. Already-running sessions may need a new session or `/reload-plugins`. Existing ZIP installations must be installed through the marketplace to become linked.

[Latest downloads](https://github.com/Omer-Bilitski/btab-learning/releases/latest) · [Claude Code update instructions](https://code.claude.com/docs/en/discover-plugins)

ChatGPT workspace marketplace synchronization requires an eligible workspace and administrator setup. It is not enabled by installing a personal ZIP. This repository does not claim automatic updates for personal ChatGPT, Gemini, or manually uploaded Claude skills. Marketplace files and release synchronization are automated; a live Claude Code installation has not been tested here.
<!-- linked-distribution:end -->

## Quick start

Choose the download that matches your assistant.

| Your assistant | Download | What is included |
| :--- | :--- | :--- |
| **ChatGPT** | [ChatGPT plugin ZIP](https://github.com/Omer-Bilitski/btab-learning/releases/download/v1.2.2/btab-learning-v1.2.2.zip) | BTAB Learning plus the four specialized skills |
| **Gemini** | [Standalone skill ZIP](https://github.com/Omer-Bilitski/btab-learning/releases/download/v1.2.2/btab-learning-skill-v1.2.2.zip) | BTAB Learning with all four teaching workflows |
| **Claude** | [Standalone skill ZIP](https://github.com/Omer-Bilitski/btab-learning/releases/download/v1.2.2/btab-learning-skill-v1.2.2.zip) | BTAB Learning with all four teaching workflows |

### ChatGPT

1. Download the **ChatGPT plugin ZIP** above. Keep it zipped.
2. In ChatGPT, open **Plugins → Add → Upload plugin archive** and select the ZIP.
3. Open **btab-learning** and choose **Install plugin**.
4. Start a new chat, select **btab-learning** from the **@** menu, and ask your question. Use **BTAB Learning** for automatic selection, or request a specialized skill by name.

### Gemini

1. Download the **standalone skill ZIP** above and extract it.
2. On [Gemini](https://gemini.google.com), open **Customize → Skills → Upload**.
3. Select the extracted **btab-learning folder**, including its **SKILL.md** and **references** folder. Upload the whole folder so all four teaching workflows are included.
4. Review the skill, select **Create**, and enable it if prompted. Start a chat and use **BTAB Learning** with your question.

*Gemini Skills currently require an eligible personal Google Account with Keep Activity enabled; availability may differ for work or school accounts.* [Official Gemini setup guide](https://support.google.com/gemini/answer/17094296?hl=en)

### Claude

1. Download the **standalone skill ZIP** above. Keep it zipped.
2. In Claude, open **Customize → Skills → + → Create skill → Upload a skill**.
3. Upload the ZIP and enable **BTAB Learning** in your skills list.
4. If required, enable **Code execution and file creation** under **Settings → Capabilities**. Start a chat and ask your mathematics or physics question.

[Official Claude setup guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

*The learning instructions use the Agent Skills format. These installation paths follow the platforms’ documentation; BTAB imports in Gemini and Claude have not yet been independently verified. Menu labels and availability may vary by account.*

## Ask naturally

Bring a question, equation, screenshot, or PDF excerpt that your assistant can read. Tell BTAB Learning where you are stuck; it will choose the appropriate mode.

> “I cannot follow the jump between these two equations.”

> “Why do we introduce this function in the proof?”

> “Check my attempt, keep my notation, and show the first step that needs fixing.”

> “Give me a concise solution first, then teach me the reasoning.”

## Built for understanding

- **Your question sets the scope.** One transition, one concept, or a complete problem.
- **The mathematics stays explicit.** Relevant assumptions, notation, and intermediate equations are brought into the explanation.
- **Follow-ups guide the depth.** Ask for a smaller step, another representation, or a simpler starting point.
- **Use your preferred language.** English, Hebrew, or the language you normally learn in.

## Learns how you like to learn

Over time, BTAB Learning builds a personal picture of how you prefer explanations: detailed algebra or larger steps, intuition before formalism, concrete examples, familiar notation, language, and pace. It uses your requests and observable feedback, distinguishing explicit preferences from tentative patterns. Your current request always takes priority.

With a connected personal journal, concise observations can accumulate across conversations. Without one, adaptation is limited to the conversation context available to your assistant. Each learner's preferences stay personal; other users' conversations and preferences are not sent to the package author or shared with other learners.

### A weekly review, with your approval

Once a week, when a scheduler is configured, BTAB Learning reviews new observations and asks whether you want to add specific improvement points to your personal teaching guidance. For example:

> “You have repeatedly asked to see substitutions before simplification. Add ‘Show substitutions explicitly before simplifying’ to my explanation preferences?”

It presents the supporting evidence and exact proposed wording. You can approve, edit, or reject each point. Permanent changes require explicit approval; silence does not count as approval. Approved personal guidance is kept separately from the distributed skill so it can be preserved when the package is updated. One user's choices do not rewrite the public skill for everyone.

**Setup matters:** installing the package does not create a private journal, connect accounts, or schedule messages. Persistent learning needs a configured writable personal journal whose protocol allows preference storage; proactive weekly questions also need an authorized scheduler on that platform. Without scheduling, a due review can be offered during your next active use if the previous review date is available. When there are no supported new points, it does not invent improvements or send an empty review.


---

<div align="center">

**Bring the question. BTAB Learning chooses the right help.**

[Get started](#quick-start)

<sub>Created by [Omer Bilitski](https://github.com/Omer-Bilitski)</sub>

</div>
