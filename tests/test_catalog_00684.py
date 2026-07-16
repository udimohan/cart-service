"""Tests for catalog_00684."""

import pytest

from cartservice.generated.catalog_00684 import (
    Product_00684,
    bucket_by_tag_00684,
    is_valid_sku_00684,
    price_with_tax_00684,
)


def test_price_with_tax_00684():
    assert price_with_tax_00684(1000, 500) == 1050


def test_price_with_tax_negative_00684():
    with pytest.raises(ValueError):
        price_with_tax_00684(1000, -1)


def test_is_valid_sku_00684():
    assert is_valid_sku_00684("abc123")
    assert not is_valid_sku_00684("")


def test_bucket_by_tag_00684():
    p = Product_00684("s1", 100, ["a"])
    assert bucket_by_tag_00684([p]) == {"a": ["s1"]}
