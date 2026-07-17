"""Tests for catalog_01309."""

import pytest

from cartservice.generated.catalog_01309 import (
    Product_01309,
    bucket_by_tag_01309,
    is_valid_sku_01309,
    price_with_tax_01309,
)


def test_price_with_tax_01309():
    assert price_with_tax_01309(1000, 500) == 1050


def test_price_with_tax_negative_01309():
    with pytest.raises(ValueError):
        price_with_tax_01309(1000, -1)


def test_is_valid_sku_01309():
    assert is_valid_sku_01309("abc123")
    assert not is_valid_sku_01309("")


def test_bucket_by_tag_01309():
    p = Product_01309("s1", 100, ["a"])
    assert bucket_by_tag_01309([p]) == {"a": ["s1"]}
