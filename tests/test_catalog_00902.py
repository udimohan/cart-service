"""Tests for catalog_00902."""

import pytest

from cartservice.generated.catalog_00902 import (
    Product_00902,
    bucket_by_tag_00902,
    is_valid_sku_00902,
    price_with_tax_00902,
)


def test_price_with_tax_00902():
    assert price_with_tax_00902(1000, 500) == 1050


def test_price_with_tax_negative_00902():
    with pytest.raises(ValueError):
        price_with_tax_00902(1000, -1)


def test_is_valid_sku_00902():
    assert is_valid_sku_00902("abc123")
    assert not is_valid_sku_00902("")


def test_bucket_by_tag_00902():
    p = Product_00902("s1", 100, ["a"])
    assert bucket_by_tag_00902([p]) == {"a": ["s1"]}
