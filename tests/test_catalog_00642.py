"""Tests for catalog_00642."""

import pytest

from cartservice.generated.catalog_00642 import (
    Product_00642,
    bucket_by_tag_00642,
    is_valid_sku_00642,
    price_with_tax_00642,
)


def test_price_with_tax_00642():
    assert price_with_tax_00642(1000, 500) == 1050


def test_price_with_tax_negative_00642():
    with pytest.raises(ValueError):
        price_with_tax_00642(1000, -1)


def test_is_valid_sku_00642():
    assert is_valid_sku_00642("abc123")
    assert not is_valid_sku_00642("")


def test_bucket_by_tag_00642():
    p = Product_00642("s1", 100, ["a"])
    assert bucket_by_tag_00642([p]) == {"a": ["s1"]}
