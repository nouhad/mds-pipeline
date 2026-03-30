# Submission Rules

Read this carefully before submitting each day's work.

---

## Branch Naming

Format: `dayNN/firstname-lastname`

Examples:
- `day01/jane-smith`
- `day03/alex-johnson`

Branch names must be **lowercase with hyphens** between name parts. No spaces, no
capital letters.

---

## Minimum Commits Per Day

You must make **at least 3 meaningful commits** per day. A single "finished everything"
commit at the end is not acceptable.

Think of commits as save points that show your progression:

```
feat: print scene name and Maya version        ← task 01 done
feat: get selection and print count            ← task 02 first attempt
fix: handle empty selection without crashing   ← bug fix
docs: add notes about cmds.objectType          ← optional but good
```

---

## PR Title Format

```
Day NN – First Last – exercises
```

Examples:
- `Day 01 – Jane Smith – exercises`
- `Day 03 – Alex Johnson – exercises`

PRs with incorrect titles will be returned for correction before review.

---

## PR Description Template

When opening your PR, fill in the following:

```markdown
## What I did
- Completed task_01: printed scene name and Maya version
- Completed task_02: selection report with object types

## What was challenging
- Understanding the guarded import pattern took a while

## Stretch goals attempted
- [ ] Filter selection by type
- [x] Count poly faces on each selected object

## Questions for the instructor
- Is there a cleaner way to handle the empty-selection case?
```

---

## Deadlines

| Day | Branch due by |
|---|---|
| Day 01 | End of Day 01, 17:00 |
| Day 02 | End of Day 02, 17:00 |
| Day 03 | End of Day 03, 17:00 |
| Day 04 | End of Day 04, 17:00 |
| Day 05 | End of Day 05, 18:00 (capstone) |

Late submissions lose one letter grade per hour unless prior notice is given.

---

## Academic Integrity

- You may discuss approaches with classmates but **write your own code**.
- Do not copy another student's implementation verbatim.
- Citing Stack Overflow or documentation in a comment is fine and encouraged.
- Use of AI assistants (ChatGPT, Copilot, etc.) is permitted **only** if you understand
  every line you submit and can explain it when asked. Paste-without-understanding is
  a violation.
- Violations result in a zero for the day and a meeting with the programme director.
