"""Tests for catalog_00071."""

import pytest

from cartservice.generated.catalog_00071 import (
    Product_00071,
    bucket_by_tag_00071,
    is_valid_sku_00071,
    price_with_tax_00071,
)


def test_price_with_tax_00071():
    assert price_with_tax_00071(1000, 500) == 1050


def test_price_with_tax_negative_00071():
    with pytest.raises(ValueError):
        price_with_tax_00071(1000, -1)


def test_is_valid_sku_00071():
    assert is_valid_sku_00071("abc123")
    assert not is_valid_sku_00071("")


def test_bucket_by_tag_00071():
    p = Product_00071("s1", 100, ["a"])
    assert bucket_by_tag_00071([p]) == {"a": ["s1"]}
