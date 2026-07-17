"""Tests for catalog_00558."""

import pytest

from cartservice.generated.catalog_00558 import (
    Product_00558,
    bucket_by_tag_00558,
    is_valid_sku_00558,
    price_with_tax_00558,
)


def test_price_with_tax_00558():
    assert price_with_tax_00558(1000, 500) == 1050


def test_price_with_tax_negative_00558():
    with pytest.raises(ValueError):
        price_with_tax_00558(1000, -1)


def test_is_valid_sku_00558():
    assert is_valid_sku_00558("abc123")
    assert not is_valid_sku_00558("")


def test_bucket_by_tag_00558():
    p = Product_00558("s1", 100, ["a"])
    assert bucket_by_tag_00558([p]) == {"a": ["s1"]}
