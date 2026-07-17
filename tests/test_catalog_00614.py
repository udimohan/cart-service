"""Tests for catalog_00614."""

import pytest

from cartservice.generated.catalog_00614 import (
    Product_00614,
    bucket_by_tag_00614,
    is_valid_sku_00614,
    price_with_tax_00614,
)


def test_price_with_tax_00614():
    assert price_with_tax_00614(1000, 500) == 1050


def test_price_with_tax_negative_00614():
    with pytest.raises(ValueError):
        price_with_tax_00614(1000, -1)


def test_is_valid_sku_00614():
    assert is_valid_sku_00614("abc123")
    assert not is_valid_sku_00614("")


def test_bucket_by_tag_00614():
    p = Product_00614("s1", 100, ["a"])
    assert bucket_by_tag_00614([p]) == {"a": ["s1"]}
