"""Tests for catalog_01023."""

import pytest

from cartservice.generated.catalog_01023 import (
    Product_01023,
    bucket_by_tag_01023,
    is_valid_sku_01023,
    price_with_tax_01023,
)


def test_price_with_tax_01023():
    assert price_with_tax_01023(1000, 500) == 1050


def test_price_with_tax_negative_01023():
    with pytest.raises(ValueError):
        price_with_tax_01023(1000, -1)


def test_is_valid_sku_01023():
    assert is_valid_sku_01023("abc123")
    assert not is_valid_sku_01023("")


def test_bucket_by_tag_01023():
    p = Product_01023("s1", 100, ["a"])
    assert bucket_by_tag_01023([p]) == {"a": ["s1"]}
