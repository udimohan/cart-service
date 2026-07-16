"""Tests for catalog_01154."""

import pytest

from cartservice.generated.catalog_01154 import (
    Product_01154,
    bucket_by_tag_01154,
    is_valid_sku_01154,
    price_with_tax_01154,
)


def test_price_with_tax_01154():
    assert price_with_tax_01154(1000, 500) == 1050


def test_price_with_tax_negative_01154():
    with pytest.raises(ValueError):
        price_with_tax_01154(1000, -1)


def test_is_valid_sku_01154():
    assert is_valid_sku_01154("abc123")
    assert not is_valid_sku_01154("")


def test_bucket_by_tag_01154():
    p = Product_01154("s1", 100, ["a"])
    assert bucket_by_tag_01154([p]) == {"a": ["s1"]}
