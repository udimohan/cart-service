"""Tests for catalog_01445."""

import pytest

from cartservice.generated.catalog_01445 import (
    Product_01445,
    bucket_by_tag_01445,
    is_valid_sku_01445,
    price_with_tax_01445,
)


def test_price_with_tax_01445():
    assert price_with_tax_01445(1000, 500) == 1050


def test_price_with_tax_negative_01445():
    with pytest.raises(ValueError):
        price_with_tax_01445(1000, -1)


def test_is_valid_sku_01445():
    assert is_valid_sku_01445("abc123")
    assert not is_valid_sku_01445("")


def test_bucket_by_tag_01445():
    p = Product_01445("s1", 100, ["a"])
    assert bucket_by_tag_01445([p]) == {"a": ["s1"]}
