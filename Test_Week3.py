import unittest
from Week_3 import create_new_item, delete_item_from_list, update_item, write_items_to_file

class TestWeek_2(unittest.TestCase):
    # Common Case: Add new item
    def test_add_new_item_to_list(self):

        # Assemble
        new_item = "apple"
        products = ["banana", "orange", "kiwi", "melon"]
        expected = ["banana", "orange", "kiwi", "melon", "apple"]

        # Act
        actual = create_new_item(new_item, "product", products)

        # Assert
        assert expected == actual

    def test_add_existing_item_to_list(self):
    # Edge Case: Add existing item
        # Assemble
        new_item = "banana"
        products = ["banana", "orange", "kiwi", "melon"]
        expected = ["banana", "orange", "kiwi", "melon"]

        # Act
        actual = create_new_item(new_item, "product", products)

        # Assert
        assert expected == actual

    def test_add_bolean_to_list(self):
    # Corner Case: Add new item
        # Assemble
        new_item = False
        products = ["banana", "orange", "kiwi", "melon"]
        expected = ["banana", "orange", "kiwi", "melon"]

        # Act
        actual = create_new_item(new_item, "product", products)

        # Assert
        assert expected == actual

    def test_delete_existing_item(self):
    # Common Case: Delete existing item
        # Assemble
        delete_item = "banana"
        products = ["banana", "orange", "kiwi", "melon"]
        expected = ["orange", "kiwi", "melon"]

        # Act
        actual = delete_item_from_list(delete_item, "product", products)

        # Assert
        assert expected == actual

    def test_delete_item_not_in_list(self):
    # Edge Case: Delete item not in list
        # Assemble
        delete_item = "apple"
        products = ["banana", "orange", "kiwi", "melon"]
        expected = ["banana","orange", "kiwi", "melon"]

        # Act
        actual = delete_item_from_list(delete_item, "product", products)

        # Assert
        assert expected == actual

    def test_update_existing_item(self):
    # Common Case: Update existing item
        # Assemble
        replace_item = "banana"
        new_item = "apple"
        products = ["banana", "orange", "kiwi", "melon"]
        expected = ["apple", "orange", "kiwi", "melon"]

        # Act
        actual = update_item(products, replace_item, new_item, "product")

        # Assert
        assert expected == actual

    def test_update_item_not_in_list(self):
    # Edge Case: Update item not in list
        # Assemble
        replace_item = "apple"
        new_item = "smoothie"
        products = ["banana", "orange", "kiwi", "melon"]
        expected = ["banana","orange", "kiwi", "melon"]

        # Act
        actual = update_item(products, replace_item, new_item, "product")

        # Assert
        assert expected == actual

    # def test_writes_list_to_file(self):

    #     # Assemble
    #     products = ["banana", "orange", "kiwi", "melon"]
    #     expected = 

    #     # Act
    #     actual = write_items_to_file("product", products)

    #     # Assert
    #     assert expected == actual

if __name__ == '__main__':
    unittest.main()
