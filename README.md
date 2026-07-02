# Shiba Samurai — Unity Remake (2.0)

A top-down samurai adventure game. This branch (`UnityRemakeVersion`) is the **Unity rebuild** of the original — a "2.0" version with better graphics and a proper game engine behind it.

> Looking for the original? The first version, written from scratch in **Python/Pygame**, lives on the [`main`](../../tree/main) branch.

## Status

Early work-in-progress prototype. Most of the effort so far has gone into art, tilemaps, animations, and prefabs. Current playable gameplay:

- **8-directional movement** with a full walk/idle animation set
- **Mouse-aimed directional sword attacks** (up / down / left / right)

## Controls

| Input | Action |
|-------|--------|
| `W` `A` `S` `D` / Arrow keys | Move |
| Left mouse button | Attack (direction based on cursor position) |

## Built with

- **Unity 2021.3.19f1**
- C# — see `Assets/Scripts/`

## Running it

1. Install **Unity 2021.3.19f1** (via Unity Hub).
2. Clone this branch and open the project folder in Unity Hub.
3. Open `Assets/Scenes/SampleScene.unity` and press **Play**.

## Project layout

```
Assets/
├── Art/          Sprites, tilesets, materials, tile assets
├── Animations/   Animation clips and controllers
├── PreFabs/      Prefabbed game objects
├── Scenes/       SampleScene (main scene)
└── Scripts/      Gameplay C# (PlayerMovement, Attacks, Layer)
```
