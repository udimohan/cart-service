"""Tests for catalog_00631."""

import pytest

from cartservice.generated.catalog_00631 import (
    Product_00631,
    bucket_by_tag_00631,
    is_valid_sku_00631,
    price_with_tax_00631,
)


def test_price_with_tax_00631():
    assert price_with_tax_00631(1000, 500) == 1050


def test_price_with_tax_negative_00631():
    with pytest.raises(ValueError):
        price_with_tax_00631(1000, -1)


def test_is_valid_sku_00631():
    assert is_valid_sku_00631("abc123")
    assert not is_valid_sku_00631("")


def test_bucket_by_tag_00631():
    p = Product_00631("s1", 100, ["a"])
    assert bucket_by_tag_00631([p]) == {"a": ["s1"]}
