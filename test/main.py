import pytest

@pytest.mark.a
@pytest.mark.parametrize(
    "test_input1, test_input2, test_input3, expected1, expected2",
    [
        (1, "super_admin", "super_admin_two", 1, "password updated"),
        (1, "super_admin_error", "super_admin_two", 0, "current password does not match"),
        (1001, "super_admin", "super_admin_two", 0, "user not found"),
    ],
)
def test_update_pwd(
    dbsession, test_input1, test_input2, test_input3, expected1, expected2
):
    res = update_pwd(dbsession, test_input1, test_input2, test_input3)
    assert res["status"] == expected1
    assert res["msg"] == expected2