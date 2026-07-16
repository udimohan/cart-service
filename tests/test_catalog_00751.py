"""Tests for catalog_00751."""

import pytest

from cartservice.generated.catalog_00751 import (
    Product_00751,
    bucket_by_tag_00751,
    is_valid_sku_00751,
    price_with_tax_00751,
)


def test_price_with_tax_00751():
    assert price_with_tax_00751(1000, 500) == 1050


def test_price_with_tax_negative_00751():
    with pytest.raises(ValueError):
        price_with_tax_00751(1000, -1)


def test_is_valid_sku_00751():
    assert is_valid_sku_00751("abc123")
    assert not is_valid_sku_00751("")


def test_bucket_by_tag_00751():
    p = Product_00751("s1", 100, ["a"])
    assert bucket_by_tag_00751([p]) == {"a": ["s1"]}
