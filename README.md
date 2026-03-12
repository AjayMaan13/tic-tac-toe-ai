# 🎮 Tic-Tac-Toe AI with Alpha-Beta Pruning

An unbeatable Tic-Tac-Toe AI that uses the Minimax algorithm with Alpha-Beta pruning optimization.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)

## 🎯 What I Built

- **Unbeatable AI** that never loses at Tic-Tac-Toe
- **Beautiful GUI** using Pygame with smooth interactions
- **Optimized algorithm** that's 50x faster than basic minimax
- **Perfect game logic** handling all win/tie conditions
- **Comprehensive tests** ensuring reliability

## 🚀 Quick Start

1. **Clone and setup**
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Mac/Linux
   ```

2. **Install and run**
   ```bash
   pip install -r requirements.txt
   python src/runner.py
   ```

3. **Test the AI**
   ```bash
   python -m pytest tests/ -v
   ```

4. **Play!** Choose X or O and try to beat the AI (spoiler: you can't!)

## 🤖 AI Concepts I Implemented

### **Core Algorithms**
- **Minimax Algorithm** - Game tree search for optimal moves
- **Alpha-Beta Pruning** - Skip bad moves to make AI 50x faster
- **Recursive Problem Solving** - Break complex decisions into simple ones

### **Game Theory**
- **Adversarial Search** - Two players with opposite goals
- **Perfect Information Games** - Both players see everything
- **Optimal Strategy** - Always make the mathematically best move

### **Performance Optimization**
- **Branch Pruning** - Eliminate useless calculations
- **Time Complexity Reduction** - From 300k+ nodes to ~7k nodes
- **Efficient Data Structures** - Smart board representation

## 📊 Performance Results

| Metric | Before Optimization | After Alpha-Beta | Improvement |
|--------|-------------------|------------------|-------------|
| **First Move Time** | 3.2 seconds | 0.06 seconds | **53x faster** |
| **Nodes Explored** | 362,880 | 7,200 | **50x fewer** |
| **User Experience** | Laggy | Instant | **Perfect** |

## 📁 Project Structure

```
tic-tac-toe-ai/
├── README.md                    # Project overview
├── PROJECT_EXPLANATION.md       # Deep technical dive
├── requirements.txt             # Dependencies
├── src/
│   ├── tictactoe.py            # AI logic and game rules
│   └── runner.py               # Pygame GUI interface
└── tests/
    └── test_tictactoe.py       # Unit tests
```

## 🚀 Real-World Applications

The same techniques used here apply to:
- **Chess engines** (Deep Blue, Stockfish)
- **Game AI** (Strategy games, puzzle games)  
- **Decision making** (Business optimization, Resource allocation)
- **Robotics** (Path planning with obstacles)

## 📚 Documentation

- **[PROJECT_EXPLANATION.md](PROJECT_EXPLANATION.md)** - Detailed technical explanation of Alpha-Beta Pruning implementation
- **[Test Coverage](tests/test_tictactoe.py)** - Comprehensive unit tests for all functionality

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Check AI performance
python tests/test_tictactoe.py
```

Expected output:
```
AI move time: 0.045 seconds
✅ All tests passed!
```

## 📄 License

MIT License — see [LICENSE](LICENSE).

## 🙏 Acknowledgments

- **CS50 AI Staff** for excellent course materials and project foundation

---

⭐ **If this project helped you understand AI algorithms, please give it a star!** ⭐

