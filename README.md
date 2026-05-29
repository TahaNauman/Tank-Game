# Tank Game

A 2D top-down arcade tank shooting game built with Python and Pygame.

## Play

```powershell
pip install -r requirements.txt
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| W A S D | Move tank |
| Mouse | Aim turret |
| Left click | Shoot |
| ESC | Quit |

## Features

- Tank movement with WASD, turret aims toward mouse cursor
- Shootable targets (wooden crates) that spawn periodically
- Score tracking and health system
- Solid collision — tank cannot walk through targets
- Clean modular architecture ready for expansion

## Project Structure

```
├── main.py                  # Entry point
├── game.py                  # Game loop and orchestration
├── settings.py              # All configurable constants
├── sprites/                 # Tank, Projectile, Target
├── weapons/                 # Weapon base + BulletWeapon
├── managers/                # Spawner, collision, score
└── ui/                      # HUD rendering
```

## Planned

- Rocket weapon with splash damage
- Explosion particle effects
- Moving targets / enemy AI
- Sound effects
- Weapon switching
