"""Tests for catalog_01477."""

import pytest

from cartservice.generated.catalog_01477 import (
    Product_01477,
    bucket_by_tag_01477,
    is_valid_sku_01477,
    price_with_tax_01477,
)


def test_price_with_tax_01477():
    assert price_with_tax_01477(1000, 500) == 1050


def test_price_with_tax_negative_01477():
    with pytest.raises(ValueError):
        price_with_tax_01477(1000, -1)


def test_is_valid_sku_01477():
    assert is_valid_sku_01477("abc123")
    assert not is_valid_sku_01477("")


def test_bucket_by_tag_01477():
    p = Product_01477("s1", 100, ["a"])
    assert bucket_by_tag_01477([p]) == {"a": ["s1"]}
