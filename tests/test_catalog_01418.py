"""Tests for catalog_01418."""

import pytest

from cartservice.generated.catalog_01418 import (
    Product_01418,
    bucket_by_tag_01418,
    is_valid_sku_01418,
    price_with_tax_01418,
)


def test_price_with_tax_01418():
    assert price_with_tax_01418(1000, 500) == 1050


def test_price_with_tax_negative_01418():
    with pytest.raises(ValueError):
        price_with_tax_01418(1000, -1)


def test_is_valid_sku_01418():
    assert is_valid_sku_01418("abc123")
    assert not is_valid_sku_01418("")


def test_bucket_by_tag_01418():
    p = Product_01418("s1", 100, ["a"])
    assert bucket_by_tag_01418([p]) == {"a": ["s1"]}
