# Required Assets

The game code is complete, but the image and sound assets it loads are **not included in this
repo** (they were lost over time). This document lists exactly what `main.py` expects and where,
so the game can run again if the files are found.

Drop the recovered files into the project root using the folder structure below. All paths are
relative to the repo root (e.g. `Sprites/scroll.png`). The font `japanese.ttf` is already present.

## `Sprites/` (top level)

| File | Used for |
|------|----------|
| `SamuraiShibaTitleScreen.png` | Title screen |
| `BackgroundOfShibaSamurai.png` | Gameplay background / map |
| `scroll.png` | Context & controls screen |

## `Sprites/Sprites/` (animation frames)

| Folder | Frames | Subject |
|--------|--------|---------|
| `Player_Idle/` | `idle_player_0..3.png` | Player idle |
| `Player_Walking_Right/` | `player_walking_right_0..7.png` | Player walking right |
| `Player_Walking_Left/` | `left_player_walking+0..7.png` | Player walking left |
| `Right Sword Slash/` | `Right_Sword_Slash_0..5.png` | Sword slash right |
| `Sword Slash Left/` | `Left_Sword_Slash_0..5.png` | Sword slash left |
| `Sword Slash Down/` | `sword_slash_down_0..5.png` | Sword slash down |
| `Sword Slash Up/` | `Up_Sword_Slash_0..5.png` | Sword slash up |
| `Shuriken/` | `shuriken_0..1.png` | Thrown shuriken |
| `Spin Attack/` | `spin_00..22.png` | Spin ability |
| `Dash_Smoke/` | `dash_smoke_0..7.png` | Dash ability smoke |
| `Archer_Fox/` | `archer_fox_0..7.png` | Archer fox (right) |
| `Archer_Fox_Left/` | `left_archer_fox_0..7.png` | Archer fox (left) |
| `Arrow/` | `arrow_0..1.png` | Enemy arrow (right) |
| `Ninja_Cat/` | `Ninja_Cat_0..2.png` | Ninja cat (right) |
| `Ninja_Cat_Left/` | `ninja_cat_left_0..2.png` | Ninja cat (left) |
| `Panda Enemy/` | `Panda_Enemy_0..7.png` | Panda sumo (right) |
| `Panda_Enemy_Left/` | `Panda_Left_0..7.png` | Panda sumo (left) |
| `enemy_death/` | `enemy_death_0..2.png` | Enemy death |
| `heart_pickup/` | `heart_pickup_0..1.png` | Heart pickup |

Single files directly in `Sprites/Sprites/`:

- `player_damage_0.png`
- `arrow_left.png`
- `cooldown_pickup_0.png`
- `bomb_pickup_0.png`

## `Sounds/`

`game_music.wav`, `intro_music.wav`, `ability_recharge.wav`, `arrow_shot.wav`, `bomb.wav`,
`enemy_death.wav`, `game_over.wav`, `heal.wav`, `hurricane.wav`, `player_damage.wav`,
`round_start.wav`, `shuriken.wav`, `smoke_bomb.wav`, `sword_slash.wav`, `walking.wav`,
`gong.wav`, `shuriken_pickup.wav`

## Fonts

- `japanese.ttf` — ✅ already in the repo.
