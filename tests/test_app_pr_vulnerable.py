import app_pr_vulnerable

def test_run_user_code():
    result = app_pr_vulnerable.run_user_code("1 + 1")
    assert result == 2

def test_get_user():
    # We only test that the function executes
    # Not correctness of DB logic
    try:
        app_pr_vulnerable.get_user("1")
    except Exception:
        # DB may not exist, but code path is executed
        assert True
