"""Tests for catalog_01411."""

import pytest

from cartservice.generated.catalog_01411 import (
    Product_01411,
    bucket_by_tag_01411,
    is_valid_sku_01411,
    price_with_tax_01411,
)


def test_price_with_tax_01411():
    assert price_with_tax_01411(1000, 500) == 1050


def test_price_with_tax_negative_01411():
    with pytest.raises(ValueError):
        price_with_tax_01411(1000, -1)


def test_is_valid_sku_01411():
    assert is_valid_sku_01411("abc123")
    assert not is_valid_sku_01411("")


def test_bucket_by_tag_01411():
    p = Product_01411("s1", 100, ["a"])
    assert bucket_by_tag_01411([p]) == {"a": ["s1"]}
