"""Tests for catalog_00559."""

import pytest

from cartservice.generated.catalog_00559 import (
    Product_00559,
    bucket_by_tag_00559,
    is_valid_sku_00559,
    price_with_tax_00559,
)


def test_price_with_tax_00559():
    assert price_with_tax_00559(1000, 500) == 1050


def test_price_with_tax_negative_00559():
    with pytest.raises(ValueError):
        price_with_tax_00559(1000, -1)


def test_is_valid_sku_00559():
    assert is_valid_sku_00559("abc123")
    assert not is_valid_sku_00559("")


def test_bucket_by_tag_00559():
    p = Product_00559("s1", 100, ["a"])
    assert bucket_by_tag_00559([p]) == {"a": ["s1"]}
