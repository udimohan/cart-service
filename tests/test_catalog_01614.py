"""Tests for catalog_01614."""

import pytest

from cartservice.generated.catalog_01614 import (
    Product_01614,
    bucket_by_tag_01614,
    is_valid_sku_01614,
    price_with_tax_01614,
)


def test_price_with_tax_01614():
    assert price_with_tax_01614(1000, 500) == 1050


def test_price_with_tax_negative_01614():
    with pytest.raises(ValueError):
        price_with_tax_01614(1000, -1)


def test_is_valid_sku_01614():
    assert is_valid_sku_01614("abc123")
    assert not is_valid_sku_01614("")


def test_bucket_by_tag_01614():
    p = Product_01614("s1", 100, ["a"])
    assert bucket_by_tag_01614([p]) == {"a": ["s1"]}
