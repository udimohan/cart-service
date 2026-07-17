"""Tests for catalog_01107."""

import pytest

from cartservice.generated.catalog_01107 import (
    Product_01107,
    bucket_by_tag_01107,
    is_valid_sku_01107,
    price_with_tax_01107,
)


def test_price_with_tax_01107():
    assert price_with_tax_01107(1000, 500) == 1050


def test_price_with_tax_negative_01107():
    with pytest.raises(ValueError):
        price_with_tax_01107(1000, -1)


def test_is_valid_sku_01107():
    assert is_valid_sku_01107("abc123")
    assert not is_valid_sku_01107("")


def test_bucket_by_tag_01107():
    p = Product_01107("s1", 100, ["a"])
    assert bucket_by_tag_01107([p]) == {"a": ["s1"]}
