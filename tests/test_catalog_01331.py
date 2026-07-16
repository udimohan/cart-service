"""Tests for catalog_01331."""

import pytest

from cartservice.generated.catalog_01331 import (
    Product_01331,
    bucket_by_tag_01331,
    is_valid_sku_01331,
    price_with_tax_01331,
)


def test_price_with_tax_01331():
    assert price_with_tax_01331(1000, 500) == 1050


def test_price_with_tax_negative_01331():
    with pytest.raises(ValueError):
        price_with_tax_01331(1000, -1)


def test_is_valid_sku_01331():
    assert is_valid_sku_01331("abc123")
    assert not is_valid_sku_01331("")


def test_bucket_by_tag_01331():
    p = Product_01331("s1", 100, ["a"])
    assert bucket_by_tag_01331([p]) == {"a": ["s1"]}
