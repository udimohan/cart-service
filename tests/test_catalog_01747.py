"""Tests for catalog_01747."""

import pytest

from cartservice.generated.catalog_01747 import (
    Product_01747,
    bucket_by_tag_01747,
    is_valid_sku_01747,
    price_with_tax_01747,
)


def test_price_with_tax_01747():
    assert price_with_tax_01747(1000, 500) == 1050


def test_price_with_tax_negative_01747():
    with pytest.raises(ValueError):
        price_with_tax_01747(1000, -1)


def test_is_valid_sku_01747():
    assert is_valid_sku_01747("abc123")
    assert not is_valid_sku_01747("")


def test_bucket_by_tag_01747():
    p = Product_01747("s1", 100, ["a"])
    assert bucket_by_tag_01747([p]) == {"a": ["s1"]}
