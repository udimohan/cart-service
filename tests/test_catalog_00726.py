"""Tests for catalog_00726."""

import pytest

from cartservice.generated.catalog_00726 import (
    Product_00726,
    bucket_by_tag_00726,
    is_valid_sku_00726,
    price_with_tax_00726,
)


def test_price_with_tax_00726():
    assert price_with_tax_00726(1000, 500) == 1050


def test_price_with_tax_negative_00726():
    with pytest.raises(ValueError):
        price_with_tax_00726(1000, -1)


def test_is_valid_sku_00726():
    assert is_valid_sku_00726("abc123")
    assert not is_valid_sku_00726("")


def test_bucket_by_tag_00726():
    p = Product_00726("s1", 100, ["a"])
    assert bucket_by_tag_00726([p]) == {"a": ["s1"]}
