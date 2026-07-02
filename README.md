# Shiba Samurai (Python / Pygame)

> *Dedicated to my best friend Rocky, fly high.*

The first project I ever really made — an infinite, round-based, top-down survival game written
from scratch in Python with Pygame, back in high school (Dec 2022). You play a shiba inu samurai
defending his village against waves of enemies.

This is the **original version**. There's also a Unity rebuild ("2.0", better graphics and engine)
on the [`UnityRemakeVersion`](../../tree/UnityRemakeVersion) branch.

## ⚠️ Assets missing

The code is complete, but most of the image and sound assets it loads were lost over time, so the
game **won't run as-is** — it will fail immediately trying to load the title screen sprite. The
full list of what's needed and where it goes is in [`ASSETS_REQUIRED.md`](ASSETS_REQUIRED.md).
Until those are restored, treat this as a code read.

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

Requires Python 3 and Pygame.

```bash
pip install -r requirements.txt
python main.py
```

(Once the [required assets](ASSETS_REQUIRED.md) are in place.)

## Files

| File | What it is |
|------|------------|
| `main.py` | **The complete game** — start screen, waves, combat, game-over loop |
| `japanese.ttf` | Font used for on-screen text |
| `player.py`, `enemy.py`, `flow.py`, `start_screen.py` | Early prototype / scratch scripts from development — kept for posterity, not used by `main.py` |
