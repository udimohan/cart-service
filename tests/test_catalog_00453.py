"""Tests for catalog_00453."""

import pytest

from cartservice.generated.catalog_00453 import (
    Product_00453,
    bucket_by_tag_00453,
    is_valid_sku_00453,
    price_with_tax_00453,
)


def test_price_with_tax_00453():
    assert price_with_tax_00453(1000, 500) == 1050


def test_price_with_tax_negative_00453():
    with pytest.raises(ValueError):
        price_with_tax_00453(1000, -1)


def test_is_valid_sku_00453():
    assert is_valid_sku_00453("abc123")
    assert not is_valid_sku_00453("")


def test_bucket_by_tag_00453():
    p = Product_00453("s1", 100, ["a"])
    assert bucket_by_tag_00453([p]) == {"a": ["s1"]}
