# Sum of Seven - Strategy Puzzle Game

A mathematical strategy game built in Python where players must clear a grid by finding combinations of numbers that sum exactly to 7. This project combines a graphical interface for settings and a logic-based terminal interface for gameplay.

## 🕹️ Gameplay Overview

The objective is to clear as many numbers as possible from a 5x10 grid filled with random digits.

1. **Difficulty Selection**: A GUI window (powered by Tkinter) allows you to choose your challenge level:
   - **Easy**: 10 lives
   - **Normal**: 7 lives
   - **Hard**: 4 lives
2. **The Grid**: The board consists of 5 rows (labeled A to E) and 2 extra "helper" dice (labeled F and G).
3. **The Goal**: Enter a combination of letters (e.g., `ABF`, `CG`, `ADE`) whose corresponding values add up to exactly **7**.
4. **Clearing**: Valid combinations are removed from the board, rows shift, and your score increases.
5. **Vitals**: 
   - If no combinations are visible, type `V` to spend a life and roll new extra dice (F & G).
   - The game ends when you have 0 lives and no more mathematical combinations of 7 are possible on the board.

## ✨ Technical Features

- **Hybrid Interface**: Seamless transition from a `Tkinter` graphical start menu to a formatted ASCII terminal game engine.
- **Advanced Combinatorial Logic**: Utilizes `itertools.combinations` to pre-calculate all possible moves, allowing the engine to intelligently verify if the game is truly over.
- **Dynamic Scoring System**: 
  - Rewards complexity: Longer combinations (using more dice) grant significantly higher points.
  - Bonus logic: Includes "Full Row" bonuses (up to 100 points) for completely clearing lines.
- **Robust Error Handling**:
  - Validates user input to ensure only existing dice are selected.
  - Prevents crashes from invalid characters or mathematical mismatches.

## 📊 Scoring Table

| Dice Used | Points |
|-----------|--------|
| 2 Dice    | 7      |
| 3 Dice    | 15     |
| 4 Dice    | 30     |
| 5 Dice    | 50     |
| 6 Dice    | 75     |
| 7 Dice    | 100    |

*Extra bonuses are awarded for clearing 1 to 5 full lines.*

## 🛠️ Installation & Usage

### Prerequisites
- **Python 3.x**
- **Tkinter**: On Ubuntu/Debian, install it via:
```bash
sudo apt install python3-tk
```

### Setup & Run

1. **Clone the repository:**
```bash
git clone https://github.com/kilian-gthb/password_generator.git
```

2. **Run the game:**
```bash
python Seven.py
```

---

Developed by [Kilian](https://github.com/kilian-gthb)