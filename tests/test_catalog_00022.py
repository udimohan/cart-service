"""Tests for catalog_00022."""

import pytest

from cartservice.generated.catalog_00022 import (
    Product_00022,
    bucket_by_tag_00022,
    is_valid_sku_00022,
    price_with_tax_00022,
)


def test_price_with_tax_00022():
    assert price_with_tax_00022(1000, 500) == 1050


def test_price_with_tax_negative_00022():
    with pytest.raises(ValueError):
        price_with_tax_00022(1000, -1)


def test_is_valid_sku_00022():
    assert is_valid_sku_00022("abc123")
    assert not is_valid_sku_00022("")


def test_bucket_by_tag_00022():
    p = Product_00022("s1", 100, ["a"])
    assert bucket_by_tag_00022([p]) == {"a": ["s1"]}
