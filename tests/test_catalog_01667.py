"""Tests for catalog_01667."""

import pytest

from cartservice.generated.catalog_01667 import (
    Product_01667,
    bucket_by_tag_01667,
    is_valid_sku_01667,
    price_with_tax_01667,
)


def test_price_with_tax_01667():
    assert price_with_tax_01667(1000, 500) == 1050


def test_price_with_tax_negative_01667():
    with pytest.raises(ValueError):
        price_with_tax_01667(1000, -1)


def test_is_valid_sku_01667():
    assert is_valid_sku_01667("abc123")
    assert not is_valid_sku_01667("")


def test_bucket_by_tag_01667():
    p = Product_01667("s1", 100, ["a"])
    assert bucket_by_tag_01667([p]) == {"a": ["s1"]}
