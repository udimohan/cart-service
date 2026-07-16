"""Tests for catalog_01574."""

import pytest

from cartservice.generated.catalog_01574 import (
    Product_01574,
    bucket_by_tag_01574,
    is_valid_sku_01574,
    price_with_tax_01574,
)


def test_price_with_tax_01574():
    assert price_with_tax_01574(1000, 500) == 1050


def test_price_with_tax_negative_01574():
    with pytest.raises(ValueError):
        price_with_tax_01574(1000, -1)


def test_is_valid_sku_01574():
    assert is_valid_sku_01574("abc123")
    assert not is_valid_sku_01574("")


def test_bucket_by_tag_01574():
    p = Product_01574("s1", 100, ["a"])
    assert bucket_by_tag_01574([p]) == {"a": ["s1"]}
