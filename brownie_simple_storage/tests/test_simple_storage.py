from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    excepted = 0
    # Assert
    assert starting_value == excepted


def test_updating_storage():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    excepted = 15
    simple_storage.store(excepted, {"from": account})
    # Assert
    assert excepted == simple_storage.retrieve()
