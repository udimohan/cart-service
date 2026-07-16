"""Tests for catalog_01439."""

import pytest

from cartservice.generated.catalog_01439 import (
    Product_01439,
    bucket_by_tag_01439,
    is_valid_sku_01439,
    price_with_tax_01439,
)


def test_price_with_tax_01439():
    assert price_with_tax_01439(1000, 500) == 1050


def test_price_with_tax_negative_01439():
    with pytest.raises(ValueError):
        price_with_tax_01439(1000, -1)


def test_is_valid_sku_01439():
    assert is_valid_sku_01439("abc123")
    assert not is_valid_sku_01439("")


def test_bucket_by_tag_01439():
    p = Product_01439("s1", 100, ["a"])
    assert bucket_by_tag_01439([p]) == {"a": ["s1"]}
