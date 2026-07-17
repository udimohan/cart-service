"""Tests for catalog_01181."""

import pytest

from cartservice.generated.catalog_01181 import (
    Product_01181,
    bucket_by_tag_01181,
    is_valid_sku_01181,
    price_with_tax_01181,
)


def test_price_with_tax_01181():
    assert price_with_tax_01181(1000, 500) == 1050


def test_price_with_tax_negative_01181():
    with pytest.raises(ValueError):
        price_with_tax_01181(1000, -1)


def test_is_valid_sku_01181():
    assert is_valid_sku_01181("abc123")
    assert not is_valid_sku_01181("")


def test_bucket_by_tag_01181():
    p = Product_01181("s1", 100, ["a"])
    assert bucket_by_tag_01181([p]) == {"a": ["s1"]}
