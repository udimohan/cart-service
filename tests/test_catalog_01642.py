"""Tests for catalog_01642."""

import pytest

from cartservice.generated.catalog_01642 import (
    Product_01642,
    bucket_by_tag_01642,
    is_valid_sku_01642,
    price_with_tax_01642,
)


def test_price_with_tax_01642():
    assert price_with_tax_01642(1000, 500) == 1050


def test_price_with_tax_negative_01642():
    with pytest.raises(ValueError):
        price_with_tax_01642(1000, -1)


def test_is_valid_sku_01642():
    assert is_valid_sku_01642("abc123")
    assert not is_valid_sku_01642("")


def test_bucket_by_tag_01642():
    p = Product_01642("s1", 100, ["a"])
    assert bucket_by_tag_01642([p]) == {"a": ["s1"]}
