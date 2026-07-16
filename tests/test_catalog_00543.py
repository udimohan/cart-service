"""Tests for catalog_00543."""

import pytest

from cartservice.generated.catalog_00543 import (
    Product_00543,
    bucket_by_tag_00543,
    is_valid_sku_00543,
    price_with_tax_00543,
)


def test_price_with_tax_00543():
    assert price_with_tax_00543(1000, 500) == 1050


def test_price_with_tax_negative_00543():
    with pytest.raises(ValueError):
        price_with_tax_00543(1000, -1)


def test_is_valid_sku_00543():
    assert is_valid_sku_00543("abc123")
    assert not is_valid_sku_00543("")


def test_bucket_by_tag_00543():
    p = Product_00543("s1", 100, ["a"])
    assert bucket_by_tag_00543([p]) == {"a": ["s1"]}
