"""Tests for catalog_00171."""

import pytest

from cartservice.generated.catalog_00171 import (
    Product_00171,
    bucket_by_tag_00171,
    is_valid_sku_00171,
    price_with_tax_00171,
)


def test_price_with_tax_00171():
    assert price_with_tax_00171(1000, 500) == 1050


def test_price_with_tax_negative_00171():
    with pytest.raises(ValueError):
        price_with_tax_00171(1000, -1)


def test_is_valid_sku_00171():
    assert is_valid_sku_00171("abc123")
    assert not is_valid_sku_00171("")


def test_bucket_by_tag_00171():
    p = Product_00171("s1", 100, ["a"])
    assert bucket_by_tag_00171([p]) == {"a": ["s1"]}
