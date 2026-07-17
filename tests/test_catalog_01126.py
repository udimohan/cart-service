"""Tests for catalog_01126."""

import pytest

from cartservice.generated.catalog_01126 import (
    Product_01126,
    bucket_by_tag_01126,
    is_valid_sku_01126,
    price_with_tax_01126,
)


def test_price_with_tax_01126():
    assert price_with_tax_01126(1000, 500) == 1050


def test_price_with_tax_negative_01126():
    with pytest.raises(ValueError):
        price_with_tax_01126(1000, -1)


def test_is_valid_sku_01126():
    assert is_valid_sku_01126("abc123")
    assert not is_valid_sku_01126("")


def test_bucket_by_tag_01126():
    p = Product_01126("s1", 100, ["a"])
    assert bucket_by_tag_01126([p]) == {"a": ["s1"]}
