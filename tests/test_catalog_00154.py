"""Tests for catalog_00154."""

import pytest

from cartservice.generated.catalog_00154 import (
    Product_00154,
    bucket_by_tag_00154,
    is_valid_sku_00154,
    price_with_tax_00154,
)


def test_price_with_tax_00154():
    assert price_with_tax_00154(1000, 500) == 1050


def test_price_with_tax_negative_00154():
    with pytest.raises(ValueError):
        price_with_tax_00154(1000, -1)


def test_is_valid_sku_00154():
    assert is_valid_sku_00154("abc123")
    assert not is_valid_sku_00154("")


def test_bucket_by_tag_00154():
    p = Product_00154("s1", 100, ["a"])
    assert bucket_by_tag_00154([p]) == {"a": ["s1"]}
