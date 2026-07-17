"""Tests for catalog_01084."""

import pytest

from cartservice.generated.catalog_01084 import (
    Product_01084,
    bucket_by_tag_01084,
    is_valid_sku_01084,
    price_with_tax_01084,
)


def test_price_with_tax_01084():
    assert price_with_tax_01084(1000, 500) == 1050


def test_price_with_tax_negative_01084():
    with pytest.raises(ValueError):
        price_with_tax_01084(1000, -1)


def test_is_valid_sku_01084():
    assert is_valid_sku_01084("abc123")
    assert not is_valid_sku_01084("")


def test_bucket_by_tag_01084():
    p = Product_01084("s1", 100, ["a"])
    assert bucket_by_tag_01084([p]) == {"a": ["s1"]}
