"""Tests for catalog_01577."""

import pytest

from cartservice.generated.catalog_01577 import (
    Product_01577,
    bucket_by_tag_01577,
    is_valid_sku_01577,
    price_with_tax_01577,
)


def test_price_with_tax_01577():
    assert price_with_tax_01577(1000, 500) == 1050


def test_price_with_tax_negative_01577():
    with pytest.raises(ValueError):
        price_with_tax_01577(1000, -1)


def test_is_valid_sku_01577():
    assert is_valid_sku_01577("abc123")
    assert not is_valid_sku_01577("")


def test_bucket_by_tag_01577():
    p = Product_01577("s1", 100, ["a"])
    assert bucket_by_tag_01577([p]) == {"a": ["s1"]}
