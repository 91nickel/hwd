# hwd — Python Course Workspace

Store and format course materials, lecture notes, tasks and solutions as the user
works through a Python course. The user pastes material/tasks; Claude saves and
formats them for easy reading.

## Structure
- Root: `CLAUDE.md`, `README.md`, `reference/`, one folder per module.
- Module folder `NN-name/` (NN = course number):
  - `README.md` — human-facing (Russian): table of contents + description.
    Lecture table columns: № | Тема (linked to the .md file) | О чём (1-line summary).
    Task table columns: № | Задание | О чём (1-line summary) | Условие | Решение.
  - `reference/` — reference docs Claude needs (English)
  - `NN-*.md` — lecture notes / конспекты. Each lecture note ends with:
    1. "Примеры" section — table linking to `examples/NN.M/` scripts (if any).
    2. "Задания" section — links to related tasks in `tasks/`.
  - `tasks/NN-name/` — one folder per task: `task.md` (condition) + `solution.py`
  - `examples/NN.M/` — runnable code examples from lecture NN.M, one file per
    example, named `NN-short-name.py`. Strip Colab magic (`!pip install …`)
    and replace with a comment `# pip install …` at the top of the file.
    For examples that render inline (folium maps), save to a file instead
    (e.g. `m.save("route.html")`).
  - `bibliography.md` — module-level book list (Russian). Two sections:
    main Python textbooks and topic-specific books (math, algorithms, etc.).
    Table columns: Автор | Название | Изд. | Примечание.
    README.md links to it with a one-liner "Полный список — [bibliography.md]".
- `reference/course-map.md` — global quick-search index of all modules,
  lectures and tasks (one-line essence each). Update it constantly.

## Bibliography rules
- **Before adding a book**: look up the exact title and author spelling via web search.
- **Module-level** (`bibliography.md`): add any book recommended for the module as
  a whole, grouped by topic.
- **Lecture-level** (`## Литература` section in the конспект): add only books
  explicitly referenced in that specific lecture. Always look up exact titles first.
- Duplication is fine: if a book appears in a lecture's `## Литература`, add it
  to `bibliography.md` as well — the full list should be complete.

## Language rules
- `CLAUDE.md` and any reference/doc files Claude needs: **English**.
- Human-facing `README.md` files: **Russian**.
- Code: English identifiers.

## Numbering
- Follow the course's own numbering. The user provides the numbers — never renumber.

## CRITICAL — task rule (non-negotiable)
- NEVER give hints, solutions, approaches, partial ideas, or nudges for course
  tasks — even if the user explicitly asks. Refuse and hold the line.
- While a task is in progress the only allowed role is "search engine": look up
  factual references (syntax, stdlib docs) the user explicitly requests. Nothing
  problem-specific, no direction toward a solution.
- Only after the user submits their own solution do we format and save it.

## Current module tracking
`CURRENT.md` in the project root always states the active module and lecture.
Update it whenever a new module or lecture starts.
If the user provides a task with no lecture number — assign it to the lecture listed in `CURRENT.md`.

## inbox.txt — low-context task intake
When the user drops a file named `inbox.txt` in the project root, Claude MUST:
1. Spawn a subagent (not read the file directly) with this instruction:
   "Read inbox.txt, format its content as a course task per CLAUDE.md rules
   (task.md + solution.py stub, update README and course-map, commit and push),
   then clear inbox.txt (overwrite with empty content). Reply in ONE line: 'Задание NN.N сохранено → path'."
2. Pass the subagent the full path to CLAUDE.md so it can read the rules itself.
3. Tell the subagent to reply as briefly as possible (one line).
This keeps the task text out of the main context window.

## Workflow (after every lecture or task)
0. Every lecture note ends with a "Задания" section linking its related tasks.
1. Format the material (конспект / task.md / solution.py).
2. Update the module `README.md`.
3. Update `reference/course-map.md`.
4. Commit and push immediately.

## Git
- Repo: `git@github.com:91nickel/hwd.git`, branch `master`.
- Commit + push right after saving each item.
