"""Tests for catalog_00359."""

import pytest

from cartservice.generated.catalog_00359 import (
    Product_00359,
    bucket_by_tag_00359,
    is_valid_sku_00359,
    price_with_tax_00359,
)


def test_price_with_tax_00359():
    assert price_with_tax_00359(1000, 500) == 1050


def test_price_with_tax_negative_00359():
    with pytest.raises(ValueError):
        price_with_tax_00359(1000, -1)


def test_is_valid_sku_00359():
    assert is_valid_sku_00359("abc123")
    assert not is_valid_sku_00359("")


def test_bucket_by_tag_00359():
    p = Product_00359("s1", 100, ["a"])
    assert bucket_by_tag_00359([p]) == {"a": ["s1"]}
