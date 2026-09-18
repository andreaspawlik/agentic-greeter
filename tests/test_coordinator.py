from scripts.coordinator import advance_run, start_run


def test_self_reviewed_advances_validated_run_to_merge():
    state = start_run(1, run_id="issue-1-test")
    state = advance_run(state, "architect_validated")
    state = advance_run(state, "developer_pr_created", {"pr_number": 2})
    state = advance_run(state, "ci_passed")

    updated = advance_run(state, "self_reviewed")

    assert updated["review_status"] == "approved"
    assert updated["review_source"] == "self"
    assert updated["next_action"] == "merge"