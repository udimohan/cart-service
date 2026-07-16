"""Tests for catalog_00525."""

import pytest

from cartservice.generated.catalog_00525 import (
    Product_00525,
    bucket_by_tag_00525,
    is_valid_sku_00525,
    price_with_tax_00525,
)


def test_price_with_tax_00525():
    assert price_with_tax_00525(1000, 500) == 1050


def test_price_with_tax_negative_00525():
    with pytest.raises(ValueError):
        price_with_tax_00525(1000, -1)


def test_is_valid_sku_00525():
    assert is_valid_sku_00525("abc123")
    assert not is_valid_sku_00525("")


def test_bucket_by_tag_00525():
    p = Product_00525("s1", 100, ["a"])
    assert bucket_by_tag_00525([p]) == {"a": ["s1"]}
