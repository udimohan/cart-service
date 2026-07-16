"""Tests for catalog_00761."""

import pytest

from cartservice.generated.catalog_00761 import (
    Product_00761,
    bucket_by_tag_00761,
    is_valid_sku_00761,
    price_with_tax_00761,
)


def test_price_with_tax_00761():
    assert price_with_tax_00761(1000, 500) == 1050


def test_price_with_tax_negative_00761():
    with pytest.raises(ValueError):
        price_with_tax_00761(1000, -1)


def test_is_valid_sku_00761():
    assert is_valid_sku_00761("abc123")
    assert not is_valid_sku_00761("")


def test_bucket_by_tag_00761():
    p = Product_00761("s1", 100, ["a"])
    assert bucket_by_tag_00761([p]) == {"a": ["s1"]}
