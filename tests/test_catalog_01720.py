"""Tests for catalog_01720."""

import pytest

from cartservice.generated.catalog_01720 import (
    Product_01720,
    bucket_by_tag_01720,
    is_valid_sku_01720,
    price_with_tax_01720,
)


def test_price_with_tax_01720():
    assert price_with_tax_01720(1000, 500) == 1050


def test_price_with_tax_negative_01720():
    with pytest.raises(ValueError):
        price_with_tax_01720(1000, -1)


def test_is_valid_sku_01720():
    assert is_valid_sku_01720("abc123")
    assert not is_valid_sku_01720("")


def test_bucket_by_tag_01720():
    p = Product_01720("s1", 100, ["a"])
    assert bucket_by_tag_01720([p]) == {"a": ["s1"]}
