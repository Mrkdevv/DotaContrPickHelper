# DotaContrPickHelper
A lightweight, clean, and fast in-game overlay for Dota 2 that helps you and your friends instantly find top-3 counter-picks during the drafting phase. No bloated websites, no heavy browsers — just press a hotkey, type the hero name, and get the counters.
✨ Features
In-Game Overlay: Transparent, borderless window that stays on top of your game (AlwaysOnTop).

Instant Smart Search: Fast, case-insensitive search by hero names or common community aliases/short names (e.g., am, sf, дуза).

Lightweight SQLite Backend: Powered by a local SQLite database containing all 122+ heroes and their respective counter-picks. Works completely offline.

Minimalist UI: Built with Python and PyQt for maximum performance and low resource usage.

🛠️ Tech Stack
Language: Python

GUI Framework: PyQt

Database: SQLite3

🚀 Roadmap / Todo
[ ] Create and populate the SQLite database schema (heroes and counter_picks tables).

[ ] Implement global hotkey listener to show/hide the overlay in-game.

[ ] Design the transparent PyQt overlay window.

[ ] Add support for custom hero aliases (English/Russian community slang).
