"""Tests for catalog_01342."""

import pytest

from cartservice.generated.catalog_01342 import (
    Product_01342,
    bucket_by_tag_01342,
    is_valid_sku_01342,
    price_with_tax_01342,
)


def test_price_with_tax_01342():
    assert price_with_tax_01342(1000, 500) == 1050


def test_price_with_tax_negative_01342():
    with pytest.raises(ValueError):
        price_with_tax_01342(1000, -1)


def test_is_valid_sku_01342():
    assert is_valid_sku_01342("abc123")
    assert not is_valid_sku_01342("")


def test_bucket_by_tag_01342():
    p = Product_01342("s1", 100, ["a"])
    assert bucket_by_tag_01342([p]) == {"a": ["s1"]}
