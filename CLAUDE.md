# hwd — Python Course Workspace

Store and format course materials, lecture notes, tasks and solutions as the user
works through a Python course. The user pastes material/tasks; Claude saves and
formats them for easy reading.

## Structure
- Root: `CLAUDE.md`, `README.md`, `reference/`, one folder per module.
- Module folder `NN-name/` (NN = course number):
  - `README.md` — human-facing (Russian): table of contents + description.
    Lecture table columns: № | Тема (linked to the .md file) | О чём (1-line summary).
    Task table columns: № | Задание | Условие | Решение.
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

## inbox.txt — task intake
When the user says to process inbox.txt:
1. Read CURRENT.md → get {module} folder and current lecture number.
2. Read inbox.txt → get task text and number (if given).
   If no number: check tasks/{module}/ for existing tasks, increment the last one.
3. Slug: transliterate the task title to lowercase-kebab-case (Russian→latin).
4. Create {module}\tasks\{NN.M.K-slug}\task.md:
   # Задание NN.M.K — Title
   {task text verbatim}
5. Create solution.py in the same folder: one line only: # NN.M.K — Title
6. Append to {module}\README.md Задания table:
   | NN.M.K | Title | [task.md](tasks/NN.M.K-slug/task.md) | [solution.py](tasks/NN.M.K-slug/solution.py) |
7. Append to reference\course-map.md under Tasks:
   - [NN.M.K] Title — one-line essence → {module}/tasks/NN.M.K-slug/
8. Overwrite inbox.txt with empty string.
9. git add, commit "Add task NN.M.K — Title", push to master.

## Workflow (after every lecture or task)
0. Every lecture note ends with a "Задания" section linking its related tasks.
1. Format the material (конспект / task.md / solution.py).
2. Update the module `README.md`.
3. Update `reference/course-map.md`.
4. Commit and push immediately.

## Git
- Repo: `git@github.com:91nickel/hwd.git`, branch `master`.
- Commit + push right after saving each item.
