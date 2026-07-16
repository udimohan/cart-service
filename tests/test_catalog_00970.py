"""Tests for catalog_00970."""

import pytest

from cartservice.generated.catalog_00970 import (
    Product_00970,
    bucket_by_tag_00970,
    is_valid_sku_00970,
    price_with_tax_00970,
)


def test_price_with_tax_00970():
    assert price_with_tax_00970(1000, 500) == 1050


def test_price_with_tax_negative_00970():
    with pytest.raises(ValueError):
        price_with_tax_00970(1000, -1)


def test_is_valid_sku_00970():
    assert is_valid_sku_00970("abc123")
    assert not is_valid_sku_00970("")


def test_bucket_by_tag_00970():
    p = Product_00970("s1", 100, ["a"])
    assert bucket_by_tag_00970([p]) == {"a": ["s1"]}
