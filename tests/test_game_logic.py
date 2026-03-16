"""FIX: Tests added to cover the refactor and bug fixes (created collaboratively using Copilot Agent mode).
This file verifies ranges, parsing, numeric/string compare behavior, hint messages, and scoring.
"""

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    get_hint_message,
    update_score,
)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    assert check_guess(50, 50) == "Win"


def test_guess_too_high_and_low():
    # Numeric comparisons
    assert check_guess(60, 50) == "Too High"
    assert check_guess(40, 50) == "Too Low"


def test_string_and_numeric_mix():
    # Secret as numeric string should still compare correctly
    assert check_guess(50, "50") == "Win"
    assert check_guess("60", 50) == "Too High"
    # Non-numeric string falls back to string compare
    assert check_guess("b", "a") == "Too High"
    assert check_guess("a", "b") == "Too Low"


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)
    # Unknown difficulty defaults to 1-100
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_parse_guess():
    ok, val, err = parse_guess("42")
    assert ok and val == 42 and err is None

    ok, val, err = parse_guess("3.7")
    assert ok and val == 3 and err is None

    ok, val, err = parse_guess("")
    assert not ok and val is None and err is not None

    ok, val, err = parse_guess(None)
    assert not ok and val is None and err is not None

    ok, val, err = parse_guess("not-a-number")
    assert not ok and val is None and err is not None


def test_get_hint_message():
    assert get_hint_message("Win") == "🎉 Correct!"
    assert get_hint_message("Too High") == "📈 Go LOWER!"
    assert get_hint_message("Too Low") == "📉 Go HIGHER!"


def test_update_score_win_and_bounds():
    # attempt_number effect on points; ensure minimum 10 points
    base = 0
    # early win (attempt 0) -> 100 -10*(0+1)=90
    assert update_score(base, "Win", 0) == 90
    # later attempts: ensure not below 10
    assert update_score(base, "Win", 100) == base + 10


def test_update_score_hints():
    base = 50
    # Too High: even attempt_number -> +5
    assert update_score(base, "Too High", 2) == base + 5
    # Too High: odd attempt_number -> -5
    assert update_score(base, "Too High", 3) == base - 5
    # Too Low always -5
    assert update_score(base, "Too Low", 1) == base - 5
