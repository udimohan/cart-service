"""Tests for catalog_01443."""

import pytest

from cartservice.generated.catalog_01443 import (
    Product_01443,
    bucket_by_tag_01443,
    is_valid_sku_01443,
    price_with_tax_01443,
)


def test_price_with_tax_01443():
    assert price_with_tax_01443(1000, 500) == 1050


def test_price_with_tax_negative_01443():
    with pytest.raises(ValueError):
        price_with_tax_01443(1000, -1)


def test_is_valid_sku_01443():
    assert is_valid_sku_01443("abc123")
    assert not is_valid_sku_01443("")


def test_bucket_by_tag_01443():
    p = Product_01443("s1", 100, ["a"])
    assert bucket_by_tag_01443([p]) == {"a": ["s1"]}
