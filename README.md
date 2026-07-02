# Shiba Samurai (Python / Pygame)

> *Dedicated to my best friend Rocky, fly high.*

The first project I ever really made — an infinite, round-based, top-down survival game written
from scratch in Python with Pygame, back in high school (Dec 2022). You play a shiba inu samurai
defending his village against waves of enemies.

This is the **original version**. There's also a Unity rebuild ("2.0", better graphics and engine)
on the [`UnityRemakeVersion`](../../tree/UnityRemakeVersion) branch.

## The game

Survive as long as you can across escalating waves of enemies:

- 🐱 **Ninja Cat** — fast and agile, but weak
- 🦊 **Archer Fox** — ranged attacker that fires arrows
- 🐼 **Panda Sumo** — slow and heavy, hits hard

Slash with your sword, throw shurikens, and use abilities to stay alive. Pick up hearts, cooldown
refreshes, and bombs dropped by fallen enemies.

## Controls

| Input | Action |
|-------|--------|
| `W` `A` `S` `D` / Arrow keys | Move |
| Left mouse button | Sword slash (toward cursor) |
| `Q` | Throw shuriken (toward cursor) |
| `E` | Heal |
| `R` | Dash |
| `F` | Spin attack |

## Running it

This project uses [uv](https://docs.astral.sh/uv/). With uv installed, one command handles the
virtual environment, installs Pygame, and launches the game:

```bash
uv run main.py
```

<details>
<summary>Without uv</summary>

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install pygame
python main.py
```
</details>

## Files

| Path | What it is |
|------|------------|
| `main.py` | **The complete game** — start screen, waves, combat, game-over loop |
| `Sprites/`, `Sounds/` | Game art (137 sprites) and audio (17 tracks) |
| `japanese.ttf` | Font used for on-screen text |
| `pyproject.toml`, `uv.lock` | Dependency + environment definition |
| `player.py`, `enemy.py`, `flow.py`, `start_screen.py` | Early prototype / scratch scripts from development — kept for posterity, not used by `main.py` |
