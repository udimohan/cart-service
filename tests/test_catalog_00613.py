"""Tests for catalog_00613."""

import pytest

from cartservice.generated.catalog_00613 import (
    Product_00613,
    bucket_by_tag_00613,
    is_valid_sku_00613,
    price_with_tax_00613,
)


def test_price_with_tax_00613():
    assert price_with_tax_00613(1000, 500) == 1050


def test_price_with_tax_negative_00613():
    with pytest.raises(ValueError):
        price_with_tax_00613(1000, -1)


def test_is_valid_sku_00613():
    assert is_valid_sku_00613("abc123")
    assert not is_valid_sku_00613("")


def test_bucket_by_tag_00613():
    p = Product_00613("s1", 100, ["a"])
    assert bucket_by_tag_00613([p]) == {"a": ["s1"]}
