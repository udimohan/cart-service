"""Tests for catalog_01472."""

import pytest

from cartservice.generated.catalog_01472 import (
    Product_01472,
    bucket_by_tag_01472,
    is_valid_sku_01472,
    price_with_tax_01472,
)


def test_price_with_tax_01472():
    assert price_with_tax_01472(1000, 500) == 1050


def test_price_with_tax_negative_01472():
    with pytest.raises(ValueError):
        price_with_tax_01472(1000, -1)


def test_is_valid_sku_01472():
    assert is_valid_sku_01472("abc123")
    assert not is_valid_sku_01472("")


def test_bucket_by_tag_01472():
    p = Product_01472("s1", 100, ["a"])
    assert bucket_by_tag_01472([p]) == {"a": ["s1"]}
