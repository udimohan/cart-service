"""Tests for catalog_01078."""

import pytest

from cartservice.generated.catalog_01078 import (
    Product_01078,
    bucket_by_tag_01078,
    is_valid_sku_01078,
    price_with_tax_01078,
)


def test_price_with_tax_01078():
    assert price_with_tax_01078(1000, 500) == 1050


def test_price_with_tax_negative_01078():
    with pytest.raises(ValueError):
        price_with_tax_01078(1000, -1)


def test_is_valid_sku_01078():
    assert is_valid_sku_01078("abc123")
    assert not is_valid_sku_01078("")


def test_bucket_by_tag_01078():
    p = Product_01078("s1", 100, ["a"])
    assert bucket_by_tag_01078([p]) == {"a": ["s1"]}
