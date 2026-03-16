def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    Expected values:
      - Easy: 1-20
      - Normal: 1-50
      - Hard: 1-100
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret using integer comparison and return the outcome string.

    Returns one of: "Win", "Too High", "Too Low"
    """
    try:
        g = int(guess)
        s = int(secret)
    except Exception:
        # If we can't coerce to int, fall back to string comparison for robustness.
        gs = str(guess)
        ss = str(secret)
        if gs == ss:
            return "Win"
        if gs > ss:
            return "Too High"
        return "Too Low"

    if g == s:
        return "Win"
    if g > s:
        return "Too High"
    return "Too Low"


def get_hint_message(outcome: str):
    """Return the user-facing hint message for a given outcome."""
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📈 Go LOWER!"
    if outcome == "Too Low":
        return "📉 Go HIGHER!"
    return ""


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
