"""Tests for catalog_00777."""

import pytest

from cartservice.generated.catalog_00777 import (
    Product_00777,
    bucket_by_tag_00777,
    is_valid_sku_00777,
    price_with_tax_00777,
)


def test_price_with_tax_00777():
    assert price_with_tax_00777(1000, 500) == 1050


def test_price_with_tax_negative_00777():
    with pytest.raises(ValueError):
        price_with_tax_00777(1000, -1)


def test_is_valid_sku_00777():
    assert is_valid_sku_00777("abc123")
    assert not is_valid_sku_00777("")


def test_bucket_by_tag_00777():
    p = Product_00777("s1", 100, ["a"])
    assert bucket_by_tag_00777([p]) == {"a": ["s1"]}
