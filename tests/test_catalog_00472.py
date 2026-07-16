"""Tests for catalog_00472."""

import pytest

from cartservice.generated.catalog_00472 import (
    Product_00472,
    bucket_by_tag_00472,
    is_valid_sku_00472,
    price_with_tax_00472,
)


def test_price_with_tax_00472():
    assert price_with_tax_00472(1000, 500) == 1050


def test_price_with_tax_negative_00472():
    with pytest.raises(ValueError):
        price_with_tax_00472(1000, -1)


def test_is_valid_sku_00472():
    assert is_valid_sku_00472("abc123")
    assert not is_valid_sku_00472("")


def test_bucket_by_tag_00472():
    p = Product_00472("s1", 100, ["a"])
    assert bucket_by_tag_00472([p]) == {"a": ["s1"]}
