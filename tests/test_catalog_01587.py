"""Tests for catalog_01587."""

import pytest

from cartservice.generated.catalog_01587 import (
    Product_01587,
    bucket_by_tag_01587,
    is_valid_sku_01587,
    price_with_tax_01587,
)


def test_price_with_tax_01587():
    assert price_with_tax_01587(1000, 500) == 1050


def test_price_with_tax_negative_01587():
    with pytest.raises(ValueError):
        price_with_tax_01587(1000, -1)


def test_is_valid_sku_01587():
    assert is_valid_sku_01587("abc123")
    assert not is_valid_sku_01587("")


def test_bucket_by_tag_01587():
    p = Product_01587("s1", 100, ["a"])
    assert bucket_by_tag_01587([p]) == {"a": ["s1"]}
