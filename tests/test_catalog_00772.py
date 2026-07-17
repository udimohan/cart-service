"""Tests for catalog_00772."""

import pytest

from cartservice.generated.catalog_00772 import (
    Product_00772,
    bucket_by_tag_00772,
    is_valid_sku_00772,
    price_with_tax_00772,
)


def test_price_with_tax_00772():
    assert price_with_tax_00772(1000, 500) == 1050


def test_price_with_tax_negative_00772():
    with pytest.raises(ValueError):
        price_with_tax_00772(1000, -1)


def test_is_valid_sku_00772():
    assert is_valid_sku_00772("abc123")
    assert not is_valid_sku_00772("")


def test_bucket_by_tag_00772():
    p = Product_00772("s1", 100, ["a"])
    assert bucket_by_tag_00772([p]) == {"a": ["s1"]}
