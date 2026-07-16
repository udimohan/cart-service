"""Tests for catalog_00107."""

import pytest

from cartservice.generated.catalog_00107 import (
    Product_00107,
    bucket_by_tag_00107,
    is_valid_sku_00107,
    price_with_tax_00107,
)


def test_price_with_tax_00107():
    assert price_with_tax_00107(1000, 500) == 1050


def test_price_with_tax_negative_00107():
    with pytest.raises(ValueError):
        price_with_tax_00107(1000, -1)


def test_is_valid_sku_00107():
    assert is_valid_sku_00107("abc123")
    assert not is_valid_sku_00107("")


def test_bucket_by_tag_00107():
    p = Product_00107("s1", 100, ["a"])
    assert bucket_by_tag_00107([p]) == {"a": ["s1"]}
