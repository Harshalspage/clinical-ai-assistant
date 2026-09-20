def validate_input(user_input):
    """
    Validate the user's clinical input.

    Returns:
        tuple(bool, str)
        True, "" if valid
        False, error_message if invalid
    """

    # Remove leading/trailing spaces
    user_input = user_input.strip()

    # Empty input
    if not user_input:
        return False, "Please enter a clinical case."

    # Very short input
    if len(user_input) < 10:
        return False, "Please provide more clinical details."

    return True, ""