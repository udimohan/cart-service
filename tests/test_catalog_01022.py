"""Tests for catalog_01022."""

import pytest

from cartservice.generated.catalog_01022 import (
    Product_01022,
    bucket_by_tag_01022,
    is_valid_sku_01022,
    price_with_tax_01022,
)


def test_price_with_tax_01022():
    assert price_with_tax_01022(1000, 500) == 1050


def test_price_with_tax_negative_01022():
    with pytest.raises(ValueError):
        price_with_tax_01022(1000, -1)


def test_is_valid_sku_01022():
    assert is_valid_sku_01022("abc123")
    assert not is_valid_sku_01022("")


def test_bucket_by_tag_01022():
    p = Product_01022("s1", 100, ["a"])
    assert bucket_by_tag_01022([p]) == {"a": ["s1"]}
