"""Tests for catalog_01353."""

import pytest

from cartservice.generated.catalog_01353 import (
    Product_01353,
    bucket_by_tag_01353,
    is_valid_sku_01353,
    price_with_tax_01353,
)


def test_price_with_tax_01353():
    assert price_with_tax_01353(1000, 500) == 1050


def test_price_with_tax_negative_01353():
    with pytest.raises(ValueError):
        price_with_tax_01353(1000, -1)


def test_is_valid_sku_01353():
    assert is_valid_sku_01353("abc123")
    assert not is_valid_sku_01353("")


def test_bucket_by_tag_01353():
    p = Product_01353("s1", 100, ["a"])
    assert bucket_by_tag_01353([p]) == {"a": ["s1"]}
