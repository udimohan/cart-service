"""Tests for catalog_01453."""

import pytest

from cartservice.generated.catalog_01453 import (
    Product_01453,
    bucket_by_tag_01453,
    is_valid_sku_01453,
    price_with_tax_01453,
)


def test_price_with_tax_01453():
    assert price_with_tax_01453(1000, 500) == 1050


def test_price_with_tax_negative_01453():
    with pytest.raises(ValueError):
        price_with_tax_01453(1000, -1)


def test_is_valid_sku_01453():
    assert is_valid_sku_01453("abc123")
    assert not is_valid_sku_01453("")


def test_bucket_by_tag_01453():
    p = Product_01453("s1", 100, ["a"])
    assert bucket_by_tag_01453([p]) == {"a": ["s1"]}
