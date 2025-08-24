"""
Simple tests for Tic-Tac-Toe AI
"""

import unittest
import sys
import os
import time

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import tictactoe as ttt


class TestTicTacToe(unittest.TestCase):
    
    def setUp(self):
        """Set up test boards."""
        self.empty_board = ttt.initial_state()
        self.x_wins = [['X', 'X', 'X'], ['O', 'O', None], [None, None, None]]
        self.tie_game = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]

    def test_initial_state(self):
        """Test empty board creation."""
        board = ttt.initial_state()
        self.assertEqual(len(board), 3)
        for row in board:
            for cell in row:
                self.assertIsNone(cell)
    
    def test_player_turns(self):
        """Test player alternation."""
        self.assertEqual(ttt.player(self.empty_board), ttt.X)
    
    def test_actions(self):
        """Test available moves."""
        actions = ttt.actions(self.empty_board)
        self.assertEqual(len(actions), 9)
    
    def test_result(self):
        """Test move application."""
        new_board = ttt.result(self.empty_board, (0, 0))
        self.assertEqual(new_board[0][0], ttt.X)
        self.assertIsNone(self.empty_board[0][0])  # Original unchanged
    
    def test_winner_detection(self):
        """Test win detection."""
        self.assertEqual(ttt.winner(self.x_wins), ttt.X)
        self.assertIsNone(ttt.winner(self.empty_board))
    
    def test_terminal(self):
        """Test game end detection."""
        self.assertTrue(ttt.terminal(self.x_wins))
        self.assertTrue(ttt.terminal(self.tie_game))
        self.assertFalse(ttt.terminal(self.empty_board))
    
    def test_utility(self):
        """Test scoring."""
        self.assertEqual(ttt.utility(self.x_wins), 1)
        self.assertEqual(ttt.utility(self.tie_game), 0)
    
    def test_minimax_basics(self):
        """Test AI returns valid moves."""
        move = ttt.minimax(self.empty_board)
        self.assertIsNotNone(move)
        self.assertIn(move, ttt.actions(self.empty_board))
        
        # AI should return None for finished games
        self.assertIsNone(ttt.minimax(self.x_wins))
    
    def test_ai_speed(self):
        """Test AI is fast (alpha-beta working)."""
        start_time = time.time()
        ttt.minimax(self.empty_board)
        execution_time = time.time() - start_time
        
        print(f"\nAI move time: {execution_time:.3f} seconds")
        self.assertLess(execution_time, 1.0, "AI too slow - check alpha-beta pruning")


if __name__ == '__main__':
    unittest.main()