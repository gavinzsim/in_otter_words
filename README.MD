### In Otter Words

When the world needs more than simply being as is. In Otter words, a change...

Featuring:
Stormy (Blue), Sparky (Orange), Trendy (Pink), Spendy (Green)

## Personalized finale

Story choices are recorded in Ren'Py save data. A normal run reaches the finale after
Stormy's machine works or breaks; the existing early endings still end immediately.
The finale writes `finale_context.json` to Ren'Py's user save directory
(`config.savedir`), alongside save data, before requesting dialogue.

To enable the online finale, replace `PUT_YOUR_OPENROUTER_API_KEY_HERE` in
`game/secrets.rpy` with your OpenRouter key. That file is ignored by Git.
Alternatively, set `OPENROUTER_API_KEY` in the environment that launches Ren'Py;
`secrets.rpy` takes precedence when it contains a key. The game sends the playthrough context and
allowed visual asset IDs to OpenRouter using `z-ai/glm-5.3-flash`. The key is
never included in the context JSON or logs. Without a key or on an API error,
the game shows one generic technical fallback. Score and relationship values
never select a preset ending.
For a build distributed to other players, use the environment variable so a
plaintext key is not packaged with the game files.

The base main-story route has 16 scored decisions and a 0–32 opportunity range.
Each optional snooze adds one recorded decision and two possible points, up to
18 decisions and a 0–36 range before the snooze ending. Some combinations end
the story early, so the score context uses the range for choices actually
encountered in a given run. The LLM decides the future from the whole context.

For local verification, run Ren'Py lint, `tests/check_finale.py` using the
Ren'Py SDK's Python executable, and the engine testcases
`renpy.exe <project> test finale_fallback_render` and
`renpy.exe <project> test finale_generated_render`. In the developer console, call
`debug_finale_state()` to log current scoring, relationships, traits, and choices.
