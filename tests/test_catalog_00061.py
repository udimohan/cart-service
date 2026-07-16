"""Tests for catalog_00061."""

import pytest

from cartservice.generated.catalog_00061 import (
    Product_00061,
    bucket_by_tag_00061,
    is_valid_sku_00061,
    price_with_tax_00061,
)


def test_price_with_tax_00061():
    assert price_with_tax_00061(1000, 500) == 1050


def test_price_with_tax_negative_00061():
    with pytest.raises(ValueError):
        price_with_tax_00061(1000, -1)


def test_is_valid_sku_00061():
    assert is_valid_sku_00061("abc123")
    assert not is_valid_sku_00061("")


def test_bucket_by_tag_00061():
    p = Product_00061("s1", 100, ["a"])
    assert bucket_by_tag_00061([p]) == {"a": ["s1"]}
