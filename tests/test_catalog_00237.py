"""Tests for catalog_00237."""

import pytest

from cartservice.generated.catalog_00237 import (
    Product_00237,
    bucket_by_tag_00237,
    is_valid_sku_00237,
    price_with_tax_00237,
)


def test_price_with_tax_00237():
    assert price_with_tax_00237(1000, 500) == 1050


def test_price_with_tax_negative_00237():
    with pytest.raises(ValueError):
        price_with_tax_00237(1000, -1)


def test_is_valid_sku_00237():
    assert is_valid_sku_00237("abc123")
    assert not is_valid_sku_00237("")


def test_bucket_by_tag_00237():
    p = Product_00237("s1", 100, ["a"])
    assert bucket_by_tag_00237([p]) == {"a": ["s1"]}
