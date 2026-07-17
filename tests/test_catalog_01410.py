"""Tests for catalog_01410."""

import pytest

from cartservice.generated.catalog_01410 import (
    Product_01410,
    bucket_by_tag_01410,
    is_valid_sku_01410,
    price_with_tax_01410,
)


def test_price_with_tax_01410():
    assert price_with_tax_01410(1000, 500) == 1050


def test_price_with_tax_negative_01410():
    with pytest.raises(ValueError):
        price_with_tax_01410(1000, -1)


def test_is_valid_sku_01410():
    assert is_valid_sku_01410("abc123")
    assert not is_valid_sku_01410("")


def test_bucket_by_tag_01410():
    p = Product_01410("s1", 100, ["a"])
    assert bucket_by_tag_01410([p]) == {"a": ["s1"]}
